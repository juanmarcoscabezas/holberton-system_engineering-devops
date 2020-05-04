#!/usr/bin/python3

"""
This script uses https://jsonplaceholder.typicode.com/
for a given employee ID, returns information about his/her
TODO list progress.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        userId = sys.argv[1]
        usr_url = 'https://jsonplaceholder.typicode.com/users/{}'
        r = requests.get(usr_url
                         .format(userId))
        user = r.json()
        if user:
            todos_url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'
            r = requests.get(todos_url
                             .format(userId))
            todos = r.json()
            todos_arraystr = '{'
            todos_arraystr += '"{}": ['.format(userId)
            for i, todo in enumerate(todos):
                todos_arraystr += '{'
                todos_arraystr += '"task": "{}", '\
                    .format(todo.get('title'))
                todos_arraystr += '"completed": {}, '\
                    .format(str(todo.get('completed')).lower())
                todos_arraystr += '"username": "{}"'\
                    .format(user.get('username'))
                todos_arraystr += '}'
                if i < len(todos) - 1:
                    todos_arraystr += ', '
            todos_arraystr += "]}"
            with open('{}.json'.format(userId), 'w') as jsonfile:
                jsonfile.write(todos_arraystr)
