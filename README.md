### Project Setup:
1. Install Python3<br/>

2. Install PostgreSQL<br/>

3. Create Database called `sipnsavor`<br/>

4. Create user with `username` and `password` as mentioned in the `.env` file<br/>

5. Setup a virtual environment:<br/>
`python3 -m venv env`

6. Activate the virtual environment:<br/>
`source env/bin/activate`

7. Install all packages:<br/>
`pip install -r requirements.txt`

8. Make Migrations:<br/>
`./manage.py makemigrations`

9. Run Migrations:<br/>
`./manage.py migrate`

10. Run Server:
`./manage.py runserver`

