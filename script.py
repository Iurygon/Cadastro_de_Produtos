import os
import time
import pymssql                  #USADO PARA FAZER A CONEXÃO COM O MSSQL E ENVIAR OS DADOS
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
nRemoveProduto  -> Indica qual produto será excluído do dicionário          (Caractere)
cAlteraRegistro -> Verifica se será feita uma atualização em algum dos 
                   dados de um dos produtos                                 (Caractere)
cChaveProduto   -> Recebe a chave do produto que será alterado na função
                   'alterarProdutos'                                        (Caractere)
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
    try:
        nOpcaoMenu = int(input('Selecione qual opção deseja seguir: '))
        match nOpcaoMenu:
            case 1: cadastraProduto()
            case 2: consultaCadastro()
            case 3: excluiProduto()
            case 4: sairPrograma()
    except ValueError:
        print('O valor digitado deve estar entre as opções listadas.')
        time.sleep(2)
        menuPrincipal()

#=-=-=-=-=-=-=-=-=-=CADASTRO DE PRODUTO=-=-=-=-=-=-=-=-=-=#
def cadastraProduto():
    os.system('cls')
    print('Bem vindo à tela de cadastro de produto! Preencha as informações solicitadas para seguir com o cadastro:')
    cNovoProduto  = 'S'
    nCodProduto   = 0
    while cNovoProduto.upper() == 'S':
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
    dictSuporte = {nCodProduto: {   'Nome': cNomeProduto.ljust(20),
                                    'Peso': fPesoProduto.ljust(6),
                                    'UnidadeMedida': cUnidadeMedida.ljust(4),
                                    'PrecoPadrao': fPrecoPadrao.ljust(5),
                                    'DescontoMaximo': fDescontoMax.ljust(2)}}
    dictProduto.update(dictSuporte)
    print(f'Cadastro realizado para o produto com código {nCodProduto}\n{dictProduto[nCodProduto]}')

#=-=-=-=-=-=-=-=-=-=CONSULTA DE PRODUTOS=-=-=-=-=-=-=-=-=-=#
def consultaCadastro():
    os.system('cls')
    print('Bem vindo à tela de consulta dos produtos!\nOs seguintes produtos estão cadastrados:')
    for chave in dictProduto.keys():
        print(f'{chave}: {dictProduto[chave]}')
    cAlteraRegistro = input('Deseja alterar alguma informação dos produtos? S/N')
    if cAlteraRegistro.upper() == 'S':
        alterarRegistros()
    else:
        menuPrincipal()

def alterarRegistros():
    cChaveProduto = input('Insira o código do produto que deverá ser alterado?')
    print(f'O produto está com os seguintes dados cadastrados:\n{dictProduto[cChaveProduto]}\nInsira os novos valores:')
    cNomeProduto    = input('Nome: ')
    fPesoProduto    = input('Peso: ')
    cUnidadeMedida  = input('Unidade de medida: ')
    fPrecoPadrao    = input('Preço padrão: ')
    fDescontoMax    = input('Desconto máximo: ')
    enviaDadosProduto(cChaveProduto, cNomeProduto, fPesoProduto, cUnidadeMedida, fPrecoPadrao, fDescontoMax)
    print('Produto alterado!')
    input('Pressione uma tecla para seguir:')
    menuPrincipal()

#=-=-=-=-=-=-=-=-=-=EXCLUSÃO DE PRODUTOS=-=-=-=-=-=-=-=-=-=#
def excluiProduto():
    os.system('cls')
    print('Bem vindo à tela de exclusão de produtos!\n Os seguintes produtos estão cadastrados:')
    for chave in dictProduto.keys():
        print(f'{chave}: {dictProduto[chave]}')
    removeProduto = input('Digite o código do produto que deverá ser excluído: ')
    print(dictProduto[removeProduto])
    dictProduto.pop(removeProduto)
    print('Produto removido! Pressione uma tecla para seguir:')
    menuPrincipal()

#=-=-=-=-=-=-=-=-=-=EXCLUSÃO DE PRODUTOS=-=-=-=-=-=-=-=-=-=#
def sairPrograma():
    os.system('cls')
    print('Programa encerrado!')

#menuPrincipal()

print(help(dict))