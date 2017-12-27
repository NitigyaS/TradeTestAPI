"""
The instance folder is designed to not be under version control and be deployment specific. It’s the perfect place to drop things that either change at runtime or configuration files.
"""

SECRET_KEY = 'p9Bv<3Eid9%$i01'
SQLALCHEMY_DATABASE_URI = 'mysql://flask_admin:flask_admin@localhost/web_app_flask'