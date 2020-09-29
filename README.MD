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

6) The project layout should resemble the following:

    <img src = "img_doc/project_app_step_1.PNG" width = "25%"/>

7) Change directories to the root folder and launch the server
    - `Control + C stops the server`

    ~~~ bash
    ./manage.py runserver
    ~~~

8) At this point, no migrations have been run and Django will present warnings when running the server. To view the migrations that need to be run:

    ~~~ bash
    ./manage.py showmigrations
    ~~~

    - the following should show up:

    ~~~ bash 
    admin
    [ ] 0001_initial
    [ ] 0002_logentry_remove_auto_add
    [ ] 0003_logentry_add_action_flag_choices
    auth
    [ ] 0001_initial
    [ ] 0002_alter_permission_name_max_length
    [ ] 0003_alter_user_email_max_length
    [ ] 0004_alter_user_username_opts
    [ ] 0005_alter_user_last_login_null
    [ ] 0006_require_contenttypes_0002
    [ ] 0007_alter_validators_add_error_messages
    [ ] 0008_alter_user_username_max_length
    [ ] 0009_alter_user_last_name_max_length
    [ ] 0010_alter_group_name_max_length
    [ ] 0011_update_proxy_permissions
    [ ] 0012_alter_user_first_name_max_length
    contenttypes
    [ ] 0001_initial
    [ ] 0002_remove_content_type_name
    sessions
    [ ] 0001_initial
    ~~~

    - To see what individual SQL queries will be run, use the following syntax:

    ~~~ bash
    ./manage.py sqlmigrate [package_name] [migration_id]
    ~~~

    - for example(a long string of SQL commands will be displayed):
    ~~~ bash
    ./manage.py sqlmigrate auth 0003
    ~~~


9) Run the first migration

    ~~~ bash
    ./manage.py migrate
    ~~~

    - running `./manage.py showmigrations` will show everything that was run along with a check beside it

    ~~~ bash
    admin
    [X] 0001_initial
    [X] 0002_logentry_remove_auto_add
    [X] 0003_logentry_add_action_flag_choices
    auth
    [X] 0001_initial
    [X] 0002_alter_permission_name_max_length
    [X] 0003_alter_user_email_max_length
    [X] 0004_alter_user_username_opts
    [X] 0005_alter_user_last_login_null
    [X] 0006_require_contenttypes_0002
    [X] 0007_alter_validators_add_error_messages
    [X] 0008_alter_user_username_max_length
    [X] 0009_alter_user_last_name_max_length
    [X] 0010_alter_group_name_max_length
    [X] 0011_update_proxy_permissions
    [X] 0012_alter_user_first_name_max_length
    contenttypes
    [X] 0001_initial
    [X] 0002_remove_content_type_name
    sessions
    [X] 0001_initial
    ~~~