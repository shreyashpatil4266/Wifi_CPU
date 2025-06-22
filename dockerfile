# Use official Python image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install Python packages
RUN pip install --no-cache-dir flask speedtest-cli psutil

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
