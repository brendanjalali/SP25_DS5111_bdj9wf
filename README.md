[![Feature Validation](https://github.com/brendanjalali/SP25_DS5111_bdj9wf/actions/workflows/validations.yml/badge.svg)](https://github.com/brendanjalali/SP25_DS5111_bdj9wf/actions/workflows/validations.yml)

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

## 5. Normalizing Gainers

### 5.1 Activate Virtual Environment and Run Job

The following are instructions for creating the normalized version of CSV's

```sh
. env/bin/activate
python bin/normalize_csv.py <path to raw gainers csv>
```


---

## 6.

To ensure that the code functions as expected, you can run the test suite using `make test`. This command runs `pylint` for code quality checks and executes unit tests to validate the CSV normalization process.

### 6.1 Running the Tests

From the root directory of the project:

```sh

. env/bin/activate
make test
````


---

## 7. Structure

The following is the structure of the Repository:

```
.
├── Makefile
├── README.md
├── bin
│   ├── __pycache__
│   │   └── normalize_csv.cpython-312.pyc
│   └── normalize_csv.py
├── init.sh
├── pylintrc
├── requirements.txt
├── sample_data
│   ├── wjsgainers.csv
│   ├── wjsgainers.html
│   ├── wjsgainers_norm.csv
│   ├── ygainers.csv
│   ├── ygainers.html
│   └── ygainers_norm.csv
├── scripts
│   ├── google-chrome-stable_current_amd64.deb
│   └── install_chrome_headless.sh
└── tests
    ├── __pycache__
    │   └── test_normalize_csv.cpython-312-pytest-8.3.4.pyc
    └── test_normalize_csv.py
```
