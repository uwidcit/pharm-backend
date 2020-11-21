from flask import Flask
from flask_jwt import JWT
from datetime import timedelta 
from flask_uploads import UploadSet, configure_uploads, IMAGES, TEXT, DOCUMENTS

from App.models import db

from App import CONFIG

from App.views import (
    api_views
)

def create_app():
    app = Flask(__name__, static_url_path='')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+CONFIG['dbuser']+':'+CONFIG['dbpassword']+'@'+CONFIG['dbhost']+'/'+CONFIG['dbname']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config['SECRET_KEY'] = CONFIG['secret_key']
    app.config['UPLOADED_PHOTOS_DEST'] = CONFIG['uploadDir']
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=CONFIG['JWTdeltaDays'])
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    db.init_app(app)
    return app

app = create_app()

app.app_context().push()

app.register_blueprint(api_views)

''' Set up JWT here (if using flask JWT)'''
# def authenticate(uname, password):
#   pass

# #Payload is a dictionary which is passed to the function by Flask JWT
# def identity(payload):
#   pass

# jwt = JWT(app, authenticate, identity)
''' End JWT Setup '''


if __name__ == '__main__':
    print('Application running in '+CONFIG['ENV']+' mode')
    app.run(host='0.0.0.0', port=8080, debug=CONFIG['debug'])
