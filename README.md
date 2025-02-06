# Project Setup Guide

## 1. Prerequisites

Before setting up the VM, ensure you have Git configured and an SSH key set up for authentication.

The following should be created one directory below the repository
```sh
chmod +x global_creds.sh
./global_creds.sh
```
This should contain:
```sh
#!/bin/bash

USER=youremail@example.com
NAME=yourusername

git config --global --list

git config --global user.email "$USER"
git config --global user.name "$NAME"

git config --global --list
```

---

## 2. Setting Up the VM

To make sure that we can quickly recreate our development environment in case of a cloud instance crash, follow these steps to set up a new VM.

### 2.1 Run the Initialization Script

The `init.sh` script automates the setup process:

```sh
./init.sh
```
---

## 3. Setup Files

Now that your VM is ready, ensure the necessary setup files are present.

### 3.1 Check all files are present

```sh
cd scripts
ls -la
```

You should see 3 files:
'install_chrome_headless.sh'
'Makefile'
'requirements.txt'

### 3.2 Make .sh to runnable

In the scripts directory make sure that 'install_chrome_headless.sh' is runnable by running:

```sh
chmod +x install_chrome_headless.sh
./install_chrome_headless.sh
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

---

## 5. Structure

The following is the structure of the Repository:

```
SP25_DS5111_bdj9wf
├── README.md
├── init.sh
├── sample_data
│   ├── ygainers.csv
│   └── ygainers.html
└── scripts
    ├── Makefile
    ├── google-chrome-stable_current_amd64.deb
    ├── install_chrome_headless.sh
    └── requirements.txt
```
