# uploadfile-pytest-bdd

This is the document aims to explain how the framework is built and how to execute it.

I. Pre-requisites:
- Have Python installed with version >= 3.9
- Have pip installed with version >= 23.0.1
- Have pipenv installed with latest version. At this time the document is drafted, version is 2023.2.18.
  +) If you don't have it, then please install it with pip3 install pipenv.


II. Setup:
- Clone this repo
- Go to the project with cd uploadfile-pytest-bdd
- Run pipenv install to install all the dependencies.
- Put a file with big size (>200 Mb) into data/ directory and uncomment the section related to big file size upload in feature file.
- Update the file path as well.
- IMPORTANT: Run this command line: export TARGET_ENV=dev.json to set the JSON file to be used as environment configuration file.
- Run:

  +) pipenv run python -m pytest to run all tests
  
  +) pipenv run python -m pytest -k {keyword} with keyword is defined in pytest.ini
  
  +) pipenv run python -m pytest -n {number} with number is number of threads for parallel execution. Please don't set something suitable with your machine.
  
  +) pipenv run python -m pytest --html=report.html to generate report to current directory.
  
Screenshots: 
[(https://we.tl/t-P6FiSRqIXR)]

III. Future improvements/optimization:
- Support for running on Selenium Grid
- Support for file creation with specific size
- Better logging and exception handling.
  
