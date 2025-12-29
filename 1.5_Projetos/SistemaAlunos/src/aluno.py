"""
Módulo aluno onde temos a classe Aluno
Ela auxilia no controle de alunos.
"""

from datetime import date

class Aluno:
    """
    Classe aluno instancia objetos
    """
    def __init__(self, nome, nasc, notas):
        """
        Método construtor que define as carcterísticas individuais de cada aluno
        """
        self._nome = nome
        self.__nascimento = nasc
     
        self._idade = self.__calc_idade()
        self._notas = notas
        self._media = self.__calc_media()
        self._situacao_media = self.__verific_sit_media()
        self.__situacao_cadastro = True

    def __calc_idade(self):
        """
        Calcula idade baseado na data de nascimento e no ano
        """
        return date.today().year - self.__nascimento
    def __calc_media(self):
        """
        Calcula a média baseada nas notas e quantidade de notas
        """
        return sum(self._notas) / len(self._notas)

    def __verific_sit_media(self):
        """
        De acordo com a média, retorna aprovado ou reprovado
        """
        if self._media >= 7:
            return 'Aprovado'
        return 'Reprovado'
    def atualizar_dados(self, notas):
        """
        Atualiza as notas do aluno, através disso:
        Atualiza a média chamando o método calc_media()
        Atualiza a situação do aluno chamando situacao_media()
        
        :param notas: Novas notas, obrigatoriamente deve ser uma lista
        """
        self._notas = notas
        self._media = self.__calc_media()
        self._situacao_media = self.__verific_sit_media()
    
    def excluir(self):
        """Altera o cadastro do aluno para 'False'(inativo)"""
        self.__situacao_cadastro = False
    def ativar(self):
        """Altera o cadastro do aluno para True(ativo)"""
        self.__situacao_cadastro = True
