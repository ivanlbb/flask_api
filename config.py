import os
from dotenv import load_dotenv


dotenv_file_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_file_path):
    load_dotenv(dotenv_file_path) #Parse a .env file and then load all the variables found as environment variables.
                                  # the .env file contains a CONFIGURATION_SETUP entry than points to one of the below class

    
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(Config):
    ENV = "development"
    #SQLALCHEMY_DATABASE_URI = "postgresql+pypostgresql://postgres:minerva@ivan-pb:5432/ivan"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:minerva@ivan-pb:5432/ivan'
    
class DockerConfig(Config):
    ENV = "docker"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:minerva@172.17.0.3:5432/ivan'

class ProductionConfig(Config):
    pass


