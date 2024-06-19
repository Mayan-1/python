from interfaces.i_instituicao_repository import IInstituicaoRepository
from models.instituicao import Instituicao

class InstituicaoRepository(IInstituicaoRepository):
  def __init__(self):
    super()
    

  def criar(self, nome, endereco):
    Instituicao.create(nome=nome, endereco=endereco)
    

    
