### A simple app to understand the working of GraphQL. It shows the summary of the user's Github profile. 

![image](https://raw.githubusercontent.com/techytushar/django-graphql-app/master/img.png)

## Usage:

1. Create a Python virtual environment in the root using `python3 -m virtualenv .` and activate it `source bin/activate`
2. Run `pip install -r requirements.txt`
3. In the `app/views.py` replace the `Github Token` with your Github Token
4. Run from `src` folder `python manage.py makemigrations` and `python manage.py migrate`
5. Run `python manage.py runserver` and use the app at `127.0.0.1:8000`

Working demo [GithubQL](https://githubql.herokuapp.com/)

Feel free to report any bugs and enhancements.