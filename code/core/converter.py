# -*- coding: utf-8 -*-

import sys
from tqdm import tqdm
from dataclasses import dataclass, field
from typing import NoReturn, Text, MutableSet, Callable

if sys.version_info > (3, 0):
  from io import StringIO
else:
  from io import BytesIO as StringIO

from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

from tools.os import OS

@dataclass(init=True, repr=True)
class ConverterPDF(OS):
  logger: Callable = field(init=True, repr=False)

  def _get_pages_data_pdf_miner(self, pdf_file: Text, pagenums: MutableSet) -> PDFPage.get_pages:
    try:
      self.logger.info(f"Getting pages data from {pdf_file} based in PDF miner...")
      return PDFPage.get_pages(pdf_file, pagenums, maxpages=0, password="", caching=True, check_extractable=False)
    except Exception as error:
      self.logger.error(f"Error general exception in get pages from {pdf_file} based in PDF miner - {error}...")

  def convert(self, pdf_file: Text) -> NoReturn:
    try:
      encoding, txt_file, output, pagenums = "utf-8", pdf_file.replace(".pdf", ".txt"), StringIO(), set()
      self.logger.info(f"1 - Convert {pdf_file} to a TXT file.")
      if not self.check_if_is_file(txt_file) or self.check_if_file_is_empty(txt_file):
        self.logger.info(f"2 - Create TXT file {txt_file}.")
        with open(txt_file, "w"): pass
        rsrcmgr, laparams = PDFResourceManager(), LAParams(all_texts=False)
        text_converter = TextConverter(rsrcmgr, output, codec=encoding, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, text_converter)
        pdf_file = open(pdf_file, "rb")
        pages_data = self._get_pages_data_pdf_miner(pdf_file, pagenums)
        pbar = tqdm(pages_data)
        for value, page in enumerate(pbar):
          interpreter.process_page(page)
          pbar.set_description(f"Doing Interpreter Page - {value}.")
        pdf_file.close()
        text = output.getvalue()
        text_converter.close()
        output.close()
        self.logger.info(f"3 - Write the information in {txt_file}.")
        with open(txt_file, "w") as file:
          file.write(text)
      else:
        self.logger.warning(f"The file {txt_file} alredy exist and isn't empty...")
    except Exception as error:
      self.logger.error(f"Error general exception in convert the information from {pdf_file} - PDF to TXT - {error}...")
