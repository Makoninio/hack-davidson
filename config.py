
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