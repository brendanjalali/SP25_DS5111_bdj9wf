# Project Setup Guide

## 1. Prerequisites

Before setting up the VM, ensure you have Git configured and an SSH key set up for authentication.

### 1.1 Set Up Git Credentials and SSH Key

Follow these steps to configure Git and create an SSH key:

```sh
./
```

### 1.2 Clone the Repository

Once your SSH key is added to GitHub, clone the project repository:

```sh
git clone git@github.com:yourusername/yourrepo.git
cd yourrepo
```

---

## 2. Setting Up the VM

To ensure that we can quickly recreate our development environment in case of a cloud instance crash, follow these steps to set up a new VM.

### 2.1 Run the Initialization Script

The `init.sh` script automates the setup process:

```sh
./init.sh
```

This script will:
- Update package lists.
- Install essential packages like `make`, `python3.12-venv`, and `tree`.
- Install Google Chrome for headless browsing.

At this point, your VM is ready for project-specific setup.

---

## 3. Creating Necessary Setup Files

Now that your VM is ready, ensure the necessary setup files are present.

### 3.1 `install_chrome_headless.sh`

This script installs Google Chrome for headless browsing. If it's not already in your repository, create it:

```sh
nano install_chrome_headless.sh
chmod +x install_chrome_headless.sh
```

### 3.2 `Makefile`

Your repository should contain a `Makefile`. If missing, create one:

```sh
nano Makefile
```

### 3.3 `requirements.txt`

Ensure your repository has a `requirements.txt` file. If missing, create it:

```sh
nano requirements.txt
```

---

## 4. Running and Organizing the Project

Once all necessary files are created, follow these steps to set up and run your project.

### 4.1 Install Dependencies

```sh
make update
```

### 4.2 Activate Virtual Environment and Run Job

```sh
source env/bin/activate
make ygainers.csv
deactivate
```

### 4.3 Organizing Output Files

Create a directory for sample data and move the generated files:

```sh
cd ..
mkdir sample_data
cd scripts
mv ygainers.html ../sample_data/
mv ygainers.csv ../sample_data/
```
