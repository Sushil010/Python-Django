# Python-Django
<h3></h3>
<h2>activate virual environment:</h2>
<h3>with command => ".venv/Scripts/activate"</h3>

<h2>Deactivte environment</h2>
<h3>deactivate</h3>


<h2>Django installation</h2>
<h3>uv pip install Django</h3>


<h2>project start</h2>
<!-- A project will be created only once but apps will be multiple inside the project -->
<h3>django-admin startproject "foldername or projectname"</h3>
<p>a subfolder with the same project or foldername will be created change directory into that folder
and start creating projects
</p>

<p>after moving into subfolder use command
<h3>python "filename" runserver (port-name:optional(8001,8000...))</h3>
</p>
![alt text](image.png)


<h2>Create application:</h2>
<!-- this below command will only create a file inside of project folder(whcih was initailized at start) -->
<!-- urls locator or url.py and settings.py won't be in these applications -->
<h3>python manage.py startapp "app-name"</h3>

<!-- first step after creating an app -->
<!-- make the main project aware that a new app has been created through settings.py in main project folder -->