# -*- coding: utf-8 -*-

import subprocess
from typing import Text, Callable
from dataclasses import dataclass, field

@dataclass(init=True, repr=False)
class Process:
  logger: Callable = field(init=True, repr=False)

  def run_command(self, command: Text) -> Text:
    try:
      if not isinstance(command, str):
        raise ValueError(f"We spec a string value, not {type(command)}")
      process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
      output, errors = process.communicate()
      if process.returncode != 0:
        self.logger.error(f"Run command failed - status returncode - {process.returncode} - {error}")
      return (output, errors)
    except subprocess.CalledProcessError as error:
      self.logger.error(f"Subprocess error when run the command {command} - {error}")
    except Exception as error:
      self.logger.error(f"Error general exception in run the command {command} - {error}")
