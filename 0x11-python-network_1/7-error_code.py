#!/usr/bin/python3

<<<<<<< HEAD
"""A script that

- takes in a URL

- sends a request to the URL

- displays the body of the response.

"""

import sys

import requests

=======
"""s takes in a URL and an email address,

sends a POST request to the passed URL"""

import requests

from sys import argv
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625




<<<<<<< HEAD
if __name__ == "__main__":
    
    url = sys.argv[1]
    

    
    r = requests.get(url)
    
    if r.status_code >= 400:
        
        print("Error code: {}".format(r.status_code))
        
    else:
        
        print(r.text)
=======

if __name__ == "__main__":
    
    req = requests.get(argv[1])
    
    if req.status_code >= 400:
        
        print('Error code: {}'.format(req.status_code))
        
    else:
        
        print(req.text)
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625
