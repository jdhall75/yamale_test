# yamale_test
testing out Yamale for a project

This is an example of using the pytest framework to validate YAML files with the YAMALE library.

## Setup
This project uses pipenv for library management and installation.  The Pipfiles are included so a simple install and activating the shell will get you started.
```
$ pipenv install 
$ pipenv shell
# Youre ready to go
```

## Intro
The `file_generator.py` script will just create some example YAML documents to run tests against.  Some sample files are included already.

In the `out/group_vars` directory you will find the the schema file `ZZZZ-schema.yml`.  The idea was to match the length of the file names to validate with the same numbers of Z's.  In a directory listing, `ls -l`, this would put the schema just below the YAML files it is meant to validate.

## Running
From the root of the project folder
```
$ py.test
```

The pytest library will automatically look for a `test` directory and include those files in the testing run.
Some naming conventions need to be followed. 


