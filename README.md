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

### Create User and Token
----
  Creates a new user and token.

* **URL**

  `/api/user/register`

* **Method:**

  `POST`
  
*  **Required Params**
 
   `username=[string]`<br />
   `password=[string]`

*  **Header**
 
   `Authorization: None`

* **Success Response:**

  * **Code:** 201 CREATED<br />
```
{
    "response": "Successfully registered a new user.",
    "username": "user",
    "token": "96033009074f716d51ad27480f1c89a4efa612c4"
}
```

* **Sample Call:**

```
curl --location --request POST 'http://localhost:8000/api/user/register' \
--form 'username=user' \
--form 'password=password'
```

### Show Stock List
----
  Shows the list of stocks.

* **URL**

  `/api/stock/list`

* **Method:**

  `GET`
  
*  **Required Params**
 
   `None`

*  **Header**
 
   `Authorization: Token`

* **Success Response:**

  * **Code:** 200 OK<br />
```
[
    {
        "oid": "AC",
        "name": "Ayala Corporation",
        "price": 733.5
    },
    {
        "oid": "CHIB",
        "name": "China Banking Corporation",
        "price": 20.6
    },
    {
        "oid": "FEU",
        "name": "Far Eastern University, Inc.",
        "price": 575.0
    },
    {
        "oid": "FLI",
        "name": "Filinvest Land, Inc.",
        "price": 0.94
    },
    {
        "oid": "GLO",
        "name": "Globe Telecom, Inc.",
        "price": 2030.0
    },
    {
        "oid": "JFC",
        "name": "Jollibee Foods Corporation",
        "price": 135.1
    },
    {
        "oid": "MER",
        "name": "Manila Electric Company",
        "price": 269.0
    },
    {
        "oid": "SMPH",
        "name": "SM Prime Holdings, Inc.",
        "price": 29.0
    },
    {
        "oid": "SLF",
        "name": "Sun Life Financial, Inc.",
        "price": 1925.0
    },
    {
        "oid": "WLCON",
        "name": "Wilcon Depot, Inc.",
        "price": 16.2
    }
]
```

* **Sample Call:**

```
curl --location --request GET 'http://localhost:8000/api/stock/list' \
--header 'Authorization: Token 96033009074f716d51ad27480f1c89a4efa612c4'
```


### Create Stock
----
  Creates a new stock.

* **URL**

  `/api/stock/create`

* **Method:**

  `POST`
  
*  **Required Params**
 
   `oid=[string]`<br />
   `name=[string]`<br />
   `price=[float]`

*  **Header**
 
   `Authorization: Token`

* **Success Response:**

  * **Code:** 201 CREATED<br />
```
{
    "oid": "GLO",
    "name": "Globe Telecom, Inc.",
    "price": "500.00"
}
```

* **Sample Call:**

```
curl --location --request POST 'http://localhost:8000/api/stock/create' \
--header 'Authorization: Token 7b5187a2b32631aff0d61b29df4530cc08c741c7' \
--form 'oid=GLO' \
--form 'name=Globe Telecom, Inc.' \
--form 'price=500'
```

### Update Stock
----
  Updates an existing stock.

* **URL**

  `/api/stock/<int:pk>/`

* **Method:**

  `PUT`<br />
  `GET`
  
*  **Required Params**
 
   `oid=[string]`<br />
   `name=[string]`<br />
   `price=[float]`

*  **Header**
 
   `Authorization: Token`

* **Success Response:**

  * **Code:** 200 OK<br />
```
{
    "oid": "GLO",
    "name": "Globe Telecom, Inc.",
    "price": "1500.00"
}
```

* **Sample Call:**

```
curl --location --request PUT 'http://localhost:8000/api/stock/1/' \
--header 'Authorization: Token 47d06b1337e333df00060c50764231b53b15976a' \
--form 'oid=GLO' \
--form 'name=Globe Telecom, Inc.' \
--form 'price=1500'
```


