# -*- coding: utf-8 -*-

import re

from dataclasses import dataclass, field
from typing import NoReturn, Text, List, Callable

from constants.regex import (REGEX_MONTH_PAYMENT, REGEX_MONTH_ISSUED_ON,
                REGEX_CPF, REGEX_SERVER_SITUATION, REGEX_SERVER_ORGAN,
                REGEX_SERVER_NAME, REGEX_LEGAL_REGULATIONS,
                REGEX_PAYING_UNID, REGEX_BANK_DATA, REGEX_INCOME)

@dataclass(init=True, repr=False)
class Regex:

  def __init__(self, logger: Callable) -> NoReturn:
    self.discount_rubrics = ["EMPRESTIMO", "EMPREST", "CARTAO CREDITO"]
    self.logger = logger

  def regex_month_payment(self, string: Text) -> Text:
    try:
      search = re.search(REGEX_MONTH_PAYMENT, string)
      return search.group() if search and len(search.group()) == 7 else None
    except Exception as error:
      self.logger.error(f"Error general exception to apply the REGEX looking for month payment - {error}...")

  def regex_month_issued_on(self, string: Text) -> Text:
    try:
      search = re.search(REGEX_MONTH_ISSUED_ON, string)
      return search.group() if search and len(search.group()) == 9 else None
    except Exception as error:
      self.logger.error(f"Error general exception to apply the REGEX looking for month issued on - {error}...")

  def regex_cpf(self, string: Text) -> Text:
    try:
      search = re.search(REGEX_CPF, string)
      return search.group() if search else None
    except Exception as error:
      self.logger.error(f"Error general exception to apply the REGEX looking for CPF - {error}...")

  def regex_server_situation(self, string: Text) -> Text:
    try:
      search = re.search(REGEX_SERVER_SITUATION, string)
      return re.sub("\n", "", search.group().split(":")[-1].lstrip()) if search else None
    except Exception as error:
      self.logger.error(f"Error general exception to apply the REGEX looking for server situation - {error}...")

  def regex_server_organ(self, string: Text) -> Text:
    try:
      split = string.split("ORGAO")[1].split("\n")[1]
      search = re.search(REGEX_SERVER_ORGAN, split)
      return search.group()[2::] if search else None
    except Exception as error:
      self.logger.error(f"Error general exception to apply the REGEX looking for server organ - {error}...")

  def regex_server_name(self, string: Text) -> Text:
    try:
      search = re.search(REGEX_SERVER_NAME, re.sub("\n", "", string))
      return search.group().strip() if search else None
    except Exception as error:
      self.logger.error(f"Error general exception to apply the REGEX looking for server name - {error}...")

  def regex_legal_regulations(self, string: Text) -> Text:
    try:
      search = re.search(REGEX_LEGAL_REGULATIONS, string)
      return re.sub("\n", "", search.group().split(":")[-1].lstrip()) if search else None
    except Exception as error:
      self.logger.error(f"Error general exception to apply the REGEX looking for legal regulations - {error}...")

  def regex_paying_unid(self, string: Text) -> Text:
    try:
      search = re.search(REGEX_PAYING_UNID, string)
      return re.sub("\n", "", search.group().split(":")[-1].lstrip()) if search else None
    except Exception as error:
      self.logger.error(f"Error general exception to apply the REGEX looking for paying unid - {error}...")

  def regex_bank_data(self, string: Text, index=0) -> Text:
    try:
      if index > 2:
        self.logger.error("Index error - We need a real index to extract the bank.")
      search = re.search(REGEX_BANK_DATA, string)
      return search.group().split(" ")[index] if search else None
    except Exception as error:
      self.logger.error(f"Error general exception to apply the REGEX looking for bank data - {error}...")

  def regex_mat_siape(self, string: Text, index=0) -> Text:
    try:
      if index > 1:
        self.logger.error("Index error - We need a real index - 0 or 1 - to extract the server mat/siape.")
      return re.split(r"\n", string)[1].split(" ")[index]
    except Exception as error:
      self.logger.error(f"Error general exception to apply the REGEX looking for mat/siape - {error}...")

  def regex_income(self, string: Text) -> List:
    try:
      index = [elemento for elemento in [string.find(elemento) for elemento in self.discount_rubrics] if elemento > 0]
      split = re.split(REGEX_INCOME, string[index[0]::])
      description = [value.replace("\n", " ").strip().split(" ")
                      for value in split if sum([value.count(elemento)
                        for elemento in self.discount_rubrics]) > 0]
      result = [" ".join(description[0])] if len(description) == 1 else ([" ".join(description[0])] +
                  [elemento for elemento in [" ".join(elemento[2::])
                    for elemento in description[1::]]])
      return [[" ".join(elemento[0:len(elemento) - 2]), elemento[-1], elemento[-2]]
                for elemento in [elemento.split(" ") for elemento in result]]
    except Exception as error:
      self.logger.error(f"Error general exception to apply the REGEX looking for income - {error}...")

  def regex_money_income(self, string: Text):
    try:
      index = [elemento for elemento in [string.find(elemento) for elemento in self.discount_rubrics] if elemento > 0]
      result, temp = [elemento for elemento in string[index[0]::].split("\n") if not elemento.isdigit()], list()
      for index, elemento in enumerate(result):
        temp.append(elemento.count("EMPRESTIMO") or elemento.count("EMPREST") or elemento.count("CARTAO CREDITO"))
      return [result[index + 1] for index, value in enumerate(temp) if value and index < len(temp)]
    except Exception as error:
      self.logger.error(f"Error general exception to apply the REGEX looking for money income - {error}...")
