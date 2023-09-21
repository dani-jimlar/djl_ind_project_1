all: install test format lint 

install:
	python3 -m pip install --upgrade pip 
	python3 -m 	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=src src/test_*.py
	python -m pytest --nbval src/*.ipynb

format:	
	black source/*.py 
	nbqa black src/*.ipynb

lint:
	nbqa ruff src/*.ipynb
	ruff check src/*.py

all: install lint format test 