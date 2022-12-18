VENV=.venv
PYTHON=$(VENV)/bin/python3
REQUIREMENTS=requirements.txt

setup: $(VENV)

$(VENV): $(REQUIREMENTS)
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r $(REQUIREMENTS)

