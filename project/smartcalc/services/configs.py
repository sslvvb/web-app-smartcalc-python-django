"""Модуль для работы с файлом конфигурации."""

# from pathlib import Path
import yaml

CONFIG_PATH: str = "smartcalc/configs/config.yml"


def read_config() -> dict:
    # Path(HISTORY_PATH).touch(exist_ok=True) ???
    with open(CONFIG_PATH, 'r') as file:
        config: dict = yaml.safe_load(file)
        return config
