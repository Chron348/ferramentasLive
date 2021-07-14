run: 
	python src/__main__.py

init:
	pip install -r requirements.txt

test:
	python -m livetools/services/test/__service_test__.py