install:
	python3 -m pip install --upgrade pip 
	python3 -m 	pip install -r requirements.txt

test:
	#python -m pytest -vv --cov=source/test_*.py
	python -m pytest --nbval source/*.ipynb
	python -m pytest -vv --cov=main --cov=lib test_*.py

format:	
	black source/*.py 
	nbqa black source/*.ipynb

lint:
	nbqa ruff source/*.ipynb
	ruff check source/*.py

refactor: format lint	

all: install lint format test