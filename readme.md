# Tortoise schema migration tool

This is a tool made to cover the lack of schema migrations in the wonderful ORM Tortoise.

install requirements, add models as required in the settings, I have already provided a set of sample models.

you can use the tool as follows:

- Install prerequisites: `dbmate` and `schemalax`
- This tool currently only supports MySQL, Postgres support will follow very soon. 

1. You should initialize the database first:

`python manage.py initdb`

2. Make you first migration:

`python manage.py makemigrations -n add_users_table`

3. Migrate your schema:

`python manage.py migrate`

4. If you make a mistake or with to rollback your last migration:

`python manage.py rollback`


