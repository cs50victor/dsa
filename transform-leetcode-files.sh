#!/bin/sh

SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
cwd='leetcode'
ext='py'
for file in `ls ${cwd}`; do
	if [ ! -f "$file" ]; then
		cleanName=`tr [:upper:] [:lower:] <<< "${file%.*}"`
		cleanName=`tr ' ' '-' <<< "${cleanName}"`
		cleanName=`tr -d '.' <<< "${cleanName}"`
		if [ $file != "$cleanName.$ext" ]; then
			mv "${cwd}/$file" "${cwd}/$cleanName.$ext"
		fi
	fi
done
IFS=$SAVEIFS