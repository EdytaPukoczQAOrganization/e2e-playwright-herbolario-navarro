# Playwright E2E Herbolario Navarro

This project performs E2E tests on the [Herbolario Navarro](https://www.herbolarionavarro.es/) website, generating a report of results. Tests are executed on **Chrome** (desktop) and on **iPhone 12** (mobile, emulated).

## Technologies

- ![Python](https://img.shields.io/badge/Python-3.12%2B-blue)  
- ![Playwright](https://img.shields.io/badge/Playwright-v1.48-green)

## View Results

You can view the test status using the following **GitHub Actions** badge:

![Test Workflow](https://github.com/EdytaPukoczQAOrganization/e2e-playwright-herbolario-navarro/actions/workflows/playwright_tests.yml/badge.svg)

## Requirements

### Python Installation

1. Download and install Python from its [official website](https://www.python.org/downloads/). Make sure to select the correct version for your operating system (Python 3.9 or higher).
2. Ensure that Python is added to your `PATH` during installation.

### Install Dependencies

Once Python is installed, clone this repository and navigate to the project folder. Then, install the necessary dependencies by running the following command in the terminal:

pip install -r requirements.txt
playwright install


### Run tests in local
To run the tests locally in visible mode, use the following command in the terminal:
pytest --headed
