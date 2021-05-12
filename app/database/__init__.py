from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app
from flask_mail import Mail, Message

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Metrohuy1770@finaldb.chzxzrzzf3ot.ap-southeast-1.rds.amazonaws.com:3306/finaldb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/duan_cntt2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mysql_db = SQLAlchemy(app)
migrate = Migrate(app, mysql_db)