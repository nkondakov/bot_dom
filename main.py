import asyncio
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers.base import start_router
from settings.settings import load_config


async def main() -> None:
    path_to_settings = Path.cwd() / ".env/prod"
    config = load_config(path_to_settings)
    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp = Dispatcher(storage=storage)
    dp.include_router(start_router)
    dp["config"] = config

    try:
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
