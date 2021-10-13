# Readme

This is a basic workup of a web app with a Python (Django) backend and a JS/TS (React) frontend.

If you want a detailed tutorial on how to build this that I would have been _*wayyy*_ too lazy to write, see the excellent 4-part tutorial series written by Mangabo Kolawole on [dev.to](https://github.com/koladev32/django-auth-react-tutorial). It takes you from how to initialize your project all the way through deploying it on AWS. This isn't lifted from there _en toto_, but it's _heavily_ based on that tutorial series.

Otherwise, follow the steps below to get started.

0. Ensure you are in the project root directory

1. Create a virtual environment

```shell
virtualenv --python=/usr/bin/python3.8 venv
```

2. Install requirements

```shell
pip install -r requirements.txt
```

3. Migrate and Start the server

```shell
python manage.py migrate
python manage.py runserver
```

4. CD into the frontend directory
5. Install the yarn dependencies
```shell
yarn install
```

6. Check out pages you created