# django_portfolio

## Difference between local and production areas:

LOCAL:

* Untracked files:

    * portfolio/settings.py -> local_settings.py (omit since don't want to have to
       update everytime we do a pull/clone/etc. = just create once when setting up
       the local & prod areas) 
	* portfolio/prod_settings.py (upload directly = don't want in public repo)
	* steps.txt
	* projects/static/projects/img/emThumb786x875.png 
	
<hr />

PRODUCTION: PythonAnywhere (separate git branch not required)

* Untracked files:
	* portfolio/settings.py -> prod_settings.py (omit since don't want to have to
       update everytime we do a pull/clone/etc. = just create once when setting up
       the local & prod areas) 
	* portfolio/prod_settings.py (upload directly = don't want in public repo)
	* prod_requirements.txt (better security if don't include this in public repo)
      * INCLUDES: python-dotenv==0.14.0  (dotenv only required to setup pAnywhere
        environment; rest is same as local_requirements.txt) 
	* staticfiles/

<hr />

PRODUCTION: Heroku

<hr />
<hr />

## Deployment Steps:

LOCAL:

* Make changes
  * May include (if made changes to DB via JSON):
	* ./manage.py loaddata projects.json 
  * May include (if made direct changes to DB):
	* ./manage.py dumpdata --indent 2 projects > projects.json
  * May include (if made significant changes to models.py):
	* python manage.py makemigrations projects
	* python manage.py migrate
* git add
* git commit
* git push

<hr />
 
PRODUCTION: PythonAnywhere (Bash console)

* cd django_portfolio
* workon myvirtualenv
* git pull --ff-only 
* May include (If change to static files - eg, images):
  * python manage.py collectstatic 
  * If a file's missing, use: python manage.py findstatic <filename\>
* Reload raffals.pythonanywhere.com via: https://www.pythonanywhere.com/user/raffals/webapps/

<hr />

PRODUCTION: Heroku

<hr />
