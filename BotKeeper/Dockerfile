FROM python:3.9-slim

# Install required packages
RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Set environment variable to use X11
ENV DISPLAY=host.docker.internal:0

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data
RUN python -m nltk.downloader punkt

# Run the application
CMD ["python", "app.py"]