"""
This module sets up the application configuration.

It utilizes Pydantic's BaseSettings for configuration management,
allowing settings to be read from environment variavbles and a .env file.
"""

from pydantic import DirectoryPath, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelSettings(BaseSettings):
    """
    ML configuration settings for the application.

    Attributes:
        model_config (SettingsConfigDict): Model config, loaded from .env file.
        model_path (DirectoryPath): Filesystem path to the model.
        model_name (str): Name of the ML model.
    """

    model_config = SettingsConfigDict(
        env_file='config/.env',
        env_file_encoding='utf-8',
        extra='ignore',
        protected_namespaces=('settings',),
    )

    data_file_name: FilePath
    model_path: DirectoryPath
    model_name: str


model_settings = ModelSettings()
