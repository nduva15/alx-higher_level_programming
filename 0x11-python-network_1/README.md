<<<<<<< HEAD
# Python - Network #1



This project involved learning how to use the `urllib` and `requests` Python

libraries to send and receive HTTP messages to URL's. I practiced sending `GET`

and `POST` requests, fetching JSON resources, and interacting with API's (the

Star Wars API, GitHub API, and Twitter API).



## Tasks :page_with_curl:



* **0. What's my status? #0**

  * [0-hbtn_status.py](./0-hbtn_status.py): Python script that fetches
  
  `https://intranet.hbtn.io/status`.
  
  * Uses `urllib`.
  


* **1. Response header value #0**

  * [1-hbtn_header.py](./1-hbtn_header.py): Python script that displays the
  
  `X-Request-Id` response header variable of a request to a given URL.
  
  * Usage: `./1-hbtn_header.py <URL>`
  
  * Uses `urllib`.
  


* **2. POST an email #0**

  * [2-post_email.py](./2-post_email.py): Python script that sends a `POST`
  
  request to a given URL with a given email, and displays the response body.
  
  * Usage: `./2-post_email.py <URL> <email>`.
  
  * Uses `urllib`.
  


* **3. Error code #0**

  * [3-error_code.py](./3-error_code.py): Python script sends a request to
  
  a given URL and displays the response body.
  
  * Handles HTTP errors.
  
  * Uses `urllib`.
  


* **4. What's my status? #1**

  * [4-hbtn_status.py](./4-hbtn_status.py): Python script that fetches
  
  `https://intranet.hbtn.io/status`.
  
  * Uses `requests`.
  


* **5. Response header value #1**

  * [5-hbtn_header.py](./5-hbtn_header.py): Python script that displays the
  
  `X-Request-Id` response header variable of a request to a given URL.
  
  * Usage: `./5-hbtn_header.py <URL>`
  
  * Uses `requests`.
  


* **6. POST an email #1**

  * [6-post_email.py](./6-post_email.py): Python script that sends a `POST`
  
  request to a given URL with a given email, and displays the response body.
  
  * Usage: `./6-post_email.py <URL> <email>`.
  
  * Uses `requests`.
  


* **7. Error code #1**

  * [7-error_code.py](./7-error_code.py): Python script sends a request to
  
  a given URL and displays the response body.
  
  * Handles HTTP errors.
  
  * Uses `requests`.
  


* **8. Search API**

  * [8-json_api.py](./8-json_api.py): Python script that sends a `POST` request
  
  to `http://0.0.0.0:5000/search_user` with a letter passed as parameter.
  
  * Usage: `./8-json_api.py <letter>`
  
  * The letter is sent as the value of the variable `q`.
  
  * If no letter is given, sets `q=""`.
  
  * If the response body is properly formatted and non-empty, displays it as
  
  `[<id>] <name>`.
  
  * Uses `requests`.
  


* **9. My Github!**

  * [10-my_github.py](./10-my_github.py): Python script that takes GitHub
  
  credentials (username and password) and uses the Github API to display the
  
  corresponding ID.
  
  * Usage: `./10-my_github.py <username> <password>`
  
  * Uses `requests`.
  


* **10. Time for an interview!**

  * [100-github_commits.py](./100-github_commits.py): Python script that lists
  
  the 10 most recent comments of a given GitHub repository using the GitHub API.
  
  * Usage: `./100-github_commits.py <repository name> <owner name>`
  
  * Uses `requests`.
=======
0x11. Python - Network #1

Table of contents

Files Description

0-hbtn_status.py	Python script that fetches https://intranet.hbtn.io/status with the urllib package

1-hbtn_header.py	Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response

2-post_email.py		Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

3-error_code.py		Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)

4-hbtn_status.py	Python script that fetches https://intranet.hbtn.io/status with the requests package

5-hbtn_header.py	Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header

6-post_email.py		Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response

7-error_code.py		Python script that takes in a URL, sends a request to the URL and displays the body of the response

8-json_api.py		Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter

10-my_github.py		Python script that takes your Github credentials (username and password) and uses the Github API to display your id

100-github_commits.py	Python script that takes in Github repo and owner name to list 10 commits (from the most recent to oldest)
>>>>>>> a1cb096b6652ca13a4e5fb24e043d4fbe759e625
