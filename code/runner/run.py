# -*- coding: utf-8 -*-

import threading
import xlsxwriter
import multiprocessing as mp
from typing import NoReturn, Any
from multiprocessing import Pool
from timeit import default_timer as timer

import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

from tools.os import OS

from core.regex import Regex

from utils.merge import Merge

from core.excel import Excel
from core.extract import Extract
from core.converter import ConverterPDF

from settings.log import Log
from settings.cli import CLIArguments
from settings.config import Config

from bot.telegram import TelegramBot

# ==============================================================================
# GLOBAL
# ==============================================================================

config, args, cores, os = Config(), CLIArguments().args, mp.cpu_count(), OS()

path = args["path"] if args["path"] else (config.get_env("PDF_PATH") if config.get_env("PDF_PATH") else "/usr/src/code/files")
number = int(args["number"] if args["number"] else (config.get_env("EXCEL_NUMBER") if config.get_env("EXCEL_NUMBER") else 20))

telegram_token = args["token"] if args["token"] else (config.get_env("TELEGRAM_TOKEN") if config.get_env("TELEGRAM_TOKEN") else None)
bot = args["bot"] if args["bot"] else False

log_path = config.get_env("LOG_PATH") if config.get_env("LOG_PATH") else "/var/log/code"
log_file = config.get_env("LOG_FILE") if config.get_env("LOG_FILE") else "file.log"
log_level = config.get_env("LOG_LEVEL") if config.get_env("LOG_LEVEL") else "DEBUG"
logger_name = config.get_env("LOGGER_NAME") if config.get_env("LOGGER_NAME") else "Code"
logger = Log(log_path, log_file, log_level, logger_name).logger

regex, extract, excel, merge = Regex(logger), Extract(logger), Excel(logger), Merge(path, logger)

if os.check_if_dir_empty(path):
  raise Exception("Empty PDF Directory...")

pdfs = os.list_all_files_in_directory_orded_by_size(path, ".pdf")
txts = os.list_all_files_in_directory_orded_by_size(path, ".txt")
excels = os.list_all_files_in_directory_orded_by_size(path, ".xlsx")

# ==============================================================================
# FUNCTIONS
# ==============================================================================

def run_convertion() -> NoReturn:
  converter, start = ConverterPDF(logger), timer()
  logger.info(f"Number of cores - {cores}\n")
  with Pool(cores) as pool:
    for file, _ in enumerate(pool.imap_unordered(converter.convert, pdfs)):
      logger.info(f"Completed file - {file}\n")
  print("\nJust %0.4f seconds elapsed to parsing this PDF to text.\n" % (timer() - start))

# ==============================================================================

def run_extract() -> NoReturn:
  start = timer()
  for txt in txts:
    txt_information, excel_file = os.read(txt, strategy="string"), txt.replace(".txt",".xlsx")
    if not os.check_if_is_file(excel_file) or os.check_if_file_is_empty(excel_file):
      head_result, information_result = extract.filter_all_information_head_page(txt_information), extract.filter_all_information_below_head(txt_information)
      first_union = [head_result[index] + value for index, value in enumerate(information_result)]
      moneys, rubrics = extract.filter_money_income(txt_information), extract.filter_income(txt_information)
      concat, middle_union = list(zip(moneys, rubrics)), list()
      for elemento in concat:
        moneys, rubrics = elemento[0], elemento[1]
        for pos, value in enumerate(rubrics):
          value.append(moneys[pos])
        middle_union.append(rubrics)
      finish = [rubric + elemento[0] for index, elemento in enumerate(list(zip(first_union, middle_union))) for rubric in elemento[1]]
      last_union = [[elemento[4] if elemento[4] else "-",
                      elemento[5] if elemento[5] else "-",
                      elemento[6] if elemento[6] else "-",
                      elemento[12] if elemento[12] else "-",
                      elemento[8] if elemento[8] else "-",
                      elemento[7] if elemento[7] else "-",
                      elemento[9] if elemento[9] else "-",
                      elemento[10] if elemento[10] else "-",
                      elemento[11] if elemento[11] else "-",
                      elemento[0] if elemento[0] else "-",
                      elemento[1] if elemento[1] else "-",
                      elemento[3] if elemento[3] else "-"] for elemento in finish]
      excel.generate(excel_file, last_union)
    else:
      print(f"\nThe excel {excel_file} alredy exist in the System...\n")
      continue
  print("Just %0.4f seconds elapsed to extracting all informatio.\n" % (timer() - start))

# ==============================================================================

def run_merge() -> NoReturn:
  start = timer()
  merge.apply(excels, number)
  print("\nJust %0.4f seconds elapsed to merging the Excel files.\n" % (timer() - start))

# ==============================================================================

def run_bot():
  telegram = TelegramBot(telegram_token, logger)
  telegram.main()

# ==============================================================================

def run() -> NoReturn:
  cprint(figlet_format("Extracon", font="starwars"), "white", attrs=["dark"])
  run = threading.Thread(target=run_bot)
  run.start()
  run_convertion()
  run_extract()
  run_merge()
