#!/usr/bin/python3

<<<<<<< HEAD
"""lists the 10 most recent commits on a given GitHub repository.

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
    url = "https://api.github.com/repos/{}/{}/commits".format(
        
        sys.argv[2], sys.argv[1])
    

    
    r = requests.get(url)
    
    commits = r.json()
    
    try:
        
        for i in range(10):
            
            print("{}: {}".format(
                
                commits[i].get("sha"),
                
                commits[i].get("commit").get("author").get("name")))
            
    except IndexError:
        
        pass
=======
    aut = argv[2]
    
    url = "https://api.github.com/repos/" + aut + "/" + argv[1] + "/commits"
    
    req = requests.get(url).json()
    
    commits = 0
    
    for line in req:
        
        print("{}: {}".format(line['sha'], line['commit']['author']['name']))
        
        commits += 1
        
        if commits == 10:
            
            exit()
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625
