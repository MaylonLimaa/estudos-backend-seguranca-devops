"""
Herança permite criar uma nova classe a partir de uma classe existente, reutilizando e especializando seus atributos e métodos.
A relação expressa é sempre do tipo “é um” (is-a).

Classe raiz: não possui superclasse.
Classe folha: não possui subclasses.
Classe ascendente (ancestral): classes acima na hierarquia.
Classe descendente: classes abaixo na hierarquia.

Especialização: modelagem de cima para baixo (genérico → específico).
Generalização: modelagem de baixo para cima (específico → genérico).

Tipos de herança
Herança de implementação (pobre): herda atributos e métodos sem adicionar novos comportamentos.
Herança para diferença: herda e adiciona ou redefine comportamentos.

Abstração
Classe abstrata: não deve ser instanciada; serve como modelo conceitual.
Método abstrato: declarado na classe base e implementado nas subclasses.

Comportamento
Sobrescrita (override): subclasse redefine um método herdado, permitindo comportamentos diferentes para a mesma interface.

Python trata herança de forma flexível, sem impor restrições rígidas.
Classes abstratas, métodos finais e limites de herança são convenções, não imposições da linguagem.

OBS: Optei por ser algo simples e didático, por isso não utilizarei ABC e abstracmethod
"""

class SerVivo():
    """
    Classe abstrata
    Classe raiz
    """
    def __init__(self, especie):
        self.especie = especie
    def respirar(self):
        """
        Todo ser vivo deve respirar
        """
        print('Respira')

class Animal(SerVivo):
    """
    Classe animal com intuito de ser classe Pai
    Herança para diferença
    """
    def __init__(self, especie, nome):
        super().__init__(especie)
        self.nome = nome
    def falar(self):
        """
        Som emitido pelo ser vivo
        """
        print('Som Genérico')

class Humano():
    """
    Classe vazia apenas para demonstrar herança multipla
    Herança de Implementação
    """
    pass

class Pessoa(Animal, Humano):
    """
    Classe com herança multipla
    Classe Folha
    """
    def falar(self, msg):
        """
        Aqui a pessoa fala, sendo aplicado override
        """
        print(msg)

class Cachorro(Animal):
    """
    Classe com herança simples
    Classe Folha
    """
    def falar(self):
        """
        Aqui o cachorro late, sendo aplicado override
        """
        print('Au, au, au')


p1 = Pessoa('Humano', 'Maylon')
p1.falar('Olá')
pitoco = Cachorro('Cachorro', 'Pitoco')
pitoco.falar()
calopsita = Animal('Calopsita', 'Paroxitona')
calopsita.falar()
