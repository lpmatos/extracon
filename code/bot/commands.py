# -*- coding: utf-8 -*-

import glob
import time
from typing import NoReturn

from telegram import Update
from telegram.ext.dispatcher import run_async
from telegram.ext import CallbackContext, CallbackQueryHandler

from utils.greeting import Greeting
from bot.keyboards import Keyboards
from constants.bot import START, ABOUT, CONTACT, DEV, MENU, HELP, UNKNOWN

class Commands(Keyboards):

  @run_async
  def start(self, update: Update, context: CallbackContext) -> NoReturn:
    bot, username, greeting = context.bot, update.message.from_user.first_name, Greeting()
    message_start = START % (username, greeting.get())
    bot.send_message(chat_id=update.message.chat.id, text=message_start)

  @run_async
  def about(self, update: Update, context: CallbackContext) -> NoReturn:
    bot = context.bot
    bot.send_message(chat_id=update.message.chat.id, text=ABOUT)

  @run_async
  def info(self, update: Update, context: CallbackContext) -> NoReturn:
    bot = context.bot
    try:
      path = "/usr/src/code/files"
      all_files = glob.glob(f"{path}/*")
      txt_files = glob.glob(f"{path}/*.txt")
      pdf_files = glob.glob(f"{path}/*.pdf")
      excel_files = glob.glob(f"{path}/*.xlsx")
    except Exception as error:
      print(error)
    information = f"""
🧾 Informações sobre o processo de conversão:

📌 Total de arquivos no diretório {path}: {len(all_files)}

📌 Total de arquivos PDF: {len(pdf_files)} arquivos.
📌 Total de arquivos TXT: {len(txt_files)} arquivos.
📌 Total de arquivos EXCEL: {len(excel_files)} arquivos.

📌 Diferença PDF - TXT: {len(pdf_files) - len(txt_files)} arquivos.
📌 Diferença PDF - EXCEL: {len(pdf_files) - len(excel_files)} arquivos.

📌 Porcentagem de arquivos PDF já convertidos para TXT: {round((len(txt_files)  / len(pdf_files)) * 100, 2)} %.
📌 Porcentagem de arquivos PDF já convertidos para EXCEL: {round((len(excel_files)  / len(pdf_files)) * 100, 2)} %.

Data Atualização: {time.strftime("%H:%M:%S", time.localtime())}.
"""
    bot.send_message(chat_id=update.message.chat.id, text=information)

  @run_async
  def contact(self, update: Update, context: CallbackContext) -> NoReturn:
    bot = context.bot
    bot.send_message(chat_id=update.message.chat_id, text=CONTACT)

  @run_async
  def dev(self, update: Update, context: CallbackContext) -> NoReturn:
    bot = context.bot
    bot.send_message(chat_id=update.message.chat_id, text=DEV)

  def menu(self, update: Update, context: CallbackContext) -> NoReturn:
    keyboard_markup = self.menu_keyboard()
    update.message.reply_text(text=MENU, reply_markup=keyboard_markup)

  def button_menu(self, update: Update, context: CallbackContext) -> NoReturn:
    query, bot = update.callback_query, context.bot
    query.answer()
    data = int(query.data)
    message = ABOUT if data == 0 else (CONTACT if data == 1
      else (DEV if data == 2 else UNKNOWN))
    bot.send_message(chat_id=query.message.chat_id,
      message_id=query.message.message_id, text=message)

  @run_async
  def help(self, update: Update, context: CallbackContext) -> NoReturn:
    bot = context.bot
    bot.send_message(chat_id=update.message.chat.id, text=HELP)

  @run_async
  def unknown(self, update: Update, context: CallbackContext) -> NoReturn:
    bot = context.bot
    bot.send_message(chat_id=update.message.chat_id, text=UNKNOWN)
