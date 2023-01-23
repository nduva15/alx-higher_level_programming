#!/usr/bin/python3

<<<<<<< HEAD
"""Displays the X-Request-Id header variable of a request to a given URL

"""

import sys

import requests

=======
"""sends a request to the URL and displays the value of the X-Request-Id"""

import requests

from sys import argv
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625




<<<<<<< HEAD
if __name__ == "__main__":
    
    url = sys.argv[1]
    

    
    r = requests.get(url)
    
    print(r.headers.get("X-Request-Id"))
=======

if __name__ == "__main__":
    
    req = requests.get(argv[1])
    
    print(req.headers.get('X-Request-Id'))
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625
