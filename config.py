import logging
from dataclasses import dataclass
import yaml

@dataclass
class CafeConfig:
    collect_earnings: bool
    invite_cafe_1: bool
    invite_cafe_2: bool
    characters_touch_cafe_1: bool
    characters_touch_cafe_2: bool

@dataclass
class SocialConfig:
    club_reward_claim: bool

@dataclass
class Config:
    game_process: str
    game_window_title: str
    logs_level: int
    start_game: bool
    prepare_game: str
    cafe: CafeConfig
    social: SocialConfig

def load_config(path='config.yaml') -> Config:
    with open(path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    return Config(
        game_process=data['game_process'],
        game_window_title=data['game_window_title'],
        logs_level=logging.getLevelNamesMapping().get(data['logs_level'].upper(), logging.INFO),
        start_game=data['start_game'],
        prepare_game=data['prepare_game'],
        cafe=CafeConfig(**data['cafe']),
        social=SocialConfig(**data['social'])
    )

config = load_config()