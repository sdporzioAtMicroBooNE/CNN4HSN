nOutFiles=0

for i in $(seq 0 ${nOutFiles})
do
	echo "python mergeFiles.py ${i}"
	python mergeFiles.py ${i}
done