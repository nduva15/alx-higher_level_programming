#!/usr/bin/python3

<<<<<<< HEAD
"""A script tha:

- takes in a letter

- sends POST request to http://0.0.0.0:5000/search_user

with the letter as a parameter.

"""

import sys

import requests

=======
"""sends a request to the URL and displays the value of the X-Request-Id"""

import requests

from sys import argv

>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625




if __name__ == "__main__":
    
<<<<<<< HEAD
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    
    payload = {"q": letter}
    

    
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    
    try:
        
        response = r.json()
        
        if response == {}:
=======
    if len(argv) > 1:
        
        q = argv[1]
        
    else:
        
        q = ""
        

        
    try:
        
        _data = {'q': q}
        
        url = 'http://0.0.0.0:5000/search_user'
        
        req = requests.post(url, _data).json()
        
        if not req:
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625
            
            print("No result")
            
        else:
            
<<<<<<< HEAD
            print("[{}] {}".format(response.get("id"), response.get("name")))
=======
            print("[{}] {}".format(req.get('id'), req.get('name')))
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625
            
    except ValueError:
        
        print("Not a valid JSON")
