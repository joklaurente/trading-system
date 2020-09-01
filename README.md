# Trading System API
Django Rest API for Simple Trading System

## Cloning repository
1. Open Git Bash. If you dont have Git Bash installed in your machine, you can download it from the https://git-scm.com/downloads and install it in your machine.
2. Change the current working directory to the location where you want the cloned directory.
3. Run the following command:
```
git clone https://github.com/joklaurente/trading-system.git
```
## Installing Python
1. Download and install Python from the official website: https://www.python.org/downloads/
2. To verify the Python installation, open your command prompt then type `python` and press Enter.
3. If Python is installed correctly, you should see output similar to what is shown below:
```
Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:46:45) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```
## Installing Pip and Pipenv
1. Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer.
2. Open a command prompt and navigate to the folder containing the get-pip.py installer.
3. Run the following command:
```
python get-pip.py
```
4. To verify the Pip installation, open your command prompt and enter the following command:
```
pip -V
```
5. If Pip is installed correctly, you should see output similar to what is shown below:

```
pip 20.1.1 from c:\python38\lib\site-packages\pip (python 3.8)
```
6. Install Pipenv by running the following command:
```
pip install pipenv
```
## Running the server
1. Go to the location where you cloned the reposity.
2. Create a virtual environment for your application.
```
pipenv shell
```
3. Install Django and other dependencies from Pipfile.
```
pipenv install
```
4. Load initial data for the application.
```
cd trading-system/
python manage.py loaddata fixtures/stocks.json
```
5. Start the Django development web server
```
python manage.py runserver
```
## API Endpoints
### Show User
----
  Creates a new user and returns a token.

* **URL**

  /api/user/register

* **Method:**

  `POST`
  
*  **Required Params**
 
   `username=[string]`<br />
   `password=[string]`


* **Success Response:**

  * **Code:** 201 CREATED<br />
    **Content:** `{
    "response": "Successfully registered a new user.",
    "username": "user",
    "token": "96033009074f716d51ad27480f1c89a4efa612c4"
}`
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST<br />
    **Content:** `{"username":["A user with that username already exists."]}`

* **Sample Call:**

  ```
  curl --location --request POST 'http://localhost:8000/api/user/register' \
  --form 'username=user' \
  --form 'password=password'
  ```