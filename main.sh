allPythonFiles=($(find * -name '*.py'| sort))

for i in ${!allPythonFiles[@]}; do
  echo "[$i] ${allPythonFiles[$i]}"
done
read -p " # > " index
echo -e "------------------------\n\n"
clear
python ${allPythonFiles[$index]}