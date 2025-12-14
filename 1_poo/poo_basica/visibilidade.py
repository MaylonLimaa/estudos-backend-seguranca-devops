"""
Este arquivo corresponde à aula "Curso POO Teoria #03a - O que é Visibilidade em um Objeto?",
adaptada para Python.

Neste arquivo aprendemos o básico sobre visibilidade de objetos (público, protegido e privado).

O conceito de Encapsulamento também foi introduzido. Embora não tenha sido aplicado de forma
completa neste arquivo, por fins de objetividade, ele será abordado e aprofundado em códigos
posteriores.
"""


class Conta:
    def __init__(self, nome, valor, email):
        self.titular = nome # Atributo público
        self.__saldo = valor # Atributo privado
        self._email = email # Atributo protegido
    
    @property
    def saldo(self): # Exemplo de utilização de um método getter
        return self.__saldo
    @saldo.setter
    def saldo(self, valor):# Exemplo de utilização de um método setter
        self.__saldo = valor

p1 = Conta('Maylon', 0, 'maylon@maylon.com')
p2 = Conta('Clara', 500, 'Clara@clara.com')

print(p1.saldo) # Exemplo de uso método getter
print(p2.saldo) # Exemplo de uso método getter
p1.saldo = 300 # Exemplo de uso método setter
print(p1.saldo) # Exemplo de uso método getter

