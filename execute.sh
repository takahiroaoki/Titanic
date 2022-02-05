#!/bin/bash
#"titanic" directory

#############################
## Execution of main.ipynb ##
#############################
# [Define Variants]
OUTPUT_DIR="./output"
FILE_NAME="test"

# Execution
jupyter nbconvert main.ipynb --to markdown --output "${FILE_NAME}.md" --execute --debug

# Tuning path to display png files in markdown
rm -rf "${OUTPUT_DIR}/${FILE_NAME}"
mkdir "${OUTPUT_DIR}/${FILE_NAME}"
mv -f "${FILE_NAME}.md" "${OUTPUT_DIR}/${FILE_NAME}"
mv -f "${FILE_NAME}_files" "${OUTPUT_DIR}/${FILE_NAME}"

#################
## LINE notify ##
#################
# [Define Variants]
MY_TOKEN="LINE NOTIFY TOKEN"
MESSAGE="We executed main.ipynb and created ${OUTPUT_DIR}/${FILE_NAME}/${FILE_NAME}.md."

# Notification
curl -X POST -H "Authorization: Bearer ${MY_TOKEN}" -F "message=${MESSAGE}" https://notify-api.line.me/api/notify
