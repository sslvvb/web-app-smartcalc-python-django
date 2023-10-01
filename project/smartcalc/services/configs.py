"""Module for working with configuration file."""

from pathlib import Path
import yaml
from django.conf import settings


def read_config() -> dict:
    config: dict = _load_config()
    return config


def update_config(key: str, value: str) -> None:
    config: dict = read_config()
    config[key] = value
    _dump_config(config)


def _load_config() -> dict:
    Path(settings.CONFIG_FILE_PATH).touch(exist_ok=True)
    with open(settings.CONFIG_FILE_PATH, 'r', encoding='utf-8') as file:
        config: dict = yaml.safe_load(file) or {}
    return config


def _dump_config(config: dict) -> None:
    with open(settings.CONFIG_FILE_PATH, 'w', encoding='utf-8') as file:
        yaml.safe_dump(config, file)
