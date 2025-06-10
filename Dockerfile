# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . .

# Expose port 8080
EXPOSE 8080

# Run the app (adjust for your app entrypoint)
CMD ["python", "app.py"]
