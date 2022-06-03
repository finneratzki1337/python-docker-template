# Template for Python Apps with local development running in a Docker container
##
Pull and launch either within virtual environment
Create virtual environment
~~~
python -m venv venv
~~~
Windows:
~~~
venv/Scripts/activate
~~~
Linux:
~~~
source venv/bin/activate
~~~
Install required dependenvies
~~~
pip install -r requirements.txt
~~~
Launch app:
~~~
python app.py
~~~
Or simply launch Docker Container
~~~
docker-compose up --build
~~~
## Environment Variables
e.g. containing credentials. .env files will be ignored by .gitignore. Copy the template file and rename to .en
## Config
Folder will ignore everything but conf_template.conf. Use as needed and adjust sections. Example in template.
## Own modules
Own modules can be imported as usual from folders in main directory. See import of module_template as example.