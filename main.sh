allPythonFiles=($(find * -name '*.py'| sort))

for i in ${!allPythonFiles[@]}; do
  echo "[$i] ${allPythonFiles[$i]}"
done
read -p " # > " index
echo -e "------------------------\n\n"
python ${allPythonFiles[$index]}