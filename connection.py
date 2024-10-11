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
        cursor.execute(f'UPDATE PRODUTOS SET {campo} = {novoValor} WHERE CODIGO = {codigo}')
        cursor.commit()
    except:
        conexao.rollback()
