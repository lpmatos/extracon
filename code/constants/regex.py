# ==============================================================================
# REGEX USED IN THIS APPLICATION
# ==============================================================================

REGEX_MONTH_PAYMENT = r"[JANFEVRBIULGOSTDZ]{3}\d{4}"
REGEX_MONTH_ISSUED_ON = r"\d{2}[JANFEVRBIULGOSTDZ]{3}\d{4}"

REGEX_CPF = r"\d{9}-\d{2}"

REGEX_SERVER_SITUATION = r"[SITUACO]{8}\s[SERVIDO:]{8}:\s[A-Z\s]+"
REGEX_SERVER_ORGAN = r":\s[\w\s\.\-\,]+"
REGEX_SERVER_NAME = r"[A-Z]+\s[A-Z\s]+"

REGEX_LEGAL_REGULATIONS = r"[REG]{3}.[JURDICO]{8}:\s[A-Z]+"

REGEX_PAYING_UNID = r"[UNID]{4}.[PAGDOR]{8}\s:\s[\w-]+"

REGEX_BANK_DATA = r"\d{3}\s\d{5}-[\dX]{1}\s[\dX\-]+"

REGEX_INCOME = r"[\d\.]+\,[\d]+"
