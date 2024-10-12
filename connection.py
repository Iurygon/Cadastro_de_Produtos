import pyodbc

def conectaSQLServer(driver='driver',server='servidor',database='banco',username='usuario',password='senha',trustedConnection='yes'):
    stringConexao = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TRUSTED_CONNECTION={trustedConnection}"
    conexao = pyodbc.connect(stringConexao)
    cursor  = conexao.cursor()
    return conexao,cursor

conexao, cursor = conectaSQLServer()

def create(codigo, nome, unidadeMedida, precoPadrao, descontoMax):
    try:
        cursor.execute(f"INSERT INTO PRODUTOS (CODIGO, NOME, UNIMEDIDA, PRECOPAD, DESCONTOMAX) VALUES('{codigo}', '{nome}', '{unidadeMedida}', {precoPadrao}, {descontoMax})")
        conexao.commit()
    except:
        conexao.rollback()

def update(codigo, campo, novoValor):
    try:
        cursor.execute(f"UPDATE PRODUTOS SET {campo} = '{novoValor}' WHERE CODIGO = '{codigo}'")
        cursor.commit()
    except:
        conexao.rollback()

def select(codigo=None):
    if codigo is None:
        resposta = cursor.execute('SELECT * FROM PRODUTOS (NOLOCK)')
    else:
        resposta = cursor.execute(f"SELECT * FROM PRODUTOS (NOLOCK) WHERE CODIGO = '{codigo}'")
    row = resposta.fetchall()
    print(f"{'CODIGO'.ljust(15)} | {'NOME'.ljust(15)} | {'UNIMEDIDA'.ljust(15)} | {'PRECOPAD'.ljust(15)} | {'DESCONTOMAX'.ljust(15)}")
    for tuple in row:
        print(f'{str(tuple[0]).ljust(15)} | {str(tuple[1]).ljust(15)} | {str(tuple[2]).ljust(15)} | {str(tuple[3]).ljust(15)} | {str(tuple[4]).ljust(15)}')

def delete(codigo):
    cursor.execute(f"DELETE FROM PRODUTOS WHERE CODIGO = '{codigo}'")
