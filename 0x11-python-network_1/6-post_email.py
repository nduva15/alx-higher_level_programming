#!/usr/bin/python3

<<<<<<< HEAD
"""A  script that:

- takes in a URL and an email address

- sends a POST request to the passed URL with the email as a parameter

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




if __name__ == "__main__":
    
<<<<<<< HEAD
    url = sys.argv[1]
    
    value = {"email": sys.argv[2]}
    

    
    r = requests.post(url, data=value)
    
    print(r.text)
=======
    values = {'email': argv[2]}
    
    req = requests.post(argv[1], data=values)
    
    print(req.text)
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625
