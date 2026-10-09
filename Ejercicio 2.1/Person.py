class Person:
  def __init__(self,nombre,apellidos,id,yob):
    self.nombre=nombre
    self.apellidos=apellidos
    self.id=id
    self.yob=yob
  def imprimir(self):
    print(f'Nombre = {self.nombre}\nApellidos = {self.apellidos}\nNumero de documento de identidad = {self.id}\nAno de nacimiento = {self.yob}')
p1=Person('Valentina','Pastrana Fajardo',1082870541,2005)
p1.imprimir()
p2=Person('Jordy','Pineda Bellido',1007401307,2000)
p2.imprimir()
