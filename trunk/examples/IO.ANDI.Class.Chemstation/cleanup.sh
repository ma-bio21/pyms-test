#!/bin/bash

# - define outputs -
PROC_OUT="proc.py.out" # output of the proc.py script
OUTPUT_DIR="output" # the directory with other output files

# - do not modify below -
echo -ne "\n Hello (from cleanup.sh)\n"

if [ -e $PROC_OUT ]; then
  echo -ne " -> Removing $PROC_OUT\n"
  rm $PROC_OUT
fi

OUT_FILES=`ls $OUTPUT_DIR`

for file in $OUT_FILES
do
  if [ -e $OUTPUT_DIR/$file ]; then 
    echo -ne " -> Removing $OUTPUT_DIR/$file\n"
    rm $OUTPUT_DIR/$file
  fi
done

echo -ne " All done.\n\n"

