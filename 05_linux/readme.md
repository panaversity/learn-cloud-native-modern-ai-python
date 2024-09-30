# What is Linux?

**Linux** is an open-source, Unix-like operating system kernel first released by Linus Torvalds in 1991. It is known for its stability, security, and flexibility, making it a popular choice for servers, desktops, and embedded systems. Linux is used as the core component of many operating systems, known as Linux distributions (distros), which include the kernel along with various applications and utilities. Popular Linux distributions include Ubuntu, Fedora, CentOS, and Debian.

#### Key Features of Linux:
1. **Open Source**: Linux is released under the GNU General Public License (GPL), allowing anyone to use, modify, and distribute the software.
2. **Security**: Linux is known for its robust security features, including user permissions, encryption, and firewall capabilities.
3. **Flexibility**: It can be used on a wide range of devices from smartphones to supercomputers.
4. **Stability and Performance**: Linux systems are known for their uptime and performance, making them ideal for server environments.
5. **Community Support**: A large community of developers and users contribute to the development and support of Linux.

### Linux Market Share in Cloud Computing

Linux dominates the cloud computing market, primarily due to its open-source nature, stability, security, and flexibility. Most cloud service providers, including AWS, Google Cloud, and Microsoft Azure, offer Linux-based virtual machines and services.

#### Market Share Statistics:
1. **AWS (Amazon Web Services)**: Linux instances make up around 92% of AWS's total instances, according to a 2020 report by the Cloud Native Computing Foundation (CNCF).
2. **Google Cloud Platform (GCP)**: Google reports that over 90% of their cloud infrastructure runs on Linux.
3. **Microsoft Azure**: While traditionally associated with Windows, Azure also supports Linux, and Linux-based instances make up around 60% of its workload, as per a report from 2019.

#### General Cloud Market Share:
- **Linux**: According to a report from the Cloud Native Computing Foundation (CNCF), as of 2020, Linux powers around 90% of all cloud infrastructure.
- **Windows**: Windows instances constitute a smaller portion of the cloud market but still hold a significant share, particularly in enterprises using Microsoft-based solutions.

Linux's dominance in cloud computing is driven by its performance, cost-effectiveness, and the extensive range of open-source tools and applications available for deployment and management.

### Sources
- [Linux Foundation](https://www.linuxfoundation.org/)
- [Cloud Native Computing Foundation (CNCF) Report](https://www.cncf.io/)
- [Amazon Web Services (AWS) Documentation](https://aws.amazon.com/)
- [Google Cloud Platform (GCP) Documentation](https://cloud.google.com/)
- [Microsoft Azure Documentation](https://azure.microsoft.com/)

## What is Ubuntu?

**Ubuntu** is a free and open-source Linux distribution based on Debian. Developed and maintained by Canonical Ltd., it is known for its user-friendliness, robust security features, and regular updates. Ubuntu is popular for both desktop and server use and has a large user base and community support. We will use it as our main Operating System.

#### Key Features of Ubuntu:
1. **User-Friendly**: Ubuntu provides a straightforward installation process and a user-friendly interface with its GNOME desktop environment.
2. **Regular Releases**: Ubuntu has a predictable release cycle, with new versions released every six months and long-term support (LTS) versions every two years.
3. **Security**: It includes regular security updates and comprehensive security features, including AppArmor and automated security patches.
4. **Software Availability**: Ubuntu has a vast repository of software and applications, easily installable via its package manager.
5. **Community and Support**: There is extensive documentation and a large community that provides support through forums, mailing lists, and social media.

### Market Share in Cloud Computing

Ubuntu is a dominant player in the cloud computing market. It is widely used by many cloud service providers and has a significant presence in cloud deployments.

#### Market Share Statistics:
1. **AWS (Amazon Web Services)**: Ubuntu is one of the most popular operating systems on AWS. According to Canonical, over half of the instances running on AWS are based on Ubuntu.
2. **Google Cloud Platform (GCP)**: Ubuntu is extensively used on GCP for its compatibility and performance. Google Cloud Marketplace offers numerous Ubuntu-based virtual machine images.
3. **Microsoft Azure**: Ubuntu is the leading Linux distribution on Azure, preferred for various applications including container deployments and artificial intelligence.

### ROS 2 and Ubuntu

**ROS 2 (Robot Operating System 2)** is a set of software libraries and tools for building robot applications. It is the successor to ROS 1 and is designed to be more flexible, scalable, and suitable for industrial applications.

#### Relationship with Ubuntu:
- **Primary Platform**: ROS 2 is primarily developed and tested on Ubuntu. Canonical and Open Robotics work closely to ensure compatibility and optimization of ROS 2 on Ubuntu.
- **Distribution and Support**: Ubuntu provides a seamless environment for installing and running ROS 2, with official packages available through its repositories.

### Sources
- [Ubuntu Official Site](https://ubuntu.com/)
- [Canonical's Reports on Cloud Usage](https://ubuntu.com/blog/cloud-and-server)
- [AWS Marketplace](https://aws.amazon.com/marketplace)
- [Google Cloud Platform Documentation](https://cloud.google.com/)
- [Microsoft Azure Documentation](https://azure.microsoft.com/)
- [ROS 2 Documentation](https://docs.ros.org/en/foxy/index.html)

Ubuntu's user-friendly nature, combined with its strong presence in cloud computing and compatibility with ROS 2, makes it a versatile and powerful choice for a wide range of applications.

## Running Ubuntu on Local Machine

When running Ubuntu on your local machine, you have two options: **Virtual Machines (VMs)** or **Docker containers**. Let's explore the differences:

1. **Virtual Machines (VMs)**:
   - VMs emulate physical computers within a host machine.
   - Each VM has its own guest operating system.
   - VMs are isolated and can run different applications on different OSes.
   - Requires more resources (RAM, disk space).
   - Suitable for running full OS environments.
   - Use a hypervisor (e.g., VMware, VirtualBox) to manage VM instances¹.

2. **Docker Containers**:
   - Containers run on top of the host OS, sharing the same kernel.
   - Lightweight and efficient—no separate guest OS.
   - Ideal for packaging applications and dependencies.
   - Requires less overhead (CPU, memory).
   - Use Docker to manage containers.
   - Great for microservices and isolated app environments¹.

**Recommendation**:
- For running Ubuntu with minimal overhead and efficient resource utilization, **Docker containers** are a popular choice. You can easily pull an Ubuntu image and run it using Docker².
- If you need a full OS environment with separate guest OSes, consider using **Virtual Machines**.

Choose based on your specific use case and resource requirements! 🚀

Sources:
(1) Docker vs Virtual Machine (VM) – Key Differences You Should Know. https://www.freecodecamp.org/news/docker-vs-vm-key-differences-you-should-know/.
(2) Run Ubuntu Linux in Docker with Desktop Environment and VNC. https://bing.com/search?q=run+ubuntu+on+local+machine+virtual+machine+or+docker+containers.
(3) Run Ubuntu Linux in Docker with Desktop Environment and VNC. https://computingforgeeks.com/run-ubuntu-linux-in-docker-with-desktop-environment-and-vnc/.
(4) How to Run Ubuntu as a Docker Container - MUO. https://www.makeuseof.com/run-ubuntu-as-docker-container/.
(5) Getty Images. https://www.gettyimages.com/detail/news-photo/in-this-photo-illustration-the-ubuntu-logo-is-seen-news-photo/1146666406.

## Running Ubuntu Docker Container on My Local Machine 

Certainly! You can run an **Ubuntu Docker container** on your local computer. Here's how:

1. **Get the Ubuntu Docker Image**:
   - If you don't have Docker installed, follow the guide on installing Docker for [Ubuntu](https://www.makeuseof.com/run-ubuntu-as-docker-container/), [macOS](https://www.makeuseof.com/run-ubuntu-as-docker-container/), or [Windows](https://www.makeuseof.com/run-ubuntu-as-docker-container/).
   - Download the latest Ubuntu Docker image using this command:
     ```
     sudo docker pull ubuntu
     ```
   - If you want a specific version (e.g., Ubuntu 20.04), use:
     ```
     sudo docker pull ubuntu:20.04
     ```

2. **Run the Ubuntu Docker Image**:
   - Execute the following command to start an interactive terminal session in the Ubuntu container:
     ```
     sudo docker run -ti --rm ubuntu /bin/bash
     ```
   - This command runs the Ubuntu container, and you'll get a Bash shell prompt.
   - Note that the image doesn't include a GUI or additional tools by default—it's super lightweight at around 78MB.

3. **Explore and Experiment**:
   - You can run Linux commands within the container.
   - For example, check the OS information using:
     ```
     cat /etc/os-release
     ```
   - Remember that Docker images only include essential elements of the OS.

Enjoy experimenting with Ubuntu in your Docker container! 🚀🐳¹⁴

Sources:
(1) How to Run Ubuntu as a Docker Container - MUO. https://www.makeuseof.com/run-ubuntu-as-docker-container/.
(2) Getting started with Docker: Running an Ubuntu Image. https://dev.to/netk/getting-started-with-docker-running-an-ubuntu-image-4lk9.
(3) Run Ubuntu Linux in Docker with Desktop Environment and VNC. https://bing.com/search?q=docker+containers+run+ubuntu+on+local+computer.
(4) Run Ubuntu Linux in Docker with Desktop Environment and VNC. https://computingforgeeks.com/run-ubuntu-linux-in-docker-with-desktop-environment-and-vnc/.
(5) How to connect to a docker container from outside the host (same .... https://stackoverflow.com/questions/33814696/how-to-connect-to-a-docker-container-from-outside-the-host-same-network-windo.