import os

lista_filme = ['La la land', 'Minions', 'Meu malvado favorito']

def titulo():
    print('''
          ==========
          LetterBoxd
          ==========
          ''')

def opcoes():
    print('''
    MENU PRINCIPAL:
      1. Cadastrar filme
      2. Lista de filme
      3. Sair do app
    
        ''')
 

def funcao1():
    os.system('clear')
    cadastro_filme =input('Insira o filme que deseja: ')
    lista_filme.append(cadastro_filme) 
    print(f'O filme {cadastro_filme} foi cadastrado com sucesso!')
    input("Clique na tecla enter para voltar ao menu principal: ")
    main()


def funcao2(): 
    os.system('clear')
    for itens in lista_filme:
         print(itens)

    input("Clique em uma tecla para voltar ao menu principal: ")
    main()

def funcao3():
    os.system('clear')
    print('APP finalizado')

def escolha():
    escolha_usuario = (input('Escolha uma opção: '))
    if (escolha_usuario =='1'):
        funcao1()

    elif(escolha_usuario =='2'):
        funcao2()

    elif(escolha_usuario =='3'):
        funcao3()

def main():
        titulo()
        opcoes()
        escolha()


if __name__=='__main__':
    main()
