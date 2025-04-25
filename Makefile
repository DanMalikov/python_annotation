.PHONY: typing

typing:
	docker build -t cheker .
	docker run -v $(PWD):/app -it --rm cheker sh -c "poetry run mypy homework/"
