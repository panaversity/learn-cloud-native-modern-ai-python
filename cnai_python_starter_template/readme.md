## Setup Instructions

## Starter Template

This will be used by students to used to do cloud native projects

## Template Setup Guide

### PreRequisite:
1. Installed Docker
2. Add DevContianer Extension to VS Code
3. Knows the purpose of `docker compose up --build -d` and `docker compose down` commands

## Setup

1. Clone the repp and open folder `cnai_python_starter_template` or it's code in VS code

2. Ensure that in VS code terminal if you type `dir` or `ls` the output is:

```bash
mjs@Muhammads-MacBook-Pro-3 cnai_python_starter_template % ls
Dockerfile      compose.yml     main.py
```

3. Start Template

In Terminal run `docker compose up --build -d`

4. Open the Container in VSCode - now using the DevContainer Remote Explorer open the Container in VS Code

5. Do all your coding - make python files and run them in vs code.

6. After practice close dev container and in terminal run `docker compose down`