while true
do
	echo $PWD
	python background_train.py
	echo "Train finished"
	t=$((3600*24*30*6))
	sleep $t
done