#!/usr/bin/python3

"""
This script uses https://jsonplaceholder.typicode.com/
for a given employee ID, returns information about his/her
TODO list progress.
"""
import json
import requests
import sys

if __name__ == '__main__':
    usr_url = 'https://jsonplaceholder.typicode.com/users'
    r = requests.get(usr_url)
    users = r.json()

    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    r = requests.get(todos_url)
    todos = r.json()

    if users is None or todos is None:
        exit()
    new_users = {}
    for user in users:
        user_id = user.get('id')
        user_todo = []
        for todo in todos:
            if todo.get('userId') == user_id:
                aux_dict = {}
                aux_dict['completed'] = todo.get('completed')
                aux_dict['task'] = todo.get('title')
                aux_dict['username'] = user.get('username')
                user_todo.append(aux_dict)
        new_users[user_id] = user_todo
    with open('todo_all_employees.json', 'w') as jsonfile:
        jsonfile.write(json.dumps(new_users))
