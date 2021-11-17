#!/bin/bash

# Script checks line length is equal in transcript txt file and output bed file
# Checks both files are present - if paths invalid, throws error
# Gets NM/NR number from column 1 of text file, checks if present in file 2 and if isn't, appends NM number of missing
# transcript to string
# Output message depending on whether or not missing transcripts have been found

# Get command line arguments
TRANSCRIPT_FILE=$1
BED_FILE=$2

missing_transcripts=()
if [[ -f ${TRANSCRIPT_FILE} ]] && [[ -f ${BED_FILE} ]]; then
  while read -r line; do
    if [[ "$line" == NM* ]] || [[ "$line" == NR* ]]; then
      transcript=$(echo "$line" | awk '{print $1}')
      if ! grep -q "$transcript" "${BED_FILE}"; then
        missing_transcripts+=("${transcript}")
      fi;
    fi;
  done < "${TRANSCRIPT_FILE}"

  if ((${#missing_transcripts[@]} == 0)); then
    echo "Bed file as expected (all transcripts present)"
  else
      echo "Transcripts missing from bed file: ${missing_transcripts[*]}"
  fi;
else
  echo "Error: Invalid file paths"
fi;