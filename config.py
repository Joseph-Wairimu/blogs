import os
class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blogs'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    @staticmethod
    def init_app(app):
        pass
class ProdConfig(Config):
    pass
    
    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blogs'
    DEBUG = True  
    

    pass

config_options = {
'development':DevConfig,
'production':ProdConfig
}

 