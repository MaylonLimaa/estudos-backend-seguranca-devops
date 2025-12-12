"""
Este arquivo corresponde à aula "Curso POO Teoria #02a - O que é um Objeto?" adaptada para Python. 
Neste aqurivo aprendemos o básico sobre Classes e Objetos.

Notas: Self é utilizado para se referir ao próprio objeto.
"""

# EXERCÍCIO 1 — Sistema de Usuários (básico)

class Usuario: # Definição da classe
    def __init__(self, nome, email, senha): # Método construtor que inicializa os atributos de objeto
        self.nome = nome # Atributo de objeto nome, cada usuário(objeto) tem um nome
        self.email = email # Atributo de objeto email, cada usuário(objeto) tem um email
        self.senha = senha # Atributo de objeto senha, cada usuário(objeto) tem um senha
    def exibir_info(self): # Método para exibir informações
        print(f'Olá {self.nome}, seu e-mail é {self.email}') # Exibe os dados
    def alterar_senha(self): # Método para alterar senha
        self.senha = input('Por gentileza, digite sua nova senha') # Altera senha

User01 = Usuario('Maylon', 'maylon123@123mail.com', '123') # Instancia um objeto, com nome, email e senha
User01.exibir_info() # O objeto User01 chama o método exibir_info()
User02 = Usuario('Pedro', 'Pedrinhogamer@154@mail.com', '456') # Instancia um segundo objeto, com nome, email e senha

# EXERCÍCIO 2 — Produto e Estoque (intermediário)

class Produto: # CLasse produto
    def __init__(self, nome, preco, qtd_estoque): # Método construtor
        self.nome = nome
        self.preco = float(preco)
        self.qtd_estoque = int(qtd_estoque)
    
    def vender(self, qtd_venda): # Método de venda
        if qtd_venda > self.qtd_estoque:
            print(f'Temos apenas {self.qtd_estoque} em estoque.')
        else:
            print('Parabéns! Venda efetuada com sucesso.')
            self.qtd_estoque -= qtd_venda 
    def repor_estoque(self, qtd_reposicao): # Metodo de repor estoque
        self.qtd_estoque += qtd_reposicao
    def exibir(self): # Método que exibe dados do produto
        print(f'O produto {self.nome} custa R$ {self.preco} e ainda temos {self.qtd_estoque} em estoque')

produt1 = Produto('Água', 2.5, 100) # Instanciando um objeto
produt1.exibir()
produt1.vender(75)
produt1.exibir()
produt1.vender(50)
produt1.exibir()
produt1.repor_estoque(100)
produt1.exibir()
produt1.vender(50)
produt1.exibir()

# EXERCÍCIO 3 — Gerenciador de Tarefas (avançado)

class Tarefa: # Classe Tarefa
    def __init__(self, titulo, descricao): # Método construtor
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = False
    
    def concluir(self): # Método
        self.concluida = True
    def exibir(self):# Método
        if self.concluida:
            print(f'A tarefa {self.titulo} está concluida!')
            print(f'Sua descrição é: {self.descricao}')
        else:
            print(f'A tarefa {self.titulo} não está concluida!')
            print(f'Sua descrição é: {self.descricao}')
class GerenciadorTarefas: # Classe
    def __init__(self): # Método construtor
        self.lista_tarefas = []
    def adicionar_tarefa(self, tarefa):
        self.lista_tarefas.append(tarefa)
    def listar_tarefas(self):
        for tarefa in self.lista_tarefas:
            tarefa.exibir()
    def concluir_tarefa(self, objt):
        # Aqui definimos um parametro objt para ser passado como o objeto a ser instanciado, e, a partir dele, acessamos o método da classe Tarefa
        objt.concluir()

t1 = Tarefa('Caminhar', 'Andar 3km')
t2 = Tarefa('Correr', 'Correr 3km')
t3 = Tarefa('Passear', 'Passear com cachorro 3km')

listatarefas = GerenciadorTarefas()
listatarefas.adicionar_tarefa(t1)
listatarefas.adicionar_tarefa(t2)
listatarefas.adicionar_tarefa(t3)
listatarefas.listar_tarefas()
listatarefas.concluir_tarefa(t1)
listatarefas.listar_tarefas()