class IInstituicaoRepository:
  def __init__(self):
    raise Exception("Não é possível, instanciar uma interface")
  
  def criar(self, instituicao):
    raise Exception("Esse método não pode ser chamado")
  
  def ler(self, id):
    raise Exception("Esse método não pode ser chamado")
  
  def ler_todos(self):
    raise Exception("Esse método não pode ser chamado")
  
  def atualizar(self):
    raise Exception("Esse método não pode ser chamado")
  
  def excluir(self):
    raise Exception("Esse método não pode ser chamado")