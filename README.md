# Todolist

Todolist application on Django==2.1.2 with simple registration, authorization and roles(admin/user). 
![alt text](https://image.ibb.co/fD2wxf/2018-11-06-04-20-45.png)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development. 

### Prerequisites
We need Python3, PostgreSQL9.6

### Installing

```
git clone https://github.com/Russel777/todolist.git
pip install virtualenv
virtualenv -p python3.6 venv-todolist
source venv/bin/activate
pip install -r requirements.txt
python manage.py loaddata todolist_app/fixtures/initial_data.json
```
Then in file /todolist/settings/local.py you should enter you log/pass for Database PostgreSql

## Run in local mode

```
python manage.py runserver
```

## Usage

First of all you should sign up, then on main page you can see all list of Todos or, for example add new Todo.

### Add Todo
1. On main page press on "Add new todo".
1. Fill all fields.
1. Press Save.

### Sort List
On main page you can sort list of Todos, just press on one of six sort buttons.

### Edit Todo
1. On main page press on Todo, which you want to edit.
1. Edit elements.
1. Press Save.

### Delete Todo
On main page press Delete Button on row of Todo which you want to delete.


## Built With

* [Django](https://www.djangoproject.com/) - The Python web framework 
* [PostgreSQL](https://www.postgresql.org/) - Database

## License

This project is licensed under the MIT License.

