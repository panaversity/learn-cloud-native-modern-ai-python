# Dependency Management using Poetry

**Poetry** is a dependency management and packaging tool for Python. It allows you to manage your Python project's dependencies, publish packages, and create reproducible environments. Poetry simplifies dependency management by using a `pyproject.toml` file where all project configurations are declared. 

Here’s how to use Poetry in a containerized Python application:

### Step-by-Step Guide

If you want to use Poetry only within the containerized application and not on your local machine, you can follow these steps:

### Step-by-Step Guide

1. **Create a `pyproject.toml` File:**
   Create a `pyproject.toml` file in your project directory to define the dependencies.

2. **Create a `Dockerfile`:**
   Create a `Dockerfile` that includes the installation of Poetry and sets up your Python application.

3. **Build and Run the Docker Container:**
   Build the Docker image and run the container.

### Detailed Steps

1. **Create a `pyproject.toml` File:**
   Define your project's dependencies and settings in a `pyproject.toml` file. Here’s an example:
   ```toml
   [tool.poetry]
   name = "my_project"
   version = "0.1.0"
   description = ""
   authors = ["Your Name <you@example.com>"]

   [tool.poetry.dependencies]
   python = "^3.10"
   requests = "^2.25.1"
   flask = "^2.0.2"

   [build-system]
   requires = ["poetry-core>=1.0.0"]
   build-backend = "poetry.core.masonry.api"
   ```

2. **Create a `Dockerfile`:**
   Create a `Dockerfile` that installs Poetry within the container and sets up your application.
   ```Dockerfile
   # Use an official Python runtime as a parent image
   FROM python:3.10-slim

   # Set the working directory
   WORKDIR /app

   # Install curl and other dependencies
   RUN apt-get update && apt-get install -y curl

   # Install Poetry
   RUN curl -sSL https://install.python-poetry.org | python3 -
   ENV PATH="/root/.local/bin:$PATH"

   # Copy the pyproject.toml and poetry.lock files
   COPY pyproject.toml /app/

   # Install the dependencies
   RUN poetry install --no-root

   # Copy the rest of the application code
   COPY . /app

   # Command to run your application
   CMD ["poetry", "run", "python", "your_app.py"]
   ```

3. **Build and Run the Docker Container:**
   - Build the Docker image:
     ```bash
     docker build -t my_poetry_app .
     ```
   - Run the container:
     ```bash
     docker run -d -p 8000:8000 my_poetry_app
     ```

### Example Project Structure

Ensure your project directory has the following structure:

```
my_project/
│
├── pyproject.toml
├── Dockerfile
└── your_app.py
```

### Explanation

1. **Creating `pyproject.toml`:**
   This file defines your project's dependencies and settings for Poetry.

2. **Dockerfile:**
   - **Base Image:** Use a lightweight Python base image (`python:3.10-slim`).
   - **Working Directory:** Set `/app` as the working directory inside the container.
   - **Install Poetry:** Use `curl` to install Poetry inside the container.
   - **Environment Path:** Add Poetry to the PATH.
   - **Copy Dependency Files:** Copy `pyproject.toml` to the container.
   - **Install Dependencies:** Run `poetry install` to install the dependencies defined in `pyproject.toml`.
   - **Copy Application Code:** Copy the rest of the application code to the container.
   - **Run Command:** Use Poetry to run your application.

3. **Build and Run:**
   - **Build the Image:** Use `docker build` to create a Docker image named `my_poetry_app`.
   - **Run the Container:** Use `docker run` to start the container, mapping port 8000 of the container to port 8000 on your host machine.

By following these steps, you ensure that Poetry is used only within the container, keeping your local machine clean and dependency management contained within the Docker environment.