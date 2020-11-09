import datetime
from typing import Text, NoReturn

class Greeting:

  def __init__(self) -> NoReturn:
    self.hour = int(datetime.datetime.now().time().hour)

  def get(self) -> Text:
    if self.hour >= 6 and self.hour <= 12:
      return "Bom dia"
    elif self.hour > 12 and self.hour <= 18:
      return "Boa tarde"
    else:
      return "Boa noite"
