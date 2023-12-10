import datetime
import os
# from flask_jwt_extended import JWTManager
from datetime import timedelta

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from flask_apscheduler import APScheduler
from flask_uploads import UploadSet, configure_uploads, IMAGES
from sqlalchemy import MetaData

app = Flask(__name__)
load_dotenv()

# scheduler = APScheduler()

app.config['SECRET_KEY'] = 'asecretkey'
############################
### DATABASE SETUP ##########
########################
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.getenv('DB_LOCATION')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
  # os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(app, metadata=MetaData(naming_convention=naming_convention))

Migrate(app, db)
migrate = Migrate(app, db, render_as_batch=True)
with app.app_context():
    if db.engine.url.drivername == "sqlite":
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db, render_as_batch=True)

# app.config["JWT_SECRET_KEY"] = "super-secret"
# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=12)
# jwt = JWTManager(app)


app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/uploads/issues')
# app.config['UPLOADED_PHOTOS_ALLOW'] = set(['jpg', 'jpeg', 'png', 'gif'])
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# patch_request_class(app)


app.config.update(
    UPLOAD_PATH=os.path.join(basedir, 'static')
)

#########################
#########################
# LOGIN CONFIGS
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

exp_time = datetime.datetime.utcnow() + timedelta(days=365 * 10)  # Expires in 10 years

# Encode the token using the user's credentials
# token = jwt.encode({'username': 'apikey', 'exp': exp_time}, app.config['SECRET_KEY'], algorithm='HS256')
# print(token)


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "raymondvaughanwilliams@gmail.com"
app.config["MAIL_PASSWORD"] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)
# emailpassword = os.environ.get('MAIL_PASSWORD')

from structure.core.views import core
from structure.users.views import users
from structure.web.views import web
from structure.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(web)
app.register_blueprint(error_pages)
