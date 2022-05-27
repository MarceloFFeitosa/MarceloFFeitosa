from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

class telaAdmin:

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
        self.menu_filmes.add_command(label="Cadastrar Filme")
        self.menu_filmes.add_separator()
        self.menu_filmes.add_command(label="Ver Filmes")
        self.menu_filmes.add_separator()
        self.menu_filmes.add_command(label="Sair", command=self.fechar_janela)

        self.menu_admin.add_cascade(label="Filmes", menu=self.menu_filmes)

        self.menu_admin.add_separator()
        self.menu_salas = Menu(self.menu_admin, tearoff=0)
        self.menu_salas.add_command(label="Cadastrar Sala")
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
        Label(self.cadastro, text="Telefone:", font="Times, 13", foreground='black').grid(row=2, column=0)
        Label(self.cadastro, text="Usuario:", font="Times, 13", foreground='black').grid(row=3, column=0)
        Label(self.cadastro, text="Senha:", font="Times, 13", foreground='black').grid(row=4, column=0)

        self.nome = Entry(self.cadastro, font="Times, 10").grid(row=0, column=1)
        self.email = Entry(self.cadastro, font="Times, 10").grid(row=1, column=1)
        self.telefone = Entry(self.cadastro, font="Times, 10").grid(row=2, column=1)
        self.usuario = Entry(self.cadastro, font="Times, 10").grid(row=3, column=1)
        self.senha = Entry(self.cadastro, font="Times, 10", show='*').grid(row=4, column=1)

        Radiobutton(self.cadastro, text="Administrador", value=1).grid(row=5, column=0)
        Radiobutton(self.cadastro, text="Cliente", value=0).grid(row=5, column=1)

        self.botao = Button(self.cadastro, text="Cadastrar", font="Times, 11")
        self.botao.configure(width=7, height=1, foreground='white', background="gray", borderwidth='2px')
        self.botao.grid(row=6, column=0, pady=15)

        self.botao = Button(self.cadastro, text="Voltar", font="Times, 11")
        self.botao.configure(width=7, height=1, foreground='white', background="gray", borderwidth='2px', command=self.voltar_janela)
        self.botao.grid(row=6, column=1)

        self.cadastro.mainloop()


class telaLogin:

    def login(self):
        try:
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

    def fechar(self):
        exit()

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
        self.root.mainloop


        self.root.mainloop()


try:
    telaLogin()
except:
    raise Exception("Erro, não foi possível abrir a janela")