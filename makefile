run: 
	python src/__main__.py
	
init:
	pip install -r requirements.txt

test:
	nosetests tests