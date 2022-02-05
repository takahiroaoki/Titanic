#!/bin/bash
#"titanic" directory

#############################
## Execution of main.ipynb ##
#############################
# [Define Variants]
OUTPUT_BASE="./output"
DIR_NAME="test2"

# Execution
jupyter nbconvert main.ipynb --to markdown --output "${DIR_NAME}.md" --execute --debug

# Tuning path to display png files in markdown
rm -rf "${OUTPUT_BASE}/${DIR_NAME}"
mkdir "${OUTPUT_BASE}/${DIR_NAME}"
mv -f "${DIR_NAME}.md" "${OUTPUT_BASE}/${DIR_NAME}"
mv -f "${DIR_NAME}_files" "${OUTPUT_BASE}/${DIR_NAME}"

#################
## LINE notify ##
#################
# [Define Variants]
MY_TOKEN="LINE NOTIFY TOKEN"
MESSAGE="We executed main.ipynb and created ${OUTPUT_BASE}/${DIR_NAME}/${DIR_NAME}.md."

# Notification
curl -X POST -H "Authorization: Bearer ${MY_TOKEN}" -F "message=${MESSAGE}" https://notify-api.line.me/api/notify
