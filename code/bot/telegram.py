# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import NoReturn, Text, Callable

from telegram import Update
from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

from bot.commands import Commands

@dataclass(init=True, repr=True)
class TelegramBot(Commands):
  token: str = field(init=True, repr=True)
  logger: Callable = field(init=True, repr=False)

  def error(self, update: Update, context: CallbackContext):
    self.logger.warning(f"Update {update} caused error - {context.error}")

  def main(self) -> NoReturn:
    updater = Updater(token=self.token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", self.start))
    dispatcher.add_handler(CommandHandler("about", self.about))
    dispatcher.add_handler(CommandHandler("info", self.info))
    dispatcher.add_handler(CommandHandler("contact", self.contact))
    dispatcher.add_handler(CommandHandler("dev", self.dev))
    dispatcher.add_handler(CommandHandler("menu", self.menu))
    dispatcher.add_handler(CallbackQueryHandler(self.button_menu))
    dispatcher.add_handler(CommandHandler("help", self.help))
    dispatcher.add_handler(MessageHandler(Filters.command, self.unknown))
    dispatcher.add_error_handler(self.error)
    updater.start_polling()
    updater.idle()
