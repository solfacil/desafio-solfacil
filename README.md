# Desafio Solfácil

## Installation
    
    You can run the project by 2 ways:

## 1 
- Install docker in your computer 
- run `docker-compose up`

## 2 -     
1. Create a virtual environment and activate it.
    - python -m venv myenv
    - myenv\Scripts\activate.bat (Windows)
    - source myenv/bin/activate (Linux)
2. Install the requirements by running `pip install -r requirements.txt`.
3. Run the makemigrations by running `python manage.py makemigrations`.
4. Run the migrations by running `python manage.py migrate`.
5. Run the server by running `python manage.py runserver`.

## Usage

Access the website at `http://localhost:8000/`.
 
You can navegate through the app and do all the actions there, but if
you prefer you can access the following urls in any program like Postman
to make the requests.
 
## Requests:

- Access Admin panel

    First you will have to create a superuser, for that use the command `python manage.py createsuperuser`.

    Follow the prompts to enter a username, email, and password for the superuser account.

    Then make the request to the admin url
    ```
    GET http://localhost:8000/admin/
    ```
    Enter the username and password for the superuser account to log in to the admin panel.

- Access the Partners List 
    ```
    GET http://localhost:8000/partners/
    ```
- Access the Partners Address List 
    ```
    GET http://localhost:8000/partners/address/
    ```
- Upload CSV

    That is a little trickier.. 
    In Postman on the request body, click "form-data", hover over the "key" input field, and find the hidden dropdown that says "Text". Click "Text", and then change it to say "File"

    for the last, in the Key field, put 'csv_file' and make the POST request
    ```
    POST http://localhost:8000/uploadCsv/
    ```
    ![alt text](./Postman_Example.png)