#!/usr/bin/env bash
set -e
echo

loc_repo="$(dirname "$(pwd)")"
loc_multiwoz="$(pwd)"
loc_package="$(pwd)/multiwoz"
loc_compute="$(pwd)/compute"
loc_scripts="${loc_package}/scripts"
loc_data="${loc_package}/data"

# Helper functions ##############################

slack_notify () {
    MSG=$1
    curl -X POST -H 'Content-type: application/json' --data '{"text":"<@UJV1L1X34>: '"${MSG}"'"}' https://hooks.slack.com/services/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
}

ask_yn() {
    # Original: https://gist.github.com/davejamesmiller/1965569
    local prompt default reply

    if [[ "${2:-}" = "Y" ]]; then
        prompt="Y/n"
        default=Y
    elif [[ "${2:-}" = "N" ]]; then
        prompt="y/N"
        default=N
    else
        prompt="y/n"
        default=
    fi

    while true; do

        # Ask the question (not using "read -p" as it uses stderr not stdout)
        echo -n "$1 [$prompt] "

        read reply

        # Default?
        if [ -z "$reply" ]; then
            reply=$default
        fi

        # Check if the reply is valid
        case "$reply" in
            Y*|y*) return 0 ;;
            N*|n*) return 1 ;;
        esac

    done
}

# Gather more information
#################################################

# Parameter list for parser
PARAMS=(${loc_data})
PARAMS+=(--action-encoding minimal)

echo "Source code location:"
echo ${loc_package}
echo

echo "Current commit:"
COMMIT="$(git --git-dir="${loc_repo}/.git" log --pretty=format:'%H' -n 1)"
echo ${COMMIT}
echo

echo "Current branch:"
BRANCH="$(git --git-dir="${loc_repo}/.git" branch | grep \* | cut -d ' ' -f2)"
echo ${BRANCH}
echo

echo "Current date and time:"
DATE=`date '+%Y%m%d-%H%M%S'`
echo ${DATE}
echo

echo "Configuration:"
read -p "Title of the experiment:        " config_title
read -p "Number of training stories:     " config_num_train
if ask_yn "Prune the story tree?"; then
    config_prune="y"
else
    config_prune="n"
fi
if ask_yn "Add status slots?"; then
    config_add_status="y"
    PARAMS+=(--add-status-slots)
else
    config_add_status="n"
fi
read -p "Slot simplification level [1]:  " config_slot_simplification
config_slot_simplification=${config_slot_simplification:-1}
PARAMS+=(--slot-simplification ${config_slot_simplification})
read -p "Chitchat weights [0]:           " config_chitchat_weights
config_chitchat_weights=${config_chitchat_weights:-0}
PARAMS+=(--chitchat ${config_chitchat_weights})
read -p "Chitchat story fraction [0]:    " config_chitchat_story_fraction
config_chitchat_story_fraction=${config_chitchat_story_fraction:-0}
PARAMS+=(--chitchat-story-fraction ${config_chitchat_story_fraction})
read -p "Chitchat variability [0]:       " config_chitchat_variability
config_chitchat_variability=${config_chitchat_variability:-0}
PARAMS+=(--chitchat-variability ${config_chitchat_variability})
echo "Action names can be merged in the following ways:"
echo "  (0): Do not merge action names"
echo "  (1): Merge bye, greet, and welcome into welcome"
echo "  (2): Also merge inform, recommend, and select to advise"
echo "  (3): Also merge request and advise to reply"
read -p "Which merge list do you choose? [0]:  " config_name_merge_list
config_name_merge_list=${config_name_merge_list:-0}
PARAMS+=(--name-merge-list ${config_name_merge_list})
if ask_yn "Keep 'book_booking_...' actions?" "Y"; then
    config_keep_book_booking="y"
    PARAMS+=(--keep-book-booking)
else
    config_keep_book_booking="n"
fi
if ask_yn "Keep all 'reqmore_general' actions?" "Y"; then
    config_keep_reqmore="y"
    PARAMS+=(--keep-reqmore)
else
    config_keep_reqmore="n"
fi
if ask_yn "Keep 'nooffer' actions?" "Y"; then
    config_keep_nooffer="y"
    PARAMS+=(--keep-nooffer)
else
    config_keep_nooffer="n"
fi
if ask_yn "Use new MultiWOZ 2.1 data set?" "Y"; then
    config_21="2.1"
else
    config_21="2.0"
fi
PARAMS+=(--dataset-version ${config_21})

config_name="${DATE}-${config_title}"


# Start setup
#################################################

echo
if ! ask_yn "Ready to start setup. Continue?"; then
    exit 1
fi

# Parse stories
# Creates: stories_all.md, stories_testlist.md, stories_vallist.md, domain.yml
PYTHONPATH=${loc_multiwoz} python3 ${loc_scripts}/parse_stories.py "${PARAMS[@]}"

# Generate prune list (those stories combine to an unambiguous tree)
# Creates: prune_list.txt
if [[ ${config_prune} == "y" ]]; then
    echo "Creating prune_list.txt..."
    PYTHONPATH=${loc_multiwoz} python3 ${loc_scripts}/story_tree.py ${loc_data}/stories_all.md --prune most-visited --output pruned > ${loc_data}/prune_list.txt
fi

# Copy files
#################################################

echo
mkdir ${loc_compute}/${config_name}
echo "Copying template files..."
cp -r ${loc_compute}/template/. ${loc_compute}/${config_name}
echo "Copying domain file..."
cp "${loc_data}/domain.yml" "${loc_compute}/${config_name}/domain.yml"

echo "*" > "${loc_compute}/${config_name}/.gitignore"

if [[ ${config_prune} == "y" ]]; then
    python3 "${loc_scripts}/prepare_stories.py" \
        "${loc_data}/stories_all.md" \
        --filter "${loc_data}/prune_list.txt" \
        --train "${loc_compute}/${config_name}/data/train/stories.md" \
        --test "${loc_compute}/${config_name}/data/test/stories.md" \
        --num-train ${config_num_train}
else
    python3 "${loc_scripts}/prepare_stories.py" \
        "${loc_data}/stories_all.md" \
        --train "${loc_compute}/${config_name}/data/train/stories.md" \
        --test "${loc_compute}/${config_name}/data/test/stories.md" \
        --num-train ${config_num_train}
fi

# Inform statistics
#################################################

echo
echo "TRAINING SET INSIGHTS ---------------------"
python3 "${loc_scripts}/prepare_stories.py" \
 "${loc_compute}/${config_name}/data/train/stories.md" \
 --insights

echo
echo "TESTING SET INSIGHTS ----------------------"
python3 "${loc_scripts}/prepare_stories.py" \
 "${loc_compute}/${config_name}/data/test/stories.md" \
 --insights

echo

python3 "${loc_scripts}/read_stories.py" "${loc_compute}/${config_name}/data/test/stories.md"

echo

# Write README
#################################################

README="${loc_compute}/${config_name}/README.md"

echo "Writing README.md..."
echo "## ${config_title}" >> ${README}
echo "" >> ${README}
echo "date:   ${DATE}" >> ${README}
echo "commit: ${COMMIT} (${BRANCH})" >> ${README}
echo "" >> ${README}
echo "Use MultiWOZ 2.1:          ${config_21}" >> ${README}
echo "Action name merge list:    ${config_name_merge_list}" >> ${README}
echo "Slot simplification level: ${config_slot_simplification}" >> ${README}
echo "Add status slots:          ${config_add_status}" >> ${README}
echo "Prune story tree:          ${config_prune}" >> ${README}
echo "Keep book_booking:         ${config_keep_book_booking}" >> ${README}
echo "Keep reqmore:              ${config_keep_reqmore}" >> ${README}
echo "Keep nooffer:              ${config_keep_nooffer}" >> ${README}
echo "" >> ${README}
echo "Chitchat infusion weights: ${config_chitchat_weights}" >> ${README}
echo "Chitchat story fraction:   ${config_chitchat_story_fraction}" >> ${README}
echo "Chitchat variability:      ${config_chitchat_variability}" >> ${README}
echo "" >> ${README}

echo
if ask_yn "Do you wish to edit the README.md in vim?" "N"; then
    vim ${README}
fi
if ask_yn "Do you wish to edit the config.yml in vim?" "N"; then
    vim "${loc_compute}/${config_name}/config.yml"
fi

echo "Done."
