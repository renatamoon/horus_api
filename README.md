# horus_api
Web scraping robot API using Playwright with Flask (Python)

<hr>

<p align="center">
  <a href="#projeto">About the project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#tecnologias">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#instalacao">How to execute it</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#imagens">Images</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
</p>

## <a id="projeto"> 💻 ABOUT THE PROJECT </a>

Webscraping challenge using Playwright library as a tool to webscrap, save it on database, finally getting data of notebooks from 
website `https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops`.

Some functionalities present on this project:

    * Webscraping with Playwright;
    * Data insertion on MongoDB;
    * Route to save data on MongoDB;
    * Route to get data from MongoDB;

🟩 PROJECT STATUS: <b>FINISHED</b> <br>

<hr>

## <a id="tecnologias"> 🧪 TECNOLOGIES </a>

- Python
- Flask
- MongoDB
- Playwright

<hr>

## <a id="instalacao"> 🔴 HOW TO EXECUTE IT </a> 

<b>- Clone the repo with the following command:</b> `git clone https://github.com/renatamoon/horus_api.git` <br>

<hr> 

#### On Windows

<b>- Create your virtual environment:</b> `python -m venv venv`<br>
<b>- Activate your virtual environment: </b>`. venv\Scripts\Activate.ps1`<br>
<b>Obs: If for any reason occurs and error:</b> on powershell execute the following command: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`<br>
<b>- Execute requirements with the command: </b>`pip install -r requirements.txt`<br>

<hr> 

#### On Linux:

<b>- Create your virtual environment:</b> `virtualenv venv`<br>
<b>- Activate your virtual environment:</b> `. venv/bin/activate`<br>
<b>- Execute requirements with the command:</b> `pip install -r requirements.txt`<br>

<hr> 
  
* Change your local string connections on the file <b>`.env`</b> <br>
* Create a database on your Local MongoDB: `laptop_database` <br>
* Create a collection on your Local MongoDB `laptop_collection` <br>

<hr>

## <a id="instalacao"> 🔴 EXECUTE HYPERCORN </a> 

- To Execute the application run the command: `uvicorn main:app --reload`

<hr>

## <a id="instalacao"> 🔴 REQUISITION ROUTES </a> 

- First use the following route to save data on your database: `http:{your-host}/put/save_laptops` ;
- Then you can use the route `http:{your-host}/get_all_laptops` to get all data from the database;

<hr>

## <a id="imagens"> 🔴 RESPONSES: </a> 

- Expected return of the route `/put/save_laptops` :

![img.png](img.png)

- Expected return of the route `get_all_laptops` :

![img_1.png](img_1.png)
