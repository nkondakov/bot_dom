import os
from pathlib import Path
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(env_file: Path) -> Config:
    load_dotenv(dotenv_path=env_file)

    return Config(
        tg_bot=TgBot(
            token=str(os.environ["BOT_TOKEN"]),
        ),
    )


if __name__ == "__main__":
    pass
