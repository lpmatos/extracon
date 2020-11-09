# -*- coding: utf-8 -*-

from typing import List, Callable
from dataclasses import dataclass, field

@dataclass(init=True, repr=False)
class Partition:
  logger: Callable = field(init=True, repr=False)

  def apply(self, information: List, number: int) -> List:
    if number <= 1 and number > 10:
      self.logger.error("Limit partition exceeded. We need a value between 2 - 10...")
    if not isinstance(information, list):
      self.logger.error(f"We expect a list type as a parameter not {type(information)}...")
    try:
      value, other = divmod(len(information), number)
      indices = [(value * elemento) + min(elemento, other) for elemento in range(number + 1)]
    except Exception as error:
      self.logger.error(f"Error apply partition - {error}")
      return []
    else:
      return [information[indices[elemento]:indices[elemento + 1]] for elemento in range(number)]
