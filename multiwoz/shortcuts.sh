#!/usr/bin/env bash

MWOZ_DIR=$(pwd)
MWOZ_SCRIPT_DIR="$(pwd)/multiwoz/scripts"

echo "MWOZ_DIR = ${MWOZ_DIR}"

MWOZ_READ() {
  python3 ${MWOZ_SCRIPT_DIR}/read_stories.py $*
}

MWOZ_LOOKUP() {
  cd ${MWOZ_DIR}
  PYTHONPATH=${MWOZ_DIR} python3 ${MWOZ_SCRIPT_DIR}/lookup_action.py
  cd -
}

MWOZ_STORY() {
  cd ${MWOZ_DIR}
  PYTHONPATH=${MWOZ_DIR} python3 ${MWOZ_SCRIPT_DIR}/lookup_story.py $*
  cd -
}

MWOZ_TREE() {
  python3 ${MWOZ_SCRIPT_DIR}/story_tree.py $*
}

MWOZ_INFO() {
  python3 ${MWOZ_SCRIPT_DIR}/prepare_stories.py $* --insights
}