# -*- coding: utf-8 -*-

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class Keyboards():

  @staticmethod
  def menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [[InlineKeyboardButton("🌐 About", callback_data="0"),
                InlineKeyboardButton("📞 Contact", callback_data="1")],
                [InlineKeyboardButton("💻 Dev", callback_data="2")]]
    return InlineKeyboardMarkup(keyboard)
