"""Модуль для работы с файлом конфигурации."""

# from pathlib import Path
import yaml

CONFIG_PATH: str = "smartcalc/configs/config.yml"


def read_config() -> dict:
    # Path(HISTORY_PATH).touch(exist_ok=True) ???
    with open(CONFIG_PATH, 'r') as file:
        return yaml.safe_load(file)


def write_background_to_config(background: str) -> dict:
    # Path(HISTORY_PATH).touch(exist_ok=True) ???
    with open(CONFIG_PATH, 'r') as file:
        config: dict = yaml.safe_load(file)
        config['background'] = background
    with open(CONFIG_PATH, 'w') as file:
        yaml.safe_dump(config, file)
        return config

    # theme = config['theme']
    # print(theme)
    #
    # config['theme'] = 'light'
    # print(config['theme'])
    #
    # with open('smartcalc/configs/config.yml', 'w') as file:
    #     yaml.safe_dump(config, file)
