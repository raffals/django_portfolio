# django_portfolio

## DIFFERENCE BETWEEN LOCAL AND PRODUCTION BRANCHES:

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


