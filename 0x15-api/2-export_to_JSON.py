#!/usr/bin/python3

"""
This script uses https://jsonplaceholder.typicode.com/
for a given employee ID, returns information about his/her
TODO list progress.
"""

import requests
import sys
import json

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
            user_dict = dict()
            new_todo = list()
            for todo in todos:
                new_todo.append({
                                 'task': todo.get('title'),
                                 'completed': todo.get('completed'),
                                 'username': user.get('username')
                               })
            user_dict[userId] = new_todo
            with open('{}.json'.format(userId), 'w') as jsonfile:
                jsonfile.write(json.dumps(user_dict))
