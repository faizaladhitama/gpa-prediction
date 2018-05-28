while true
do
	echo "Running Machine Learning Model..."
	python api/ml_models/background_train.py
	echo "Train finished"
	t=$((3600*24*30*6))
	sleep $t
done