"""
Polimorfismo: capacidade de objetos diferentes responderem ao mesmo método de maneiras distintas.
No exemplo, todos os seres vivos podem "falar", 
mas cada tipo de ser vivo tem seu comportamento próprio.
"""

class SerVivo():
    """Classe raiz abstrata"""
    def __init__(self, especie):
        self.especie = especie

    def respirar(self):
        """Todo ser vivo deve respirar"""
        print('Respira')


class Animal(SerVivo):
    """Classe pai de animais, herança para diferença"""
    def __init__(self, especie, nome):
        super().__init__(especie)
        self.nome = nome

    def falar(self, msg=None):
        """Método que pode ser sobrescrito (override)"""
        if msg:
            print(f'{self.nome} diz: {msg}')
        else:
            print('Som Genérico')

class Pessoa(Animal):
    """Herança múltipla, classe folha"""
    def falar(self, msg=None):
        """Override do método Animal.falar"""
        if msg:
            print(f'{self.nome} fala: {msg}')
        else:
            print(f'{self.nome} está em silêncio')


class Cachorro(Animal):
    """Herança simples, classe folha"""
    def falar(self, msg=None):
        """Override: cachorro late"""
        print('Au, au, au')


# Lista de objetos polimórficos
seres_vivos = [
    Pessoa('Humano', 'Maylon'),
    Cachorro('Cachorro', 'Pitoco'),
    Animal('Calopsita', 'Paroxitona')
]

# Chamando o mesmo método para todos os objetos
for ser in seres_vivos:
    ser.falar('Olá')  # Cada objeto reage de forma diferente (polimorfismo)
