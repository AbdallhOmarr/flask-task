import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'azlkqkwommxkm342p5lsmdvxcaszx'
    DEBUG = True
    TESTING = True


    
class DevelopmentConfig(Config):
    TESTING = False 
    MYSQL_USER= 'root'
    MYSQL_PASSWORD = '3agD-Fdc3GgadFbg23hf2Aac6ce-1g6a'
    MYSQL_HOST = 'monorail.proxy.rlwy.net'
    MYSQL_DB = "railway"
    MYSQL_PORT = 54859
    MYSQL_URL = 'mysql://root:3agD-Fdc3GgadFbg23hf2Aac6ce-1g6a@mysql.railway.internal:3306/railway'
    
 
class TestingConfig(Config):
    DEBUG = False 
        
    # database url for testing
    MYSQL_DATABASE_USER= 'root'
    MYSQL_DATABASE_PASSWORD = 'root12345#'
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_DB = "car_rental_test"
    

class ProductionConfig(Config):
    TESTING = False
    DEBUG = False 
    
    # database url for production 
    
    
config = {
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig,
    "default":DevelopmentConfig
}