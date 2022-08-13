# Sample Test Login - Hudl Tech Screening

This repository contains a sample coding challenge containing a small test framework that tests a login page

# Requirements

* Python 3.7.X
* pip and setuptools
* venv

# Installation

1. Download or clone the repository 
2. Open a terminal
3. Go to the project root directory "/hudl_technical_challenge_login/".
4. Create a virtual environment: `py -m venv venv`
5. Activate the virtual environment executing the following script: `.\venv\Scripts\activate`
6. Execute the following command to download the necessary libraries:  `pip install -r requirements.txt`
7. add a file titled: credentials.py under the data folder, the format of this file should be as followed: 
   class LoginCredentials:
      email = "email@email.com"
      password = "password"


# Test Execution

1. Open a terminal
2. From the project root directory run: `pytest -v --html=results/report.html`

# Configuration

Default test execution is in Chrome. Preferences can be changed in "/data/config.yaml" file

# Results

To check the report, open the '/results/report.html' file once the execution has finished.

   
