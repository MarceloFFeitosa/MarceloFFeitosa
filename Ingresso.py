from Filme import Filme
from Cliente import Cliente

class Ingresso(Filme, Cliente):
    def __init__(self, nome, sessão, id, codigo, tipo):
        super().__init__(nome, id)
        self.__sessao = sessão
        self.__codigo = codigo
        self.__tipo = tipo


    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo


