from config.db_config import db
from models.instituicao import Instituicao

db.connect()

db.create_tables([Instituicao])

db.close()


