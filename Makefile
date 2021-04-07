.PHONY: lint
lint:
	black task1 task2
	isort task1 task2
	flake8 task1 task2
