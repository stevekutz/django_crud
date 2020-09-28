#### Environment Setup


1) Create virtual environment using `pipenv`

   - using `--three` lets pipenv know to use Python3

    ~~~ bash
    pipenv --three
    ~~~

2) Activate the virtual environment

    - enter `exit` to leave the virtual environment

    ~~~ bash
    pipenv shell
    ~~~

3) While in the virtual environment, install `django`

    ~~~ bash
    pipenv install django
    ~~~

4) Create the project. Make sure to use the `.` to help with migration to Heroku later. The `.` will create the project folder directly in the root instead of creating its own project folder and then creating a project folder of the the same name within.

    ~~~ bash
    django-admin startproject crud_proj .
    ~~~

5) Create an app called notes

    ~~~ bash
    django-admin startapp notes
    ~~~

6) The project layout shuld resemble the following:

    <img src = "img_doc/project_app_step_1.PNG" width = "25%"/>
