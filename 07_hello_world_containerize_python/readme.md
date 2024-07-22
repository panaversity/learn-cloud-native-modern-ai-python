# Containerize Hello World Python Apps with Docker

Creating a containerized "Hello World" Python application involves writing a simple Python script and a Dockerfile to containerize the application. Here’s how you can do it:

### Step 1: Create a app directory and Write the Python Script

Create a file named `app.py` with the following content:

```python
# app.py

print("Hello, World!")
```

### Step 2: Create a Dockerfile

Create a file named `Dockerfile` in the same directory as your `app.py` with the following content:

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run app.py when the container launches
CMD ["python", "app.py"]
```

### Step 3: Build the Docker Image

Open a terminal, navigate to the directory containing your `app.py` and `Dockerfile`, and run the following command to build the Docker image:

```sh
docker build -t hello-world-app .
```

This command tells Docker to build an image with the tag `hello-world-app` using the current directory (denoted by `.`) as the context.

### Step 4: Run the Docker Container

After building the Docker image, you can run it with the following command:

```sh
docker run hello-world-app
```

You should see the output `Hello, World!` in your terminal.

### Step 5: Verify the Docker Image and Container

You can verify that the Docker image was created successfully and list all Docker images with the following command:

```sh
docker images
```

To see the running container, use:

```sh
docker ps
```

To see all containers, including stopped ones, use:

```sh
docker ps -a
```

### Full Example Directory Structure

Your project directory should look like this:

```
hello-world-app/
├── app.py
└── Dockerfile
```

### Additional Notes

- **Python Base Image**: We are using `python:3.9-slim`, a lightweight Python image. You can choose different versions or variants based on your needs.
- **Work Directory**: Setting the work directory with `WORKDIR /app` ensures that all subsequent commands are run in this directory inside the container.
- **Copy Command**: `COPY . /app` copies the contents of the current directory on your host into the `/app` directory in the container.
- **Command**: `CMD ["python", "app.py"]` specifies the command to run the Python script when the container starts.

This simple example demonstrates the basic steps to create a containerized Python application. You can expand on this by adding more dependencies, handling environment variables, or integrating with other services.