venv: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur requirements.txt

test: venv
	./venv/bin/pytest
