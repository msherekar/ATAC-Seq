install:
	pip install -r requirements.txt

run:
	python src/main.py

test:
	pytest tests/

docker-build:
	docker build -t atacseq-pipeline .

docker-run:
	docker run -p 8000:8000 atacseq-pipeline

# make install      # Install dependencies
# make run          # Run API
# make test         # Run all tests
# make docker-build # Build Docker image
# make docker-run   # Run container
