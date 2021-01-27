import importlib
import traceback
import html
import json
import re
from typing import Optional
import os
from telegram import Message, Chat, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async, DispatcherHandlerStop
from telegram.utils.helpers import escape_markdown

from firefoxbot import (
    dispatcher,
    DEV_USERS,
    SUDO_USERS,
    TOKEN,
)
 import typing_action

PM_START_TEXT = f"""
`Hi..Welcome` 💃
`I'm` [乂🖤⃝ƛԼƛƝƘƦƖƬӇƛ💃⃟ 🦋࿐](https://telegra.ph/file/7f9e3d2e338f8567a47eb.jpg)
`I'm here to help you manage your groups.. Click Help button to find out more about how to use me to my full potential..`
"""
buttons += [[InlineKeyboardButton(text="♻️ ADD ME TO YOUR GROUP ♻️",
                                  url="t.me/firefoxbot?startgroup=true"),
]]

buttons += [[InlineKeyboardButton(text="SOURCE CODE 💫",
                                  url="https://github.com/momskidvaava/firefoxbot"),
             InlineKeyboardButton(text="SUPPORT🌳",
                                  url="https://t.me/my_botfamily"),
]]

buttons += [[InlineKeyboardButton(text="☘ CLOSE THE MENU ☘",
                                  callback_data="close_menu")]]

IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []
CHAT_SETTINGS = {}
USER_SETTINGS = {}

GDPR = []

        
            update.effective_message.reply_text(
                PM_START_TEXT,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                disable_web_page_preview=False,
            )
    else:
        update.effective_message.reply_text("Heya, 乂🖤⃝ƛԼƛƝƘƦƖƬӇƛ⃟🦋࿐ Here, How can I help you? 🙂")




def send_start(update, context):
    # Try to remove old message
    try:
        query = update.callback_query
        query.message.delete()
    except BaseException:
        pass

    chat = update.effective_chat  # type: Optional[Chat]
    first_name = update.effective_user.first_name
    text = PM_START_TEXT
 
    buttons += [[InlineKeyboardButton(text="Close the Menu ☘",
                                  callback_data="close_menu")]]


    update.effective_message.reply_text(
        PM_START_TEXT,
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode=ParseMode.MARKDOWN,
        timeout=60,
        disable_web_page_preview=False,
    )


def start_stop(update, context):
    # Try to remove old message
    try:
        query = update.callback_query
        query.message.delete()
    except BaseException:
        pass

    chat = update.effective_chat  # type: Optional[Chat]
    first_name = update.effective_user.first_name
    text = "The menu is closed 🍁"
    buttons = [[InlineKeyboardButton(text="Reopen Menu 🍁",
                                     callback_data="bot_start")]]

    update.effective_message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode=ParseMode.MARKDOWN,
        timeout=60,
        disable_web_page_preview=False,
    )


def error_handler(update, context):
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if
    # something breaks.
    LOGGER.error(msg="Exception while handling an update:",
                 exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them
    # together.
    tb_list = traceback.format_exception(None, context.error,
                                         context.error.__traceback__)
    tb = "".join(tb_list)

    # Build the message with some markup and additional information about what
    # happened.
    message = ("An exception was raised while handling an update\n"
               "<pre>update = {}</pre>\n\n"
               "<pre>{}</pre>").format(
                   html.escape(
                       json.dumps(update.to_dict(),
    if WEBHOOK:
        LOGGER.info("Using webhooks.")
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)

        if CERT_PATH:
            updater.bot.set_webhook(
                url=URL + TOKEN,
                certificate=open(
                    CERT_PATH,
                    "rb"))
        else:
            updater.bot.set_webhook(url=URL + TOKEN)
            client.run_until_disconnected()

    else:
        LOGGER.info("Using long polling.")
        updater.start_polling(timeout=15, read_latency=4)
        updater.bot.send_message(
            chat_id=MESSAGE_DUMP,
            text="Elizabeth Started...")
        client.run_until_disconnected()

    updater.idle()


if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    client.start(bot_token=TOKEN)
    main()
