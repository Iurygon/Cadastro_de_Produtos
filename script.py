import os
'''
VARIÁVEIS

dictProduto     -> Dicionário onde os dados dos produtos serão inseridos    (Dicionário)
nOpcaoMenu      -> Indica qual opção o usuário deseja no menu principal.    (Numérico)
nCodProduto     -> Variável incremental para o código do produto            (Numérico)
cNomeProduto    -> Nome do produto                                          (Caractere)
fPesoProduto    -> Peso do produto em g                                     (Flutuante)
cUnidadeMedida  -> Unidade em que o produto é medido                        (Caractere)
fPrecoPadrao    -> Valor padrão do produto                                  (Flutuante)
fDescontoMax    -> Desconto máximo a ser liberado para o produto            (Flutuante)
dictSuporte     -> Recebe as informações que serão inseridas do produto
                   e envia para o dicionário principal                      (Dicionário) 
cNovoProduto    -> Define se, no cadastro de produto, o usuário irá fazer
                   um novo cadastro ou voltar ao menu principal             (Caractere)
'''

dictProduto = {}

#=-=-=-=-=-=-=-=-=-=MENU PRINCIPAL=-=-=-=-=-=-=-=-=-=#
def menuPrincipal():
    os.system('cls')
    print('Menu principal do cadastro de produto:\n'
        '1 - Cadastrar novo produto\n'
        '2 - Consultar dados de produto\n'
        '3 - Excluir produto cadastrado\n'
        '4 - Sair do programa')
    nOpcaoMenu = int(input('Selecione qual opção deseja seguir: '))
    match nOpcaoMenu:
        case 1: cadastraProduto()
        case 2: consultaCadastro()
        case 3: excluiProduto()
        case 4: sairPrograma()

#=-=-=-=-=-=-=-=-=-=CADASTRO DE PRODUTO=-=-=-=-=-=-=-=-=-=#
def cadastraProduto():
    os.system('cls')
    print('Bem vindo à tela de cadastro de produto! Preencha as informações solicitadas para seguir com o cadastro:')
    cNovoProduto  = 'S'
    nCodProduto   = 0
    while cNovoProduto == 'S':
        cNomeProduto    = input('Nome: ')
        fPesoProduto    = input('Peso: ')
        cUnidadeMedida  = input('Unidade de medida: ')
        fPrecoPadrao    = input('Preço padrão: ')
        fDescontoMax    = input('Desconto máximo: ')
        enviaDadosProduto(str(nCodProduto).zfill(6), cNomeProduto, fPesoProduto, cUnidadeMedida, fPrecoPadrao, fDescontoMax)
        cNovoProduto     = input('Deseja cadastrar um novo produto? S/N: ')
        if cNovoProduto.upper().strip(' ') != 'S':
            cNovoProduto = 'N'
            menuPrincipal()        
        else:
            nCodProduto += 1
            

def enviaDadosProduto(nCodProduto, cNomeProduto, fPesoProduto, cUnidadeMedida, fPrecoPadrao, fDescontoMax):
    dictSuporte = {nCodProduto: {   'Nome': cNomeProduto,
                                    'Peso': fPesoProduto,
                                    'UnidadeMedida': cUnidadeMedida,
                                    'PrecoPadrao': fPrecoPadrao,
                                    'DescontoMaximo': fDescontoMax}}
    dictProduto.update(dictSuporte)
    print(f'Cadastro realizado para o produto com código {nCodProduto}\n{dictProduto[nCodProduto]}')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=#
def consultaCadastro():
    print('Bem vindo à tela de consulta dos produtos!')
    print(dictProduto)

def excluiProduto():
    print('Excluir produto')
    
def sairPrograma():
    os.system('cls')
    print('Programa encerrado!')

menuPrincipal()