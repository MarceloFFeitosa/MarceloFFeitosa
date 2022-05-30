from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3


class verFilmes:

    def fechar(self):
        self.ver_filmes.destroy()

    def __init__(self):
        self.ver_filmes = Toplevel()
        self.ver_filmes.title("Cinemania - Lista de Filmes")
        self.ver_filmes.configure(height=700, width=500)
        self.ver_filmes.resizable(False, False)
        self.ver_filmes.iconbitmap("icone.ico")

        Label(self.ver_filmes, text="Lista de filmes cadastrados", font="Times, 13", foreground='black').grid(row=0, column=1, columnspan=2, padx=6)

        self.lista = ttk.Treeview(self.ver_filmes, selectmode="browse",
                                      column=("column1", "column2", "column3", "column4"), show='headings')
        self.lista.column("column1", width=100, minwidth=100, stretch=NO)
        self.lista.heading("#1", text="Filme")
        self.lista.column("column2", width=100, minwidth=100, stretch=NO)
        self.lista.heading("#2", text="Diretor")
        self.lista.column("column3", width=80, minwidth=50, stretch=NO)
        self.lista.heading("#3", text="Duração")
        self.lista.column("column4", width=200, minwidth=200, stretch=NO)
        self.lista.heading("#4", text="Descrição")
        self.lista.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

        self.botao = Button(self.ver_filmes, text="Voltar", font="Times, 11")
        self.botao.configure(width=7, height=1, foreground='white', background="gray", borderwidth='2px',
                             command=self.fechar)
        self.botao.grid(row=5, column=1, columnspan=2, pady=15)

        self.ver_filmes.mainloop()


class atualizarFilme:

    def fechar(self):
        self.atualizar_filme.destroy()

    def __init__(self):
        self.atualizar_filme = Toplevel()
        self.atualizar_filme.title("Cinemania - Atualizar Filmes")
        self.atualizar_filme.configure(height=700, width=500)
        self.atualizar_filme.resizable(False, False)
        self.atualizar_filme.iconbitmap("icone.ico")

        Label(self.atualizar_filme, text="Escolha o filme que quer atualizar", font="Times, 13", foreground='black').grid(row=0, column=1, columnspan=2, padx=6)
        Label(self.atualizar_filme, text="Nome do Filme:", font="Times, 13", foreground='black').grid(row=1, column=0)
        Label(self.atualizar_filme, text="Diretor:", font="Times, 13", foreground='black').grid(row=2, column=0)
        Label(self.atualizar_filme, text="Duração:", font="Times, 13", foreground='black').grid(row=2, column=2)
        Label(self.atualizar_filme, text="Sinopse:", font="Times, 13", foreground='black').grid(row=3, column=0)

        self.nomeFilme = Entry(self.atualizar_filme, font="Times, 10").grid(row=1, column=1)
        self.diretor = Entry(self.atualizar_filme, font="Times, 10").grid(row=2, column=1)
        self.duracao = Entry(self.atualizar_filme, font="Times, 10").grid(row=2, column=3)
        self.sinopse = Entry(self.atualizar_filme, font="Times, 10").grid(row=3, column=1)

        self.botao = Button(self.atualizar_filme, text="Atualizar", font="Times, 11")
        self.botao.configure(width=7, height=1, foreground='white', background="gray", borderwidth='2px', command=self.fechar)
        self.botao.grid(row=5, column=1, pady=15)

        self.botao = Button(self.atualizar_filme, text="Cancelar", font="Times, 11")
        self.botao.configure(width=7, height=1, foreground='white', background="gray", borderwidth='2px',command=self.fechar)
        self.botao.grid(row=5, column=2, pady=15)

        self.cadastros = ttk.Treeview(self.atualizar_filme, selectmode="browse", column=("column1", "column2", "column3", "column4"), show='headings')
        self.cadastros.column("column1", width=100, minwidth=100, stretch=NO)
        self.cadastros.heading("#1", text="Filme")
        self.cadastros.column("column2", width=100, minwidth=100, stretch=NO)
        self.cadastros.heading("#2", text="Diretor")
        self.cadastros.column("column3", width=80, minwidth=50, stretch=NO)
        self.cadastros.heading("#3", text="Duração")
        self.cadastros.column("column4", width=200, minwidth=200, stretch=NO)
        self.cadastros.heading("#4", text="Descrição")
        self.cadastros.grid(row=7, column=0, columnspan=4, padx=5, pady=5)

        self.atualizar_filme.mainloop()

class cadastroFilme:

    def fechar(self):
        self.cadastro_filme.destroy()

    def __init__(self):
        self.cadastro_filme = Toplevel()
        self.cadastro_filme.title("Cinemania - Cadastro de Filmes")
        self.cadastro_filme.configure(height=700, width=500)
        self.cadastro_filme.resizable(False, False)
        self.cadastro_filme.iconbitmap("icone.ico")

        Label(self.cadastro_filme, text="Nome do Filme:", font="Times, 13", foreground='black').grid(row=0, column=0)
        Label(self.cadastro_filme, text="Diretor:", font="Times, 13", foreground='black').grid(row=1, column=0)
        Label(self.cadastro_filme, text="Duração:", font="Times, 13", foreground='black').grid(row=1, column=2)
        Label(self.cadastro_filme, text="Sinopse:", font="Times, 13", foreground='black').grid(row=2, column=0)

        self.nomeFilme = Entry(self.cadastro_filme, font="Times, 10").grid(row=0, column=1)
        self.diretor = Entry(self.cadastro_filme, font="Times, 10").grid(row=1, column=1)
        self.duracao = Entry(self.cadastro_filme, font="Times, 10").grid(row=1, column=3)
        self.sinopse = Entry(self.cadastro_filme, font="Times, 10").grid(row=2, column=1)

        self.botao = Button(self.cadastro_filme, text="Cadastrar", font="Times, 11")
        self.botao.configure(width=7, height=1, foreground='white', background="gray", borderwidth='2px',
                             command=self.fechar)
        self.botao.grid(row=6, column=1)

        self.botao = Button(self.cadastro_filme, text="Cancelar", font="Times, 11")
        self.botao.configure(width=7, height=1, foreground='white', background="gray", borderwidth='2px',
                             command=self.fechar)
        self.botao.grid(row=6, column=2, padx=15, pady=15)

        self.cadastro_filme.mainloop()

class telaAdmin:

    def ver_filmes(self):
        try:
            verFilmes()
        except:
            raise Exception("Erro ao tentar abrir a lista de filme")

    def atualizar_filme(self):
        try:
            atualizarFilme()
        except:
            raise Exception("Erro ao tentar abrir cadastro de filme")

    def cadastrar_filme(self):
        try:
            cadastroFilme()
        except:
            raise Exception("Erro ao tentar abrir cadastro de filme")

    def fechar_janela(self):
        if messagebox.askyesno("Sair?", "Deseja realmente sair?"):
            self.admin.destroy()

    def __init__(self):
        self.admin = Tk()
        self.admin.title("Cinemania - Administrador")
        self.admin.configure(height=500, width=600, background='gray')
        self.admin.resizable(False, False)
        self.admin.iconbitmap("icone.ico")

        self.menu_admin = Menu(self.admin)
        self.menu_admin.add_separator()

        self.menu_filmes = Menu(self.menu_admin, tearoff=0)
        self.menu_filmes.add_command(label="Cadastrar Filme", command=self.cadastrar_filme)
        self.menu_filmes.add_separator()
        self.menu_filmes.add_command(label="Atualizar Filme", command=self.atualizar_filme)
        self.menu_filmes.add_separator()
        self.menu_filmes.add_command(label="Ver Filmes", command=self.ver_filmes)
        self.menu_filmes.add_separator()
        self.menu_filmes.add_command(label="Sair", command=self.fechar_janela)

        self.menu_admin.add_cascade(label="Filmes", menu=self.menu_filmes)

        self.menu_admin.add_separator()
        self.menu_salas = Menu(self.menu_admin, tearoff=0)
        self.menu_salas.add_command(label="Cadastrar Sala")
        self.menu_salas.add_separator()
        self.menu_salas.add_command(label="Atualizar Salas")
        self.menu_salas.add_separator()
        self.menu_salas.add_command(label="Ver Salas")

        self.menu_admin.add_cascade(label="Salas", menu=self.menu_salas)

        self.menu_admin.add_separator()
        self.menu_clientes = Menu(self.menu_admin, tearoff=0)
        self.menu_clientes.add_command(label="Ver Clientes ")

        self.menu_admin.add_cascade(label="Clientes", menu=self.menu_clientes)

        self.admin.configure(menu=self.menu_admin)
        self.admin.mainloop


class telaCadastro:

    def voltar_janela(self):
        if messagebox.askyesno("Voltar?", "Deseja realmente voltar?"):
            self.cadastro.destroy()

    def __init__(self):
        self.cadastro = Toplevel()
        self.cadastro.title("Cinemania - Cadastro")
        self.cadastro.resizable(False, False)
        self.cadastro.iconbitmap("icone.ico")

        Label(self.cadastro, text="Nome:", font="Times, 13", foreground='black').grid(row=0, column=0)
        Label(self.cadastro, text="Email:", font="Times, 13", foreground='black').grid(row=1, column=0)
        Label(self.cadastro, text="Telefone:", font="Times, 13", foreground='black').grid(row=0, column=2)
        Label(self.cadastro, text="Usuario:", font="Times, 13", foreground='black').grid(row=3, column=0)
        Label(self.cadastro, text="Senha:", font="Times, 13", foreground='black').grid(row=4, column=0)
        Label(self.cadastro, text="Repetir Senha:", font="Times, 13", foreground='black').grid(row=4, column=2)

        self.nome = Entry(self.cadastro, font="Times, 10").grid(row=0, column=1)
        self.email = Entry(self.cadastro, font="Times, 10").grid(row=1, column=1)
        self.telefone = Entry(self.cadastro, font="Times, 10").grid(row=0, column=3)
        self.usuario = Entry(self.cadastro, font="Times, 10").grid(row=3, column=1)
        self.senha = Entry(self.cadastro, font="Times, 10", show='*').grid(row=4, column=1)
        self.confirm_senha = Entry(self.cadastro, font="Times, 10", show='*').grid(row=4, column=3)

        Radiobutton(self.cadastro, text="Administrador", value=1).grid(row=5, column=1, pady=5)
        Radiobutton(self.cadastro, text="Cliente", value=0).grid(row=5, column=2, pady=5)

        self.botao = Button(self.cadastro, text="Cadastrar", font="Times, 11")
        self.botao.configure(width=7, height=1, foreground='white', background="gray", borderwidth='2px')
        self.botao.grid(row=6, column=1, pady=10)

        self.botao = Button(self.cadastro, text="Voltar", font="Times, 11")
        self.botao.configure(width=7, height=1, foreground='white', background="gray", borderwidth='2px', command=self.voltar_janela)
        self.botao.grid(row=6, column=2)

        self.cadastro.mainloop()


class telaLogin:

    def login(self):
        try:
            self.root.destroy()
            telaAdmin()
        except:
            raise Exception("Erro ao tentar abrir a tela de administrador")

    def sobre(self):
        messagebox.showinfo("Desenvolvedores", """Aplicativo de gerenciamento de cinema feito em python e tkinter orientado a objetos feito por\n\nMarcelo Ferreira Feitosa\nGustavo Murillo""")

    def abrir_cadastro(self):
        try:
            telaCadastro()
        except:
            raise Exception("Erro ao tentar abrir a tela de cadastro")

    def fechar_janela(self):
        if messagebox.askyesno("Sair?", "Deseja realmente sair?"):
            self.root.destroy()

    def __init__(self):
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW")
        self.root.iconbitmap("icone.ico")
        self.root.title("Cinemania - Tela Login")
        self.img = ImageTk.PhotoImage(Image.open("logo.jpeg"))
        self.painel = Label(self.root, image=self.img)
        self.painel.grid(row=0, column=0)

        Label(self.root, text= "Usuário:", font="Times, 12", foreground='black').grid(row=1, column=0, pady=5)
        Label(self.root, text= "Senha:", font="Times, 12", foreground='black').grid(row=3, column=0, pady=5)
        self.login_usuario = Entry(self.root, font="Times, 10").grid(row=2, column=0)
        self.login_senha = Entry(self.root, font="Times, 10", show='*').grid(row=4, column=0)
        self.botao = Button(self.root, text="Entrar", font="Times, 12")
        self.botao.configure(width=10, height=2, foreground='white', background="red4", borderwidth='4px', command=self.login)
        self.botao.grid(row=5, column=0, sticky='N', pady=15)

        #criando uma barra de menu
        self.menu = Menu(self.root)
        self.menu.add_separator()

        self.menu_cadastrar = Menu(self.menu, tearoff=0)
        self.menu_cadastrar.add_command(label="Cadastrar", command=self.abrir_cadastro)
        self.menu_cadastrar.add_separator()
        self.menu_cadastrar.add_command(label="Sair", command=self.fechar_janela)

        self.menu.add_cascade(label="Cadastrar-se", menu=self.menu_cadastrar)
        self.menu.add_separator()

        self.menu_sobre = Menu(self.menu, tearoff=0)
        self.menu_sobre.add_command(label="Sobre", command=self.sobre)

        self.menu.add_cascade(label="Sobre", menu=self.menu_sobre)
        self.root.configure(menu=self.menu)
        self.root.mainloop()


        self.root.mainloop()


try:
    telaLogin()
except:
    raise Exception("Erro, não foi possível abrir a janela")