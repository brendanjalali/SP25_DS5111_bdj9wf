default:
	@cat Makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt
	bash -c "source env/bin/activate && pip install -r requirements.txt"

lint: env
	. env/bin/activate; pylint bin/ || true

test: lint
	. env/bin/activate;  pytest -vv tests

ygainers.html:
	. env/bin/activate; sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=>'

ygainers.csv: ygainers.html
	. env/bin/activate; python -c "import pandas as pd; raw = pd.read_html('data/ygainers.html'); raw[0].to_csv('data/ygainers.csv')"

wsjgainers.html:
	. env/bin/activate; sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 https://www.wsj.com/market-data/stocks/us/movers > data/wsjgainers.html

wsjgainers.csv: wsjgainers.html
	. env/bin/activate; python -c "import pandas as pd; raw = pd.read_html('data/wsjgainers.html'); raw[0].to_csv('data/wsjgainers.csv')"

gainers:
	@if [ -z "$(SRC)" ]; then \
		echo "Error: Must input SRC Parameter"; \
		echo "Usage: make gainers SRC=yahoo"; \
		echo "   or: make gainers SRC=wsj"; \
		exit 1; \
	fi

	@echo "Checking source and generating HTML..."
	@if [ "$(SRC)" = "yahoo" ]; then \
		$(MAKE) ygainers.html; \
	elif [ "$(SRC)" = "wsj" ]; then \
		$(MAKE) wsjgainers.html; \
	else \
		echo "Error: Unknown SRC '$(SRC)'. Use 'yahoo' or 'wsj'."; \
		exit 1; \
	fi

	@echo "Processing gainers from $(SRC)..."
	@. env/bin/activate
	@python3 get_gainer.py $(SRC)
