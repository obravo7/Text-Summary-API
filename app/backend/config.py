

class Config:
    JSON_AS_ASCII = True
    PROPAGATE_EXCEPTIONS = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user_name}:{password}' \
        '@{host_name}/{database}?charset=utf8'.format(

            # TODO: use with SQLAlchemy
            user_name='',
            password='',
            host_name='localhost',
            database='summary'
        )
