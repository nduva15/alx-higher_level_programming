#!/usr/bin/python3

<<<<<<< HEAD
"""A script that:

- takes in a URL

- sends a POST request to the passed URL

- takes email as a parameter

- displays the body of the response

"""

import sys

import urllib.parse

import urllib.request
=======
from sys import argv

from urllib.request import Request, urlopen

from urllib.parse import urlencode
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625





if __name__ == "__main__":
    
<<<<<<< HEAD
    url = sys.argv[1]
    
    value = {"email": sys.argv[2]}
    
    data = urllib.parse.urlencode(value).encode("ascii")
    

    
    request = urllib.request.Request(url, data)
    
    with urllib.request.urlopen(request) as response:
        
        print(response.read().decode("utf-8"))
=======
    url = argv[1]
    
    values = {'email': argv[2]}
    

    
    data = urlencode(values)
    
    data = data.encode('ascii')
    
    req = Request(url, data)
    
    with urlopen(req) as res:
        
        content = res.read().decode('utf-8')
        
        print(content)
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625
