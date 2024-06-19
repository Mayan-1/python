from config.db_config import *

class Instituicao(Model):
  nome = CharField()
  endereco = CharField(unique=True)

  class Meta:
    database = db
