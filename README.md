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

<!--1.  first step after creating an app -->
<!-- make the main project aware that a new app has been created through settings.py in main project folder -->
<!-- For this go to settings.py inside of main project folder and write the name of app that is created such as "project1" in this case under installed apps lists -->

<!--2. Second step is to make the templates appear in the application create  -->
<!-- things to consider: we had already made a template under the main project but considering each application is a unique app we can meke a different template in each of the app -->
<!--create a template folder under application and under that same app name and under that all templates will be created  -->


<!-- step 3. as seen in the diagram: make the views(html file inside of project1 render by using request and render) -->
<!-- now the urls has to be passed to the application form main project one  -->
<!-- for this create urls.py within the application as it won't exist 
after this creation copy the content of urls.py from root level and paste it on the application folder
-->
<!-- Important thing to do now is to give access to that url.py file of the app that we have create for this use or
import include and use this syntax
 -->
 <h2>Giving access to the apps urls</h2>
 <h3>path('blog/', include('blog.urls'))</h3>

<h2>Check url.py to find which pages present and which page are made homepage</h2>

 <!-- Usage of common layout files that can be used with only some basic synatx -->
 <!-- A unnamed block will be used in every layout(the block will be positioned within a specified area)
  -->
  <!-- to use this we have to use the exyend property in any other files -->
  <!-- In order to use templates place of other app we can use the same extend property -->
  <!-- the compiler will check first inside of the folder for layout file and if not it will check under the  root directory. -->

  <h2>For tailwind start</h2> 
  <!-- create venv or inside of venv that was created -->
   <h3>python manage.py tailwind start</h3>




  <!-- Working with models: -->
  <!-- first define models within each application it may consist of media like images -->
  <!-- For media access settings has to be updated -->
  <!-- update the url as accordingly the settings update -->


  <!-- Before making or running app we need to migrate the particular app using -->
  <!-- python manage.py makemigrations firstapp -->
  <!-- this will generate a migration file such that all the commands witten in models will create a 
  sql format within the init python file of the migrations folder.
   -->

   <!-- do migrate the manage.py file after this -->



   <!-- Through admin.py we can attach any model to it and can see it in admin panel -->
   <!-- 
   
   first step is to import the model made.
   second step is to add the method made inside of model into the admin.
   
   -->





<h2> Showing data from databse to frontend</h2>
<!-- first take all the object values from database and store in  a variale -->
<h3>mn=methodname.object.all()</h3>
<!-- at last at the render portion -->
<h3>{mn:"mn"}</h3>

<!-- use above to change at the formtend folder or html template at the beginning -->
<!-- Just be careful with the template that was created top match the structure. -->
<!-- 38 -->

<h2>Any change in model we have to use below syntax or simply make migration</h2>
<h3> python manage.py makemigrations "app_folder(firstapp)"</h3>
<h3>python manage.py migrate</h3>

<!-- Basically in view you have to put those things that you have to show -->
<!-- create a view or functions -->
<!-- view will ask for a page to display and create a html file -->
<!-- at last you need url for redirection to shoe the route -->

<!-- For relocation or redirect into another page we have used variable ({%....%}) inside of anchor tag

the anchor tag consists of url so that redirection can be provided.

in this case the name used along with url can be used again.
 -->

 <h2>Defining URL</h2>
 <h3>{% url 'aero_desc' ap.id %}</h3>