# Hello World Container Operations

1. Overview
[Read Chapters 1 and 7 of our Text Book: Docker Deep Dive by Nigel Poulton 2024 Edition](https://www.amazon.com/Docker-Deep-Dive-Nigel-Poulton/dp/1916585256/ref=sr_1_1_sspa)

[Watch: Docker Crash Course for Absolute Beginners](https://www.youtube.com/watch?v=pg19Z8LL06w)

2. Installing Docker Desktop (Chapter 3)

https://docs.docker.com/get-docker/

    docker version

Test Docker Installation:

    docker run hello-world

**For Windows:**

- 64-bit version of Windows 10/11
- Hardware virtualization support must be enabled in your system’s BIOS
- WSL 2

[How to Install WSL2 with Ubuntu](https://youtu.be/J2PQuVAI99c?si=X-lg60sGq6PkkD5P)

[Docker for Windows Installation and Troubleshooting for Beginners](https://youtu.be/R4uy6Oqiy5I?si=DglDYuvf-zvFY9bS)


**For Mac**, if docker command not running:

https://stackoverflow.com/questions/64009138/docker-command-not-found-when-running-on-mac

https://www.insightsjava.com/2022/01/how-to-create-bash-profile-on-mac.html

3. Play with Docker

Play with Docker (PWD) is a fully functional internet-based Docker playground that lasts for 4 hours. You can add multiple nodes and even cluster them in a swarm.

https://labs.play-with-docker.com/

4. The Big Picture (Chapter 4)

### Linux Ubuntu

* Pull Ubuntu Image:

    docker pull ubuntu

Note:

[Docker Hub Image](https://hub.docker.com/_/ubuntu)

* List the Images:

    docker images

* Launch the Container:

    docker run -it ubuntu /bin/bash

Note: You’ll see that the shell prompt has changed. This is because the -it flags switch your shell into the terminal
of the container — your shell is now inside of the new container!


* List all running processes:

    ps -elf

* Exit the Container without terminating it:

    Press Ctrl-PQ to exit the container without terminating it.

* List All Running Containers:

    docker ps

* Attaching to running Container:

    docker exec -it container_name bash

* Stop the Container:

    docker stop container_name

* List the Containers, even those that are in stopped state:

    docker ps -a

* Kill the Container:

    docker rm container_name


## Attach VSCode to a Running Container

https://code.visualstudio.com/docs/devcontainers/attach-container

https://www.youtube.com/watch?v=OTrJrDZEFYs


## Learn the Docker Commands

[Docker Cheat Sheet: All the Most Essential Commands in One Place + Downloadable PDF](https://www.hostinger.com/tutorials/docker-cheat-sheet)

## Learn the Linux Commands

[60 Essential Linux Commands + Free Cheat Sheet](https://www.hostinger.com/tutorials/linux-commands)
