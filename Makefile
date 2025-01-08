.PHONY: format typecheck lint clean up_bot

format:
	poetry run black .

typecheck:
	poetry run mypy .

lint:
	poetry run ruff check

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

up_bot:
	poetry run python vkbot/main.py

up_rag:
	python rag/main.py
