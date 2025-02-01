
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"
    OPENAI_KEY = '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'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}