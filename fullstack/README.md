<h1></h1>

<h2>Environment Setup</h2>
<h3> python -m venv .venv</h3>

<h2>Activate the virtual environment</h2>
<h3>h.venv\Scripts\activate</h3>

<h2>make a requirement.txt file</h2>
<h3>python freeze > requirements.txt</h3>

<h2>Install uv if required</h2>
<h3>pip install uv</h3>

<h2>install django</h2>
<h3>uv pip install django</h3>

<h2>create django project</h2>
<h3>django-admin startproject project_name</h3>

change directory to created project and run server
<h3>python manage.py runserver</h3>

make migrations 
<h3>python manage.py makemigrations</h3>
<h3>python manage.py migrate</h3>

create superuser
<h3>python manage.py createsuperuser (Sushil/Sushil010)</h3>
