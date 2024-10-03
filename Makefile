install:
	pip install --upgrade pip && pip install -r Requirements.txt

format:
	black *.py
	
lint:
	ruff check *.py

test:
	python3 -m pytest -vv --nbval -cov=mylib -cov=main test*.py
	
all: install format lint test
