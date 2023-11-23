PY ?= python
POETRY ?= poetry
PIP ?= pip

build-CommonLayer:
	mkdir -p "$(ARTIFACTS_DIR)/python"
	$(POETRY) export --only=common --format=requirements.txt > requirements.txt
	$(PY) -m $(PIP) install -r requirements.txt -t "$(ARTIFACTS_DIR)/python" \
		--implementation cp --platform manylinux2014_x86_64 --only-binary=:all: --


build-DataManipLayer:
	mkdir -p "$(ARTIFACTS_DIR)/python"
	$(POETRY) export --only=datamanip --format=requirements.txt > requirements.txt
	$(PY) -m $(PIP) install -r requirements.txt -t "$(ARTIFACTS_DIR)/python" \
		--implementation cp --platform manylinux2014_x86_64 --only-binary=:all: --
