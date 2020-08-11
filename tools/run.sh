#!/usr/bin/env bash

set -e

ENDPOINT_ID=$1

if [ "$1" = "" -o "$1" = "--help" -o "$1" = "-help" -o "$1" = "-h" ]; then
    echo "Usage: $0 SESSIONIZE_ENDPOINT_ID" 1>&2
    echo "Run entrypoint to fetch sessions data from Sessionize."
    exit 1
fi

SCRIPT_DIR=$(cd $(dirname $0); pwd)

SESSIONS_LIST_ENDPOINT="https://sessionize.com/api/v2/${ENDPOINT_ID}/view/Sessions"
SPEAKERS_LIST_ENDPOINT="https://sessionize.com/api/v2/${ENDPOINT_ID}/view/Speakers"
# Required python>=3.7.0
python ${SCRIPT_DIR}/main.py ${SESSIONS_LIST_ENDPOINT} ${SPEAKERS_LIST_ENDPOINT} \
    -l ${SCRIPT_DIR}/data/invited.json -d ${SCRIPT_DIR}/talks.csv
