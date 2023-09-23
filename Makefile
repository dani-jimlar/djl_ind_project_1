all: install test format lint 

install:
	python3 -m pip install --upgrade pip 
	python3 -m 	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=source source/test_*.py
	python -m pytest --nbval source/*.ipynb

format:	
	black source/*.py 
	nbqa black source/*.ipynb

lint:
	nbqa ruff source/*.ipynb
	ruff check source/*.py

all: install lint format test 