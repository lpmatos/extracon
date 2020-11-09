# -*- coding: utf-8 -*-

import re
from typing import NoReturn, Text, List, Callable

from core.regex import Regex

class Extract(Regex):

  def __init__(self, logger: Callable) -> NoReturn:
    self.logger = logger
    super().__init__(logger)

  def filter_people_per_page_and_rubric(self, txt_information: Text) -> List:
    try:
      self.logger.info(f"Filter people per page and Rubrics...")
      return[(page[0], pessoa) for page in [re.split(r"[-]{132}", page)
              for page in re.split(r"PAGINA", re.sub(r"\s\s+", "\n", txt_information))]
                  for pessoa in page if sum([pessoa.count(elemento)
                      for elemento in self.discount_rubrics]) > 0]
    except Exception as error:
      self.logger.error(f"Error general exception in filter people per page and rubric - {error}...")

  def filter_head_page(self, txt_information: Text) -> List:
    try:
      self.logger.info(f"Filter head page...")
      return [head[0] for head in self.filter_people_per_page_and_rubric(txt_information)]
    except Exception as error:
      self.logger.error(f"Error general exception in filter the head of a page - {error}...")

  def filter_below_head(self, txt_information: Text) -> List:
    try:
      self.logger.info(f"Filter below head page...")
      return [information[1].split("TOTAL RENDIMENTOS")[0].replace("*** CONTINUA ...", "")
              .replace("SIAPE - SISTEMA INTEGRADO DE ADMINISTRACAO DE RECURSOS HUMANOS", "")
              for information in self.filter_people_per_page_and_rubric(txt_information)]
    except Exception as error:
      self.logger.error(f"Error general exception in filter everything below the head of a page - {error}...")

  def filter_all_information_head_page(self, txt_information: Text) -> List:
    try:
      self.logger.info(f"Filter all information in head page...")
      return [[self.regex_server_organ(value),
              self.regex_month_payment(value),
              self.regex_server_situation(value)] for value in self.filter_head_page(txt_information)]
    except Exception as error:
      self.logger.error(f"Error general exception in filter all information of head page - {error}...")

  def filter_all_information_below_head(self, txt_information: Text) -> List:
    try:
      self.logger.info(f"Filter all information below head page...")
      return [[self.regex_cpf(value),
              self.regex_server_name(value),
              self.regex_bank_data(value, index=0),
              self.regex_bank_data(value, index=1),
              self.regex_bank_data(value, index=2),
              self.regex_mat_siape(value)] for value in self.filter_below_head(txt_information)]
    except Exception as error:
      self.logger.error(f"Error general exception in filter all information below head - {error}...")

  def filter_money_income(self, txt_information: Text) -> List:
    try:
      return [self.regex_money_income(elemento) for elemento in self.filter_below_head(txt_information)]
    except Exception as error:
      self.logger.error(f"Error general exception in filter money income - {error}...")

  def filter_income(self, txt_information: Text) -> List:
    try:
      return [self.regex_income(elemento) for elemento in self.filter_below_head(txt_information)]
    except Exception as error:
      self.logger.error(f"Error general exception in filter income - {error}...")
