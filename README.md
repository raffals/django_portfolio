# django_portfolio

## Difference between local and production areas:

* LOCAL:

	* local_requirements.txt  
	   * -- NO: python-dotenv==0.14.0 (only required to setup pAnywhere environment)  
 
* Untracked files:

    * portfolio/settings.py -> local_settings.py (omit since don't want to have to
       update everytime we do a pull/clone/etc. = just create once when setting up
       the local & prod areas) 
	* portfolio/prod_settings.py (upload directly = don't want in public repo)
	* steps.txt
	* projects/static/projects/img/emThumb786x875.png 
	
<hr />

* PythonAnywhere PRODUCTION: 

* Untracked files:
	* portfolio/settings.py -> prod_settings.py (omit since don't want to have to
       update everytime we do a pull/clone/etc. = just create once when setting up
       the local & prod areas) 
	* portfolio/prod_settings.py (upload directly = don't want in public repo)
	* prod_requirements.txt (better security if don't include this in public repo)
      * -- YES: python-dotenv==0.14.0  (only required to setup pAnywhere environment) 
	* staticfiles/

<hr />

Heroku PRODUCTION:


## Deployment Steps:

* LOCAL:

* Make changes
  * May include (if made changes to DB via JSON): ./manage.py loaddata projectsSlides.json 
  * May include (if made direct changes to DB): ./manage.py dumpdata --indent 2 projects > projectsSlides.json
* git add
* git commit
* git push

* PRODUCTION:

* git pull --ff-only

  * PythonAnywhere: 
	* If change to static files (eg, images): python manage.py collectstatic 
	  * If a file's missing, use: python manage.py findstatic <filename>
	  * Reload raffals.pythonanywhere.com

  * Heroku:

