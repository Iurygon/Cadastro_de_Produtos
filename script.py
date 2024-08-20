import os
'''
VARIÁVEIS

dictProduto     -> Dicionário onde os dados dos produtos serão inseridos    (Dicionário)
nOpcaoMenu      -> Indica qual opção o usuário deseja no menu principal.    (Numérico)
nCodProduto     -> Variável incremental para o código do produto            (Numérico)
cNomeProduto    -> Nome do produto                                          (Caractere)
fPesoProduto    -> Peso do produto em Kg                                    (Flutuante)
cUnidadeMedida  -> Unidade em que o produto é medido                        (Caractere)
fPrecoPadrao    -> Valor padrão do produto                                  (Flutuante)
fDescontoMax    -> Desconto máximo a ser liberado para o produto            (Flutuante)
'''

dictProduto = {}

def menuPrincipal():
    print('Menu principal do cadastro de produto:\n'
        '1 - Cadastrar novo produto\n'
        '2 - Consultar dados de produto\n'
        '3 - Excluir produto cadastrado\n'
        '4 - Sair do programa')
    try:
        nOpcaoMenu = int(input('Selecione qual opção deseja seguir: '))
        match nOpcaoMenu:
            case 1: cadastraProduto()
            case 2: consultaCadastro()
            case 3: excluiProduto()
            case 4: sairPrograma()
    except:
        print('O valor digitado deve estar entre as opções disponíveis')

def cadastraProduto():
    os.system('cls')
    print('Bem vindo à tela de cadastro de produto! Preencha as informações solicitadas para seguir com o cadastro:')
    nCodProduto     = 0
    cNomeProduto    = input('Nome: ')
    fPesoProduto    = input('Peso: ')
    cUnidadeMedida  = input('Unidade de medida: ')
    fPrecoPadrao    = input('Preço padrão: ')
    fDescontoMax    = input('Desconto máximo: ')
    # print(str(nCodProduto).zfill(6))

def consultaCadastro():
    print('Consultar cadastro')

def excluiProduto():
    print('Excluir produto')
    
def sairPrograma():
    os.system('cls')
    print('Programa encerrado!')

menuPrincipal()