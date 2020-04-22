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
read -p "Title of the baseline experiment: " config_title_base
read -p "Title of the actual experiment:   " config_title
read -p "Number of training stories: " config_num_train
read -p "Chitchat weights:           " config_chitchat_weights
read -p "Chitchat story fraction:    " config_chitchat_story_fraction
read -p "Chitchat variability:       " config_chitchat_variability
read -p "Slot simplification level:  " config_slot_simplification
if ask_yn "Keep 'request' action separate?"; then
    config_separate_request="y"
else
    config_separate_request="n"
fi
if ask_yn "Use prune list?" "Y"; then
    config_prune="y"
else
    config_prune="n"
fi
if ask_yn "Use new MultiWOZ 2.1 data set?" "Y"; then
    config_21="2.1"
else
    config_21="2.0"
fi

# Start setup
#################################################

echo
if ! ask_yn "Ready to start setup. Continue?" "N"; then
    exit 1
fi

# Parse stories
# Creates: stories_all.md, stories_testlist.md, stories_vallist.md, domain.yml
if [[ ${config_separate_request} == "y" ]]; then
    PYTHONPATH=${loc_multiwoz} python3 ${loc_scripts}/parse_stories.py ${loc_data} \
        --dataset-version ${config_21} \
        --action-encoding minimal \
        --slot-simplification ${config_slot_simplification} \
        --chitchat ${config_chitchat_weights} \
        --chitchat-story-fraction ${config_chitchat_story_fraction} \
        --chitchat-variability ${config_chitchat_variability} \
        --separate-request
else
    PYTHONPATH=${loc_multiwoz} python3 ${loc_scripts}/parse_stories.py ${loc_data} \
        --dataset-version ${config_21} \
        --action-encoding minimal \
        --slot-simplification ${config_slot_simplification} \
        --chitchat ${config_chitchat_weights} \
        --chitchat-story-fraction ${config_chitchat_story_fraction} \
        --chitchat-variability ${config_chitchat_variability}
fi

# Split stories into two sets
# All domains: attraction booking general hotel restaurant taxi train
python3 "${loc_scripts}/prepare_stories.py" \
    "${loc_data}/stories_all.md" \
    --train "${loc_data}/stories_set1.md" \
    --test "${loc_data}/stories_set2.md" \
    --train-domains booking general hotel restaurant \
    --test-domains attraction general taxi train

# Copy files
#################################################

config_name="${DATE}-${config_title_base}"

echo
mkdir ${loc_compute}/${config_name}
echo "Copying template files for baseline..."
cp -r ${loc_compute}/template/. ${loc_compute}/${config_name}
echo "Copying domain file for baseline..."
cp "${loc_data}/domain.yml" "${loc_compute}/${config_name}/domain.yml"

echo "*" > "${loc_compute}/${config_name}/.gitignore"

if [[ ${config_prune} == "y" ]]; then

    # Find subset of union of both sets that is self-consistent
    # in terms of wizard actions
    echo "Creating prune_list..."
    PYTHONPATH=${loc_multiwoz} python3 ${loc_scripts}/story_tree.py \
      ${loc_data}/stories_set1.md \
      --prune most-visited \
      --output pruned > ${loc_data}/prune_list.txt

    echo "Preparing baseline data..."
    python3 "${loc_scripts}/prepare_stories.py" \
        "${loc_data}/stories_set1.md" \
        --filter "${loc_data}/prune_list.txt" \
        --train "${loc_compute}/${config_name}/data/train/stories.md" \
        --test "${loc_compute}/${config_name}/data/test/stories.md" \
        --num-train ${config_num_train}
else
    echo "Preparing baseline data..."
    python3 "${loc_scripts}/prepare_stories.py" \
        "${loc_data}/stories_set1.md" \
        --train "${loc_compute}/${config_name}/data/train/stories.md" \
        --test "${loc_compute}/${config_name}/data/test/stories.md" \
        --num-train ${config_num_train}
fi

config_name="${DATE}-${config_title}"

echo
mkdir ${loc_compute}/${config_name}
echo "Copying template files for augmented experiment..."
cp -r ${loc_compute}/template/. ${loc_compute}/${config_name}
echo "Copying domain file for augmented experiment..."
cp "${loc_data}/domain.yml" "${loc_compute}/${config_name}/domain.yml"

echo "*" > "${loc_compute}/${config_name}/.gitignore"

if [[ ${config_prune} == "y" ]]; then

    # Find subset of union of both sets that is self-consistent
    # in terms of wizard actions
    echo "Creating prune_list..."
    PYTHONPATH=${loc_multiwoz} python3 ${loc_scripts}/story_tree.py \
      ${loc_data}/stories_set1.md \
      ${loc_data}/stories_set2.md \
      --prune most-visited \
      --output pruned > ${loc_data}/prune_list.txt

    echo "Preparing augmented data..."
    python3 "${loc_scripts}/prepare_stories.py" \
        "${loc_data}/stories_set1.md" \
        --filter "${loc_data}/prune_list.txt" \
        --train "${loc_compute}/${config_name}/data/train/stories.md" \
        --test "${loc_compute}/${config_name}/data/test/stories.md" \
        --num-train ${config_num_train}
else
    echo "Preparing augmented data..."
    python3 "${loc_scripts}/prepare_stories.py" \
        "${loc_data}/stories_set1.md" \
        --train "${loc_compute}/${config_name}/data/train/stories.md" \
        --test "${loc_compute}/${config_name}/data/test/stories.md" \
        --num-train ${config_num_train}
fi

if [[ ${config_prune} == "y" ]]; then
    # List the stories in set 2 that we can merge into the baseline training set
    # to create the full training set
    echo "Creating merge_list..."
    PYTHONPATH=${loc_multiwoz} python3 ${loc_scripts}/story_tree.py \
      "${loc_compute}/${config_name}/data/train/stories.md" \
      --merge ${loc_data}/stories_set2.md \
      --prune most-visited \
      --output pruned > ${loc_data}/merge_list.txt

    # Append stories from set 2 to training stories file, except for those not on the merge_list
    echo "Appending second data set to training set..."
    python3 "${loc_scripts}/cat_stories.py" \
      "${loc_compute}/${config_name}/data/train/stories.md" \
      ${loc_data}/stories_set2.md \
      --filter ${loc_data}/merge_list.txt

else
    echo "Appending second data set to training set..."
    cat "${loc_data}/stories_set2.md" >> "${loc_compute}/${config_name}/data/train/stories.md"
fi

# Inform statistics
#################################################

config_name="${DATE}-${config_title_base}"

echo
echo "TRAINING SET INSIGHTS [baseline] ----------"
python3 "${loc_scripts}/prepare_stories.py" \
 "${loc_compute}/${config_name}/data/train/stories.md" \
 --insights

config_name="${DATE}-${config_title}"

echo
echo "TRAINING SET INSIGHTS [full] --------------"
python3 "${loc_scripts}/prepare_stories.py" \
 "${loc_compute}/${config_name}/data/train/stories.md" \
 --insights

echo
echo "TESTING SET INSIGHTS ----------------------"
python3 "${loc_scripts}/prepare_stories.py" \
 "${loc_compute}/${config_name}/data/test/stories.md" \
 --insights

echo

# Write READMEs
#################################################

config_name="${DATE}-${config_title_base}"
README="${loc_compute}/${config_name}/README.md"

echo "Writing README.md (base)..."
echo "## ${config_title_base}" >> ${README}
echo "" >> ${README}
echo "Baseline experiment to ${DATE}-${config_title}" >> ${README}
echo "" >> ${README}
echo "date:   ${DATE}" >> ${README}
echo "commit: ${COMMIT} (${BRANCH})" >> ${README}
echo "" >> ${README}
echo "Chitchat infusion weights: ${config_chitchat_weights}" >> ${README}
echo "Chitchat story fraction:   ${config_chitchat_story_fraction}" >> ${README}
echo "Chitchat variability:      ${config_chitchat_variability}" >> ${README}
echo "Slot simplification level: ${config_slot_simplification}" >> ${README}
echo "Separate request action:   ${config_separate_request}" >> ${README}
echo "" >> ${README}

config_name="${DATE}-${config_title}"
README="${loc_compute}/${config_name}/README.md"

echo "Writing README.md (full)..."
echo "## ${config_title}" >> ${README}
echo "" >> ${README}
echo "Augmented experiment to baseline ${DATE}-${config_title_base}" >> ${README}
echo "" >> ${README}
echo "date:   ${DATE}" >> ${README}
echo "commit: ${COMMIT} (${BRANCH})" >> ${README}
echo "" >> ${README}
echo "Chitchat infusion weights: ${config_chitchat_weights}" >> ${README}
echo "Chitchat story fraction:   ${config_chitchat_story_fraction}" >> ${README}
echo "Chitchat variability:      ${config_chitchat_variability}" >> ${README}
echo "Slot simplification level: ${config_slot_simplification}" >> ${README}
echo "Separate request action:   ${config_separate_request}" >> ${README}
echo "" >> ${README}

echo "Done."
