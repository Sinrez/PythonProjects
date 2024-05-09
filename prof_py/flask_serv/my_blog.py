#export FLASK_APP=app && export FLASK_ENV=development && flask run
#source flask_env/bin/activate      

from app import create_app

app = create_app()
app.logger.info("MyBlog is running")