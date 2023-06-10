from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📝 Генерировать текст", callback_data="generate_text"),
            InlineKeyboardButton(text="🖼 Генерировать изображение", callback_data="generate_image"),
        ],
        [
            InlineKeyboardButton(text="💳 Купить токены", callback_data="buy_tokens"),
            InlineKeyboardButton(text="💰 Баланс", callback_data="balance"),
        ],
        [
            InlineKeyboardButton(text="💎 Партнёрская программа", callback_data="ref"),
            InlineKeyboardButton(text="🎁 Бесплатные токены", callback_data="free_tokens"),
        ],
        [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")],
    ]
)

exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
