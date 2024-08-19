'''
VARIÁVEIS

nOpcaoMenu -> Indica qual opção o usuário deseja no menu principal.
'''

print('Menu principal do cadastro de produto:\n'
      '1 - Cadastrar novo produto\n'
      '2 - Consultar dados de produto\n'
      '3 - Excluir produto cadastrado\n'
      '4 - Sair do programa')

try:
    nOpcaoMenu = int(input('Selecione qual opção deseja seguir: '))
except:
    print('O valor digitado deve estar entre as opções disponíveis')