# -*- coding: utf-8 -*-

import datetime
import pandas as pd
from tqdm import tqdm
from dataclasses import dataclass, field
from typing import List, NoReturn, Callable

from tools.os import OS
from tools.partition import Partition

@dataclass(init=True, repr=False)
class Merge(OS):
  path: str = field(init=True, repr=False)
  logger: Callable = field(init=True, repr=False)

  def apply(self, excels: List, number: int) -> NoReturn:
    if len(excels) == 0 or not excels:
      self.logger.error("No merge excels...")
    self.logger.debug(f"Apply merge: {len(excels)} excels - {number} excels")
    partition = Partition(self.logger).apply(excels, number)
    print(excels)
    pbar, info = tqdm(partition), str(datetime.datetime.now()).split(" ")[0].replace("-", "_")
    try:
      for index, value in enumerate(pbar, start=1):
        output = f"EXCEL_MERGED_{info}_{index}.xlsx"
        file = self.join_directory_with_file(self.path, output)
        if self.check_if_is_file(file):
          self.logger.warning(f"\nThe fiel {file} alredy exist in the system...")
          continue
        self.logger.info(f"Convertion in index - {index}...")
        excels = [pd.ExcelFile(excel) for excel in value]
        frames = [elemento.parse(elemento.sheet_names[0], header=None, index_col=None) for elemento in excels]
        frames[1:] = [df[1:] for df in frames[1:]]
        combined = pd.concat(frames)
        self.logger.info(f"Creating the Excel file {output}...")
        combined.to_excel(file, header=False, index=False)
        pbar.set_description(f"Doing Interpreter Page - {index}.")
    except Exception as error:
      self.logger.error(f"Error general exception when we loop the partition list to build the merge - {error}...")
