#!/usr/bin/python3

<<<<<<< HEAD
"""A script that

- fetches https://alx-intranet.hbtn.io/status.

- uses urlib package

"""





if __name__ == '__main__':
    
    import urllib.request
    

    
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        
        content = res.read()
        
        print("Body response:")
        
        print("\t- type: {}".format(type(content)))
=======
"""Python script that fetches"""

import urllib.request





def getStatus():
    
    """a"""
    
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        
        content = res.read()
        
        type_content = type(content)
        
        print("Body response:")
        
        print("\t- type: {}".format(type_content))
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625
        
        print("\t- content: {}".format(content))
        
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
<<<<<<< HEAD
=======
        

        
if __name__ == "__main__":
    
    getStatus()
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625
