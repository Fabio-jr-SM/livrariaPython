import os
import livraria
os.system("cls")

def printLivros():
    cont=1
    print("============LIVROS============\n".center(100))
    print("{:<5} {:<40} {:<20} {:<10} {:<10} {:<10} {:<10}\n".format("Nº", "Nome", "Autor", "Ano", "Gênero", "Preço", "Páginas"))
    for nome_livros, livros in livraria.titulos.items():
        nome = nome_livros
        autor = livros["autor"]
        ano = livros["ano"]
        genero = livros["Gênero"]
        preco = livros["Preço"]
        pagina = livros["N. Páginas"]
        print("{:<5} {:<40} {:<20} {:<10} {:<10} {:<10} {:<10} ".format(cont, nome, autor, ano, genero, preco, pagina))
        cont += 1


def addLivros():
    os.system("cls")
    nome = input("Digite o nome do Livro: ")
    autor = input("Digite o autor do Livro: ")
    ano = int(input("Digite o ano do Livro: "))
    genero = input("Digite o genero do Livro: ")
    preco = float(input("Digite o Preço do Livro: "))
    pagina = int(input("Digite o numero de paginas do Livro: "))

    livraria.titulos[nome] = {"autor":autor,"ano":ano,"Gênero":genero,"Preço":preco,"N. Páginas":pagina}

def removerLivros():
    os.system("cls")
    printLivros()
    livroRemove = input("Digite nome do livro que deseja remover: ")
    del livraria.titulos[livroRemove]


while True:
    printLivros() 
    op = int(input("\n\nEscolha:\n1 - Adicionar livro\n2 - Remover livro\n3 - Atualizar livro\n4 - Sair\n"))
    if(op==1):
        addLivros()
    elif(op==2):
        removerLivros()
    elif(op==4):
        break

print("\n")
