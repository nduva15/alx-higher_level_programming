#!/usr/bin/python3

<<<<<<< HEAD
"""A script that:

- takes in a URL,

- sends a request to the URL

- displays the body of the response (decoded in utf-8).

"""
=======
from sys import argv

from urllib.request import Request, urlopen

from urllib.parse import urlencode

from urllib.error import HTTPError
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625





if __name__ == "__main__":
    
<<<<<<< HEAD
    import sys
    
    from urllib import request, error
=======
    req = Request(argv[1])
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625
    

    
    try:
        
<<<<<<< HEAD
        with request.urlopen(sys.argv[1]) as res:
            
            print(res.read().decode('UTF-8'))
            
    except error.HTTPError as er:
        
        print('Error code:', er.code)
=======
        with urlopen(req) as res:
            
            print(res.read().decode('utf-8'))
            
    except HTTPError as ex:
        
        print('Error code:', ex.code)
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625
