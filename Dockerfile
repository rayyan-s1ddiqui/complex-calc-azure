# Use an official Python base image
FROM python:3.11-slim

# Install system dependencies for Tesseract and image processing
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    poppler-utils \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy app code
COPY ./app ./app
COPY ./run.py .

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (FastAPI default is 8000)
EXPOSE 8000

# Run the app with Uvicorn
CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"]
