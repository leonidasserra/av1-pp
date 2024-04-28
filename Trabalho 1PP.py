import os

info_livros = {
    1: {'nome': 'Dom Casmurro', 'editora': 'Editora ABC', 'ano': 1899, 'valorpago': 25.99, 'emprestimo': '', 'reserva': None},
    2: {'nome': 'Grande Sertão: Veredas', 'editora': 'Editora XYZ', 'ano': 1956, 'valorpago': 30.50, 'emprestimo': '', 'reserva': None},
    3: {'nome': 'Harry Potter e a Pedra Filosofal', 'editora': 'Editora QRS', 'ano': 1997, 'valorpago': 20.75, 'emprestimo': '', 'reserva': None}
}

def cadastrar_livro():
    nome_livro = input('Nome do livro: ')
    codigo_livro = int(input('Código do livro: '))
    editora = input('Editora: ')
    ano = int(input('Ano: '))
    valor_pago = float(input('Valor Pago: '))
    info_livros[codigo_livro] = {'nome': nome_livro, 'editora': editora, 'ano': ano, 'valorpago': valor_pago, 'emprestimo': '', 'reserva': None}

def calcular_acervo():
    num_livros = len(info_livros)
    print(f'Existem {num_livros} cadastrados na biblioteca')

def status_emprestimo(emprestado):
    return 'emprestado' if emprestado else 'não emprestado'

def exibir_livros():
    for id_livro, livro in info_livros.items():
        print(f'Código:{id_livro}'
              f'Nome: {livro["nome"]}\n'
              f'Editora: {livro["editora"]}\n'
              f'Ano: {livro["ano"]}\n'
              f'Valor Pago: {livro["valorpago"]}\n'
              f'Emprestimo: {status_emprestimo(livro["emprestimo"])}\n')

def localizar_livro():
    busca_id_livro = int(input('Qual o código do livro que você deseja: '))
    livro = info_livros.get(busca_id_livro)
    if livro:
        print(livro)
    else:
        print('Livro não encontrado.')

def excluir_livro():
    busca_id_livro = int(input('Qual o código do livro que você deseja excluir: '))
    if busca_id_livro in info_livros:
        print('EXCLUINDO LIVRO...')
        del info_livros[busca_id_livro]
    else:
        print('Livro não encontrado.')

def alterar_livro():
    busca_id_livro = int(input('Qual o ID do livro que você deseja editar: '))
    livro = info_livros.get(busca_id_livro)
    if livro:
        print('Editar informações do livro:')
        livro['nome'] = input(f'Nome atual: {livro["nome"]}. Novo nome: ')
        livro['editora'] = input(f'Editora atual: {livro["editora"]}. Nova editora: ')
        livro['ano'] = int(input(f'Ano atual: {livro["ano"]}. Novo ano: '))
        livro['valorpago'] = float(input(f'Valor Pago atual: {livro["valorpago"]}. Novo valor pago: '))
        print('Informações do livro editadas com sucesso!')
    else:
        print('Livro não encontrado.')

def emprestar_livro():
    emprestador = input('Qual o seu nome: ')
    busca_id_livro = int(input('Qual o ID do livro que você deseja emprestar: '))
    livro = info_livros.get(busca_id_livro)
    if livro:
        if livro['emprestimo'] == '' and livro['reserva'] == None:
            print(f'{livro["nome"]} está sendo emprestado para você, {emprestador}... ')
            livro['emprestimo'] = emprestador
        elif livro['emprestimo'] == '' and emprestador == livro['reserva']:
            print(f'Conforme reserva, o livro {livro["nome"]} está sendo emprestado para você, {emprestador}...')
            livro['emprestimo'] = emprestador
            livro['reserva'] = None
        elif livro['emprestimo'] == '' and livro['reserva'] != None:
            print('O LIVRO JÁ ESTÁ RESERVADO PARA OUTRO')
        else:
            print('LIVRO JÁ ESTÁ EMPRESTADO')
    else:
        print('Livro não encontrado.')

def reservar_livro():
    nome_reservante = input('Qual o seu nome: ')
    busca_id_livro = int(input('Qual o ID do livro que você deseja reservar: '))
    livro = info_livros.get(busca_id_livro)
    if livro:
        if livro['reserva'] == None:
            print(f'{livro["nome"]} está sendo reservado para você... ')
            livro['reserva'] = nome_reservante
        else:
            print('LIVRO JÁ')
    else:
        print('Livro não encontrado.')

def main():
    try:
        while True:
            print('''
                [0]ENCERRAR PROGRAMA
                [1]CADASTRAR LIVRO
                [2]EXCLUIR LIVRO
                [3]NÚMERO DO ACERVO
                [4]EXIBIR LIVROS
                [5]LOCALIZAR LIVRO
                [6]ALTERAR LIVRO
                [7]EMPRESTAR LIVRO
                [8]RESERVAR LIVRO
                [9]ENCERRAR EMPRÉSTIMO''')
            digito = int(input('Escolha sua opção: '))
            if digito == 0:
                break
            elif digito == 1:
                cadastrar_livro()
            elif digito == 2:
                excluir_livro()
            elif digito == 3:
                calcular_acervo()
            elif digito == 4:
                exibir_livros()
            elif digito == 5:
                localizar_livro()
            elif digito == 6:
                alterar_livro()
            elif digito == 7:
                emprestar_livro()
            elif digito == 8:
                reservar_livro()
            elif digito == 9:
                #FAZER FUNÇÃO
                print('Encerrando empréstimo...')
            else:
                print("Digite uma opção válida")
    except ValueError:
        print("Digite uma opção válida")


main()
