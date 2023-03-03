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
- IMPORTANT: Run this command line for setting the JSON file to be used as environment configuration file: _export TARGET_ENV=dev.json_
- Run:

  +) _pipenv run python -m pytest_ to run all tests
  
  +) _pipenv run python -m pytest -k {keyword}_ with keyword is defined in pytest.ini
  
  +) _pipenv run python -m pytest -n {number}_ with number is number of threads for parallel execution. Please don't set something suitable with your machine.
  
  +) _pipenv run python -m pytest --html=report.html_ to generate report to current directory.
  
Screenshots: are found on screenshots folder.

III. Future improvements/optimization:
- Support for running on Selenium Grid
- Support for file creation with specific size
- Better logging and exception handling.
  
