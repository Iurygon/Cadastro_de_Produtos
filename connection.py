import pyodbc

def conectaSQLServer(driver='driver',server='servidor',database='banco',username='usuario',password='senha',trustedConnection='yes'):
    stringConexao = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TRUSTED_CONNECTION={trustedConnection}"
    conexao = pyodbc.connect(stringConexao)
    cursor  = conexao.cursor()
    return conexao,cursor

conexao, cursor = conectaSQLServer()

def create(codigo, nome, unidadeMedida, precoPadrao, descontoMax):
    cursor.execute(f"INSERT INTO PRODUTOS VALUES ({codigo}, {nome}, {unidadeMedida}, {precoPadrao}, {descontoMax})")

create('000001','Bala','Uni',0.50,0)