class Produto():
  #variáveis / atributo
  __codigo:int
  __nome:str
  __estoque:int
  __valor:float

  #inicializador
  def __init__(self,codigo,nome,estoque,valor):
    self.codigo = codigo
    self.nome = nome
    self.estoque = estoque
    self.valor = valor

  #encapsulamento
  @property
  def codigo(self):
    return codigo
  @property
  def nome(self):
    return nome
  @property
  def estoque(self):
    return estoque
  @property
  def valor(self):
    return valor

  #setters
  @codigo.setter
  def codigo(self,codigo):
    self.__codigo = int(codigo)
    
  @nome.setter
  def nome(self,nome):
    self.__nome = nome

  @estoque.setter
  def estoque(self,estoque):
    self.__estoque = int(estoque)

  @valor.setter
  def valor(self,valor):
    self.__valor = float(valor)

  #métodos / funções
  def entrada_estoque(int:quantidade):
    estoque += int(quantidade)

  def saida_estoque(int:quantidade):
    estoque -= int(quantidade)
    
