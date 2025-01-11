# Stage 1: Build stage
FROM python:3.9-slim AS builder

# Set the working directory
WORKDIR /app

# Install build dependencies for psycopg2 and other compiled libraries
RUN apt-get update && apt-get install -y \
  curl \
  gcc \
  libpq-dev \
  build-essential \
  && rm -rf /var/lib/apt/lists/*

# Copy the requirements file (`fareweller` folder) and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --prefix=/install -r /app/requirements.txt

# Stage 2: Final stage with only the necessary components
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install runtime dependencies (including `curl` for health-check of Flask app)
RUN apt-get update && apt-get install -y libpq5 curl \
  && rm -rf /var/lib/apt/lists/*

# Create a non-root user and group, and set permissions
RUN useradd -m -d /home/nonrootuser nonrootuser
USER nonrootuser

# Copy only the installed dependencies from the builder stage, adjust ownership
COPY --from=builder --chown=nonrootuser:nonrootuser /install /usr/local

# Copy the application code and set correct ownership and permissions
COPY --chown=nonrootuser:nonrootuser . /app

# Set environment variables
ENV FLASK_APP=app.py
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

# Expose the port the app runs on
EXPOSE 5003

# Use non-root user to run the application
USER nonrootuser

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5003"]
