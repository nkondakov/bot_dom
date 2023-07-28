import os
from pathlib import Path
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class DatabaseConfig:
    @property
    def conn_string(self) -> str:
        return "sqlite:///data/db.sqlite"

    @property
    def async_conn_string(self) -> str:
        return "sqlite+aiosqlite:///data/db.sqlite"


@dataclass
class TgBot:
    token: str
    use_redis: bool


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(env_file: Path) -> Config:
    load_dotenv(dotenv_path=env_file)

    return Config(
        tg_bot=TgBot(
            token=str(os.environ["BOT_TOKEN"]),
            use_redis=eval(os.environ["USE_REDIS"]),
        ),
        db=DatabaseConfig(),
    )


if __name__ == '__main__':
    pass
