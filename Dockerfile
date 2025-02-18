# Use lightweight Python base image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy only dependencies first to cache them (Optimizes rebuilds)
COPY pyproject.toml requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code after dependencies are installed
COPY src/ ./src/

# Expose API port
EXPOSE 8000

# Run API
CMD ["python", "src/api.py"]
