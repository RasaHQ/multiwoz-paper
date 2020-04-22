#!/usr/bin/env bash
set -e
echo

loc_repo="$(dirname "$(pwd)")"
loc_multiwoz="$(pwd)"
loc_package="$(pwd)/multiwoz"
loc_compute="$(pwd)/compute"
loc_scripts="${loc_package}/scripts"
loc_data="${loc_package}/data"

# Helper functions
#################################################

slack_notify () {
    MSG=$1
    curl -X POST -H 'Content-type: application/json' --data '{"text":"<@UJV1L1X34>: '"${MSG}"'"}' https://hooks.slack.com/services/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
}

notify () {
    MSG=$1
    echo ${MSG}
    if [[ ${use_slack} == "y" ]]; then
        slack_notify "${MSG}"
    fi
}

raise () {
    MSG="ERROR: ${1}"
    notify "${MSG}"
    exit 1
}

ask() {
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
        if [[ -z "$reply" ]]; then
            reply=${default}
        fi

        # Check if the reply is valid
        case "$reply" in
            Y*|y*) return 0 ;;
            N*|n*) return 1 ;;
        esac

    done
}

# Gather information
#################################################

use_slack="n"

echo "Which experiment(s) would you investigate?"
python3 ask_computation.py  # Without parameters, the list of experiments is printed

echo
echo -n "I want to investigate experiment(s) number: "
read experiment
readarray -t experiments < <( python3 ask_computation.py ${experiment} )

num_experiments=${#experiments[@]}

# Investigate experiments
#################################################

echo
n=1
for e in "${experiments[@]}"; do

    echo
    echo ${e}
    echo "---------------------------------------"
    echo

    grep "Start of experiment" \
    ${loc_compute/}/${e}/README.md -A 1 || echo "No start time stamp"

    grep "End of experiment" \
    ${loc_compute/}/${e}/README.md -A 1 || echo "No end time stamp"

    grep "Chitchat infusion weights" \
    ${loc_compute/}/${e}/README.md -A 2 || echo "No construction info"

    echo "TRAINING scores:"
    grep "Evaluation Results on CONVERSATION level" \
    ${loc_compute/}/${e}/test-train.out -A 11 | cut -c 48-

    echo "TESTING scores:"
    grep "Evaluation Results on CONVERSATION level" \
    ${loc_compute/}/${e}/test-test.out -A 11 | cut -c 48-

    echo

    if [[ ${n} -lt ${num_experiments} ]]; then
        if ! ask "Investigate next experiment?" "Y"; then
            exit 1
        fi
    fi

    let "n++"
done
