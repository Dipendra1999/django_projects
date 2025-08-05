# django_projects
this helps to build webpage that helps in deploying ML models on websites to check connectivity and effectivity and availability.

-**Create the admin user by the following commands**:
 +BY manage.py:
python manage.py createsuperuser

enter the username , email and password 
+By shell:
type= python manage.py shell
>>> from django.contrib.auth.models import User
>>>User.objects.create_superuser('yourusername', 'youremail@example.com', 'yoursecurepassword')

