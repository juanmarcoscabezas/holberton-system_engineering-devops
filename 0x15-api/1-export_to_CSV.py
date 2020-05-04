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
            with open('{}.csv'.format(userId), 'w') as csvfile:
                for todo in todos:
                    line = '"{}","{}","{}","{}"\n'.format(
                                    userId,
                                    user.get('username'),
                                    todo.get('completed'),
                                    todo.get('title'))
                    csvfile.write(line)
