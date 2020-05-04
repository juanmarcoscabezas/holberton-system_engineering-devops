#!/usr/bin/python3

"""
This script uses https://jsonplaceholder.typicode.com/
for a given employee ID, returns information about his/her
TODO list progress.
"""

import requests
import sys

if len(sys.argv) > 0:
    userId = sys.argv[1]
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(userId))
    user = r.json()
    r = requests.get('https://jsonplaceholder.typicode.com/todos/?userId={}'.format(userId))
    todos = r.json()
    doneTasks = 0
    todosString = ''
    for todo in todos:
        if todo.get('completed') == True:
            doneTasks +=1
        todosString += '\t {}\n'.format(todo.get('title'))
    print('Employee {} is done with tasks({:d}/{:d}):'.format(user.get('name'), doneTasks, len(todos)))
    print(todosString, end='')
