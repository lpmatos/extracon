# -*- coding: utf-8 -*-

from operator import itemgetter
from os import path, makedirs, stat, listdir
from typing import NoReturn, Text, List, Any

class OS:

  def __init__(self) -> NoReturn:
    self.extensions = [".txt", ".pdf", ".xlsx"]

  @classmethod
  def check_if_dir_exists(cls, directory: Text) -> bool:
    return True if path.exists(directory) else False

  @classmethod
  def check_if_is_dir(cls, directory: Text) -> bool:
    return True if path.isdir(directory) else False

  @classmethod
  def check_if_is_file(cls, file: Text) -> bool:
    return True if path.isfile(file) else False

  @classmethod
  def check_if_file_is_empty(cls, file: Text) -> bool:
    return True if stat(file).st_size == 0 else False

  @classmethod
  def join_directory_with_file(cls, directory: Text, file: Text) -> Text:
    return str(path.join(directory, file))

  @classmethod
  def create_directory(cls, directory: Text) -> NoReturn:
    try:
      makedirs(directory)
    except OSError:
      print(f"OSError in create the directory {directory}")

  @classmethod
  def create_file(cls, file: Text) -> NoReturn:
      with open(file, mode="w"): pass

  def check_if_path_and_file_exist(self, directory: Text, file: Text, creation=True) -> NoReturn:
    if self.check_if_is_dir(directory):
      if not self.check_if_is_file(file):
        if creation:
          self.create_file(file)
        else:
          raise Exception(f"File {file} not exist")
    else:
      self.create_directory(directory)
      self.create_file(file)

  def check_if_dir_empty(self, directory: Text) -> bool:
    return True if len(self.list_all_directory(directory)) == 0 else False

  def list_all_directory(self, directory: Text) -> List:
    return listdir(directory) if self.check_if_is_dir(directory) else []

  def list_all_files_in_directory(self, directory: Text, extension=".txt") -> List:
    list_directory, is_dir = self.list_all_directory(directory), self.check_if_is_dir(directory)
    files = [self.join_directory_with_file(directory, file) for file in list_directory
              if self.check_if_is_file(self.join_directory_with_file(directory, file))] if is_dir else []
    return [self.join_directory_with_file(directory, file) for file in files if file.endswith(extension)] if extension in self.extensions else None

  def list_all_files_in_directory_orded_by_size(self, directory: Text, extension=".txt") -> List:
    list_directory = self.list_all_files_in_directory(directory, extension)
    return [self.join_directory_with_file(directory, file[0])
              for file in sorted([(file, path.getsize(self.join_directory_with_file(directory, file))/1024)
                  for file in list_directory], key=itemgetter(1), reverse=True)][::-1]

  def read(self, path: Text, strategy="string") -> Any:
    with open(path, mode="r", encoding="utf-8") as file:
      if strategy == "string":
        return file.read()
      elif strategy == "list":
        return file.readlines()
      else:
        raise Exception("This strategy isn't accept - We have string/list strategy.")
