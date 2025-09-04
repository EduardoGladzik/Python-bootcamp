import os
from datetime import timedelta

class Config:
    """Configuração base"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
class DevelopmentConfig(Config):
    """Configuração para desenvolvimento"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Configuração para produção"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Configuração para testes"""
    DEBUG = True
    TESTING = True

# Mapeamento de configurações
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

