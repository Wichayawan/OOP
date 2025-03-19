from contract import Contract
from emailsender import MailSender

class EmailableContract(Contract, MailSender):
    pass