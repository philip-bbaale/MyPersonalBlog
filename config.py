import os

class Config:
    
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'postgres://olaxeopvvvaovc:2e9199e55fc98030a8843ced2950c34be63a60514637c6a925676bc3d0ef5ef0@ec2-52-201-55-4.compute-1.amazonaws.com:5432/d29v2atrpmeual'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
<--->