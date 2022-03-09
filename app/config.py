import os
from functools import lru_cache


class BaseConfig:
    # fetch database environment from .env
    # TODO: change the credentials later
    DB_PROVIDER = os.environ.get('DB_PROVIDER', 'mysql+pymysql')
    DB_DATABASE = os.environ.get('DB_DATABASE', 'ms-api')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'root')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '3306')

    SQLALCHEMY_DATABASE_URL = f"{DB_PROVIDER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    DATABASE_CONNECT_DICT: dict = {}

    POST_API_HOST = os.environ.get('POST_API_HOST', '') #Example http://<your_host>/api


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
