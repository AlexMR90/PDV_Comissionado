Class Cliente():
  #variáveis / atributos
  __codigo:int
  __nome:str
  __endereco:str
  
  #inicializador
  def __init__(self,codigo,nome,endereco):
    self.codigo = codigo
    self.nome = nome
    self.endereco = endereco

  #encapsulamento
  @property
  def codigo(self):
    return self.__codigo
  @property
  def nome(self):
    return self.__nome
  @property
  def endereco(self):
    return self.__endereco

  #setters
  @codigo.setter
  def codigo(self,codigo):
    self.__codigo = int(codigo)
  @nome.setter
  def nome(self,nome):
    self.__nome = nome
  @endereco.setter
  def endeereco(self,endereco):
    self.__endereco = endereco

  
  

  
