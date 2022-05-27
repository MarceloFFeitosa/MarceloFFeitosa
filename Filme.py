class Filme:
    def __init__(self, nome, diretor, duracao, descricao):
        self.__nome = nome
        self.__diretor = diretor
        self.__duracao = duracao
        self.__descricao = descricao

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_diretor(self):
        return self.__diretor

    def set_diretor(self, diretor):
        self.__diretor = diretor

    def get_duracao(self):
        return self.__duracao

    def set_duracao(self, duracao):
        self.__duracao = duracao

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

