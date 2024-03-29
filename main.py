import asyncio
from aiogram_dialog import setup_dialogs
from bot import dp, bot


async def main() -> None:
    # Запускаем бота и пропускаем все накопленные входящие сообщения
    setup_dialogs(dp)  # Подключаем диалоги

    await bot.delete_webhook(drop_pending_updates=True)
    #  Запускаем бот
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
