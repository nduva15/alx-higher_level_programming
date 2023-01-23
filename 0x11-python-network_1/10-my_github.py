#!/usr/bin/python3

<<<<<<< HEAD
"""A script that:

- takes your GitHub credentials (username and password)

- uses the GitHub API to display your id

"""

import sys

import requests

from requests.auth import HTTPBasicAuth
=======
import requests

from sys import argv
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625





if __name__ == "__main__":
    
<<<<<<< HEAD
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    
    r = requests.get("https://api.github.com/user", auth=auth)
    
    print(r.json().get("id"))
=======
    url = "https://api.github.com/user"
    
    _auth = (argv[1], argv[2])
    
    req = requests.get(url, auth=_auth).json()
    
    reqId = req.get('id')
    
    print(reqId)
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625
