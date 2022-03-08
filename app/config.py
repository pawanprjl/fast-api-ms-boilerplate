import os
from functools import lru_cache


class BaseConfig:
    # fetch database environment from .env
    # TODO: change the credentials later
    DB_PROVIDER = os.environ.get('DB_PROVIDER', 'mysql+pymysql')
    DB_DATABASE = os.environ.get('DB_DATABASE', 'mysql')
    DB_USER = os.environ.get('DB_USER', 'pawan')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
    DB_HOST = os.environ.get('DB_HOST', 'mysql')
    DB_PORT = os.environ.get('DB_PORT', '3306')

    SQLALCHEMY_DATABASE_URL = f"{DB_PROVIDER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    DATABASE_CONNECT_DICT: dict = {}

    POST_API_HOST = os.environ.get('POST_API_HOST', 'http://localhost:8080/api')


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


class StagingConfig(BaseConfig):
    pass


@lru_cache()
def get_settings():
    config_cls_dist = {
        "dev": DevelopmentConfig,
        "prod": ProductionConfig,
        "staging": StagingConfig
    }

    config_name = os.environ.get("FAST_API_CONFIG", "dev")
    config_cls = config_cls_dist[config_name]
    return config_cls


settings = get_settings()
