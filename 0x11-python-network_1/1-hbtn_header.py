#!/usr/bin/python3

<<<<<<< HEAD
"""A script that:

- takes in a URL,

- sends a request to the URL and displays the value

- of the X-Request-Id variable found in the header ofthe response.

"""

import sys

import urllib.request



if __name__ == "__main__":
    
    url = sys.argv[1]
    

    
    request = urllib.request.Request(url)
    
    with urllib.request.urlopen(request) as response:
        
        print(dict(response.headers).get("X-Request-Id"))
=======
"""sends a request to the URL and displays the value of the X-Request-Id"""

import urllib.request

import sys





def getRequest():
    
    """a"""
    
    with urllib.request.urlopen(sys.argv[1]) as res:
        
        req = res.headers.get('X-Request-Id')
        
        print(req)
        

        
if __name__ == "__main__":
    
    getRequest()
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625
