from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from flask import session
#from flask_session import Session
from datetime import timedelta 
from flask_uploads import UploadSet, configure_uploads, IMAGES, TEXT, DOCUMENTS


'''from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()'''
from App.models.database import *

from App.models.user import *

from App.controllers.auth import *

from App import CONFIG

from App.views import (
    api_views,
    product_views,
    auth_views,
    cart_views
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
    #sess = Session()
    #sess.init_app(app)
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    db.init_app(app)
    return app

app = create_app()

app.app_context().push()

#db.create_all(app=app)

app.register_blueprint(api_views)
app.register_blueprint(product_views)
app.register_blueprint(auth_views)
app.register_blueprint(cart_views)

jwt = JWT(app, authenticate, identity)



if __name__ == '__main__':
    print('Application running in '+CONFIG['ENV']+' mode')
    app.run(host='0.0.0.0', port=8080, debug=CONFIG['debug'])
