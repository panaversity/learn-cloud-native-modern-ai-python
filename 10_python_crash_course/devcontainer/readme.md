**DevContainer** (short for Development Container) is a feature provided by Visual Studio Code (VSCode) that allows you to define a containerized environment for your development workspace. This ensures consistency across different development environments and makes it easy to set up and share development configurations.

### Step-by-Step Guide

Here’s how you can set up a DevContainer for a simple Python console application.


1. **Install VSCode and Docker:**
   Ensure you have VSCode and Docker installed on your local machine.

2. **Install the Dev Containers Extension:**
   Install the Dev Containers extension in VSCode.

3. **Create a DevContainer Configuration:**
   Add the necessary configuration files to set up your development environment.

4. **Open the Project in a DevContainer:**
   Use VSCode to open the project in the DevContainer.

### Detailed Steps

1. **Install VSCode and Docker:**
   - Download and install [Visual Studio Code](https://code.visualstudio.com/).
   - Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

2. **Install the Dev Containers Extension:**
   - Open VSCode.
   - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window.
   - Search for "Dev Containers" and install the **Dev Containers** extension by Microsoft.

3. **Create a DevContainer Configuration:**
   - In your project directory, create a `.devcontainer` folder.
   - Inside the `.devcontainer` folder, create a `devcontainer.json` file and a `Dockerfile`.

   Here’s an example structure and content:

   ```
   my_project/
   ├── .devcontainer/
   │   ├── devcontainer.json
   │   └── Dockerfile
   ├── pyproject.toml
   └── main.py
   ```

   **devcontainer.json:**
   ```json
   {
     "name": "Python DevContainer",
     "build": {
       "dockerfile": "Dockerfile"
     },
     "settings": {
       "python.pythonPath": "/usr/local/bin/python"
     },
     "extensions": [
       "ms-python.python",
       "ms-python.vscode-pylance"
     ],
     "postCreateCommand": "poetry install",
     "remoteUser": "vscode"
   }
   ```

   **Dockerfile:**
   ```Dockerfile
   # Use an official Python runtime as a parent image
   FROM python:3.10-slim

   # Set the working directory
   WORKDIR /workspace

   # Install curl and other dependencies
   RUN apt-get update && apt-get install -y curl

   # Install Poetry
   RUN curl -sSL https://install.python-poetry.org | python3 -
   ENV PATH="/root/.local/bin:$PATH"

   # Install additional tools (optional)
   RUN apt-get install -y git

   # Copy the pyproject.toml and poetry.lock files
   COPY pyproject.toml /workspace/

   # Install the dependencies
   RUN poetry install --no-root

   # Set user
   ARG USERNAME=vscode
   RUN useradd -ms /bin/bash $USERNAME
   USER $USERNAME
   ```

4. **Open the Project in a DevContainer:**
   - Open VSCode.
   - Navigate to your project directory.
   - Click on the green `><` icon in the bottom-left corner of the VSCode window.
   - Select `Remote-Containers: Open Folder in Container...`.
   - Choose your project folder.

VSCode will build the container using the `Dockerfile` specified in the `.devcontainer` folder and set up the development environment according to the `devcontainer.json` configuration. This includes installing the specified VSCode extensions and running the `postCreateCommand` to install dependencies.

### Example Project Structure and Files

**Project Directory Structure:**
```
my_project/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── pyproject.toml
└── main.py
```

**pyproject.toml:**
```toml
[tool.poetry]
name = "my_project"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.10"
requests = "^2.25.1"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

**main.py:**
```python
import requests

def main():
    response = requests.get('https://api.github.com')
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    main()
```

By following these steps, you can set up a consistent development environment using DevContainers for a simple Python console application. This approach ensures that your development setup is reproducible and isolated from your local machine’s configuration.