import os
class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
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
 
    DEBUG = True  
    

    pass

config_options = {
'development':DevConfig,
'production':ProdConfig
}

 