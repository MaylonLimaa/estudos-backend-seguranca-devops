"""
Arquivo de estudo para Programação Orientada a Objetos (POO) em Python.

Objetivos:
1. Reforçar o entendimento sobre classes, métodos e atributos em Python.
2. Aplicar o conceito de encapsulamento, reforçando boas práticas de organização e controle de acesso.
3. Apresentar e diferenciar os relacionamentos entre classes:
   - Associação
   - Agregação
   - Composição
"""

class Cliente:
    """
    Classe Cliente:
    Representa um cliente que pode realizar pedidos no sistema.

    Relacionamentos:
    - Composição com Pedido: um pedido não pode existir sem um cliente.
    - Associação com Produto: o cliente interage com produtos por meio de pedidos,
      mas não depende diretamente deles para existir.
    """


class Produto:
    """
    Classe Produto:
    Representa um produto existente (ou potencialmente existente) no sistema.

    Relacionamentos:
    - Agregação com Pedido: um produto pode estar associado a um pedido,
      mas continua existindo independentemente dele.
    - Associação com Cliente: o produto é visualizado ou solicitado por clientes,
      sem depender diretamente deles.
    """


class Pedido:
    """
    Classe Pedido:
    Representa um pedido realizado por um cliente.

    Relacionamentos:
    - Composição com Cliente: o pedido depende obrigatoriamente de um cliente.
    - Agregação com Produto: o pedido agrega um ou mais produtos,
      que podem existir sem o pedido.
    """
