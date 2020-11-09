# -*- coding: utf-8 -*-

import xlsxwriter
from dataclasses import dataclass, field
from typing import NoReturn, Text, List, Callable

@dataclass(init=True, repr=True)
class Excel:
  logger: Callable = field(init=True, repr=False)

  COLUMNS = ["A1", "B1", "C1",
    "D1", "E1", "F1", "G1", "H1", "I1", "J1", "K1", "L1"]
  NAMES = ["ORGAO", "MES",
    "SITUACAO", "MATRICULA","NOME", "CPF", "BANCO", "AGENCIA", "CC",
    "DESCRICAO", "PRAZO", "VALOR"]

  def _create_excel(self, excel_file: Text) -> NoReturn:
    self.logger.info(f"Creating Excel {excel_file}...")
    workbook = xlsxwriter.Workbook(excel_file)
    worksheet, bold = workbook.add_worksheet("CONVERTION"), workbook.add_format({"bold": True})
    for column, name in zip(self.COLUMNS, self.NAMES):
      worksheet.write(column, name, bold)
    return workbook, worksheet

  def _populate_excel(self, worksheet: Callable, information: List) -> NoReturn:
    self.logger.info(f"Populate Excel...")
    row, col = 1, 0
    for a, b, c, d, e, f, g, h, i, j, k, l in information:
      worksheet.write(row, col, a)
      worksheet.write(row, col + 1, b)
      worksheet.write(row, col + 2, c)
      worksheet.write(row, col + 3, d)
      worksheet.write(row, col + 4, e)
      worksheet.write(row, col + 5, f)
      worksheet.write(row, col + 6, g)
      worksheet.write(row, col + 7, h)
      worksheet.write(row, col + 8, i)
      worksheet.write(row, col + 9, j)
      worksheet.write(row, col + 10, k)
      worksheet.write(row, col + 11, l)
      row += 1

  def generate(self, excel_file: Text, information: List) -> NoReturn:
    if not isinstance(information, list):
      self.logger.error(f"We expect a list type as a parameter not {type(information)}...")
    try:
      workbook, worksheet = self._create_excel(excel_file)
      self._populate_excel(worksheet, information)
      workbook.close()
    except Exception as error:
      self.logger.error(f"Error general exception Excel file creation {excel_file} - {error}...")
