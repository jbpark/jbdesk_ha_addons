from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234@localhost:3306/testdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

admin = Admin(app, name='microblog', template_mode='bootstrap3')
# Add administrative views here

app.run()