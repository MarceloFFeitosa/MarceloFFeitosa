class Usuario:
    def __init__(self, nome, email, telefone, usuario, senha):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__usuario = usuario
        self.__senha = senha

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_usuario(self):
        return self.__usuario
    
    def set_usuario(self, new_usuario):
        self.__usuario = new_usuario

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha):
        self.__senha = senha

