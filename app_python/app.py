# um aplicativo de delivery chamado Sabor express

import os

#lista
restaurantes = [{'nome': 'McDonalds', 'categoria':'fastfood','ativo':False},
                {'nome': 'BurguerKing', 'categoria':'fastfood','ativo':False},
                {'nome': 'PizzaHut', 'categoria':'fastfood','ativo':False},]



def exibir_nome_programa():
    '''Exibe o nome do programa formatado
     
        Inputs:
            nada
        Outputs:
            imprime na tela a mensagem
    
        ''' #isso é uma docstring, usada pra "documentar" uma funcao


    #gerado usando o fsymbols.com, obs: aspas tripla obedece a formatacao do editor
    print("""
    █▀ ▄▀█ █▄▄ █▀█ █▀█    █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄    ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
    """)

def exibir_titulo(texto):
    os.system('cls')# windows
    print(texto,'\n')


def listar_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def ir_menu():
    input('Digite uma tecla para voltar ao menu do programa ')
    main()

def cadastrar_restaurante():
    exibir_titulo('Cadastrando novo restaurante... ')

    nome_res = input('Digite o nome do restaurante: ')
    categoria_res = input(f'Qual a categoria do {nome_res}: ')
    dicionario = {'nome': nome_res, 'categoria': categoria_res, 'ativo': False}

    restaurantes.append(dicionario)
    print(f'O {nome_res} foi cadastrado como restaurante\n')

    ir_menu()

def listar_restaurantes():
    exibir_titulo('Listando todos os restaurante... ')


    print(f' {'nome restaurante'.ljust(21)} | {'categoria'.ljust(20)} | {'ativo'}')
    print('-'*60)

    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativo' if restaurante['ativo'] else 'desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    ir_menu()

def alterar_estado_restaurante():
    exibir_titulo('Listando todos os restaurante... ')

    nome_res = input('Qual restaurante deseja alterar o status: ')
    res_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_res:
            res_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            if restaurante['ativo'] == True:
                print('Restaurante ativado com sucesso!')
            else:
                print('Restaurante desativado com sucesso!')

    if not res_encontrado:
        print('restaurante nao encontrado')

    ir_menu()



def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Digite a sua opção '))
        #print(f'Voce escolheu a opção: {opcao_escolhida}')
    except:
        print("Valor invalido")
        ir_menu()

    if opcao_escolhida == 1:
        cadastrar_restaurante()
    elif opcao_escolhida == 2:
        listar_restaurantes()
    elif opcao_escolhida == 3:
        alterar_estado_restaurante()
    elif opcao_escolhida == 4:
        exibir_titulo('Encerrando app')
    else:
        print("Opcao invalida")
        ir_menu()



#------------------------------------------------------------------

def main():
    os.system('cls')
    exibir_nome_programa()
    listar_opcoes()
    escolher_opcoes()


if __name__ == '__main__':
    main()