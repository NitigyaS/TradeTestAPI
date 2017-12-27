import os
from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

# execute only if run as a script
if __name__ == '__main__':
    app.run()


#export FLASK_CONFIG=development
#export FLASK_APP=run.py
#flask run


#For Database
#flask db init
#flask db migrate
#flask db upgrade