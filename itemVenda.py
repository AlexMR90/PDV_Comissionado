#importações
from produto import Produto

class ItemVenda():
  #variáveis / atributos
  __quantidade:int
  __produto = Produto

  #inicializador
  #def __init__(self, quantidade,produto):
    self.quantidade = quantidade
    self.produto = produto

  #encapsulamento
  @property
  def quantidade(self):
    return quantidade

  @property
  def produto(self):
    return produto

  #setters

  @quantidade.setter
  def quantidade(self,quantidade):
    self.__quantidade = int(quantidade)

  @produto.setter
  def produto(self,produto):
    self.__produto = produto

  #métodos / funções
  def calcularValorTotalItem():
    return quantidade * produto.valor
