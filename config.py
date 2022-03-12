
class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blog'
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

 