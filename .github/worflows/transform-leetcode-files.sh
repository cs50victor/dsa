SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
for file in `ls leetcode`; do
	if [ ! -f "$file" ]; then
		cleanName=`tr '[:blank:]' '-' <<< "$file"`
		cleanName=`tr '[:upper:]' '[:lower:]' <<< "$cleanName"`
		if [ $file != $cleanName ]; then
			mv "$file" $cleanName
		fi
	fi
done
IFS=$SAVEIFS