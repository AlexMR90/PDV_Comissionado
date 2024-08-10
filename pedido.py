
#importações
from cliente import Cliente
from vendedor import Vendedor
from itemVenda import ItemVenda

class Pedido():

  #variáveis / atributos
  __cliente = cliente
  __vendedor = vendedor
  self.__itens = []

  #inicializador
  def __init__(self,cliente,vendedor,itens)
    self.cliente = cliente
    self.vendedor = vendedor
    self.itens = []

  #encapsulamento
  @property
  def cliente(self):
    return cliente

  @property
  def vendedor(self):
    return vendedor

  @property
  def itens(self):
    return itens

  #setters
  @cliente.setter
  def cliente(self,cliente)
    self.__cliente = cliente

  @cliente.setter
  def vendedor(self,vendedor)
    self.__vendedor = vendedor

  @cliente.setter
  def itens(self,itens)
    self.__itens = itens

  def calcularValorTotalPedido():
    valorTotal = 0
    for i in itens:
      valorTotal = valorTotal  + itens.calcularValorTotalItem()
    return valorTotal

  def calcularComissaoPedido():
    return calcularValorTotalPedido() * vendedor.PercentualComissao()

  
    
    
  
