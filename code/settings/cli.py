# -*- coding: utf-8 -*-

from typing import NoReturn, Text
from argparse import ArgumentParser, RawTextHelpFormatter, ArgumentError

from constants.general import CLI

class CLIArguments:

  def __init__(self) -> NoReturn:
    self._parser = self._create_parser_object()
    self._adding_arguments()
    self.args = vars(self._parser.parse_args())

  @staticmethod
  def _create_parser_object() -> ArgumentParser:
    try:
      return ArgumentParser(
        description="Extracon - convert all PDF files to Excel getting some informations",
        prog="extracon",
        epilog=CLI,
        formatter_class=RawTextHelpFormatter)
    except ArgumentError as error:
      print(f"Error when we create a parser object - {error}")

  def _adding_arguments(self) -> NoReturn:
    self._parser.add_argument("-p", "--path",
                                type=str,
                                metavar="<path>",
                                default=None,
                                help="PDF Path")
    self._parser.add_argument("-t", "--token",
                                type=str,
                                metavar="<token>",
                                default=None,
                                help="Telegram Token")
    self._parser.add_argument("-bot", "--bot",
                                action="store_true",
                                required=False,
                                default=False,
                                dest="bot",
                                help="Enable Bot Telegram")
    self._parser.add_argument("-number", "--number",
                                action="store",
                                required=False,
                                dest="number",
                                help="Number of Excel Files that we will generate in final process")
    self._parser.add_argument("-v", "--version",
                                action="store_true",
                                help="Show Extracon version")
