import sqlite3
from functions.usuario_db import cadastro_usuario, login_usuario
from functions.produto_db import cadastro_produto, atualizar_produto, deletar_produto,buscar_produto, buscar1_produto,venda_produto

conn = sqlite3.connect('sistema_database')
c = conn.cursor()

def cadastro():

    name = input('Digite seu email: ')
    password = input ('Digite sua senha: ')
    endereco = input ('Digite seu endereço: ')
    cliente = input ('Digite seu nome: ')
    telefone = input ('Digite seu telefone: ')
    cadastro_usuario(conn,name,password,endereco,cliente,telefone)
   
def login():
    email =  input('Digite seu email: ')
    senha =input('Digite sua senha: ')
    usuario_autenticado =  login_usuario (conn,email,senha)
    if len(usuario_autenticado) > 0:  
        main_interno()
    print(len(usuario_autenticado) > 0)
    

def main_inicial():

    lista =  {
        1: cadastro,
        2: login,
        3: exit,
        
    }
    
    while True: 
      
        opc = int(input('\nBem Vindo\n1- Cadastrar Usuario\n2- Realizar Login\n3- Sair Sistema \nDigite uma opção: '))
        lista[opc]()       


def cadastrar():
    nome = input ('Digite o nome do produto que deseja Cadastrar: ')
    cadastro_produto(conn,nome)

def atualizar():
    id = int(input('Digite o id do Produto: '))
    novo_produto = input ('Digite o novo nome do Produto: ')
    atualizar_produto(conn,id,novo_produto)

def buscar():

    produto = buscar_produto(conn)
    print(produto)

def deletar():
    id = (input('Digite o id do Produto para Deletar: '))
    deletar_produto(conn,id)


def buscar1():

    busca_name = (input('Digite o nome do produto para buscar: ')) 
    buscar1_produto(conn,busca_name)

def venda():

    venda = (input('Digite a data da venda: '))
    id_produto = int(input('Digite o id do produto: '))
    id_cliente = (input('Digite o id do cliente: '))
    print('Obrigado,volte sempre!')
    venda_produto(conn,venda,id_produto,id_cliente)
        

       
def main_interno():

    menu = {
        1: cadastrar,
        2: atualizar,
        3: buscar,
        4: deletar,
        5: buscar1,
        6: venda,
        7: exit,
    }

    while True:
        opcao = int(input('\n1- Cadastrar Produto\n2- Atualizar Produto\n3- Buscar Produto\n4- Deletar Produto\n5- Buscar 1 produto\n6- Venda\n7- Sair\nDigite a opção que deseja: '))
        menu[opcao]()


main_inicial()
        




