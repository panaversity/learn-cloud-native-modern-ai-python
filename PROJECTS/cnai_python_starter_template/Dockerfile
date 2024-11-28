# Use an official Python runtime as a parent image
FROM python:3.12

LABEL maintainer="panaversity"
# Set the working directory in the container
WORKDIR /code
# copy the current directory content into the working directory of the container 
COPY . /code/
# Install system dependencies required for potential Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Run the app. CMD can be overridden when starting the container
CMD ["sleep", "infinity"]
