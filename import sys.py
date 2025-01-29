import sys
print(f"Caminho do Python: {sys.executable}")

import os
import pandas as pd
import pyodbc


# PARTE 1: EXTRAÇÃO CAMINHO CSV
def extract_data():
    # Caminho para o arquivo CSV
    file_patch = r'C:\Users\gabri\OneDrive\Desktop\Datasets\shoes_dim.csv'
    if not os.path.exists(file_patch):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_patch}")
    
    # Ler o arquivo CSV
    data = pd.read_csv(file_patch)
    return data

# PARTE 2: TRANSFORMAÇÃO
def transform_data(data):
    # Verificar se a coluna existe
    if 'best_for_wear' not in data.columns:
        raise KeyError("A coluna 'best_for_wear' não foi encontrada no DataFrame.")
    
    # Criar coluna 'Quantidade' baseada em 'best_for_wear'
    data['Quantidade'] = data['best_for_wear']
    

    #Contando a quantidade de best_for_wear
    count_best_for_wear = data['best_for_wear'].value_counts().reset_index()
    count_best_for_wear.columns = ['best_for_wear','count'] #renomeando as colunas
    print("'contagem best for wear':")
    print(count_best_for_wear)


    return count_best_for_wear

#LOADING NO SQL SERVER
def load_data_to_sql(dataframe,table_name,server,database):
    #CONEXAO COM O BANCO SQL SERVER
    connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes"
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Criar tabela no SQL Server
    create_table_query = f"""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = '{table_name}' AND xtype='U')
    CREATE TABLE dbo.{table_name} (
        best_for_wear NVARCHAR(255),
        count INT 
        )
        """
    cursor.execute(create_table_query)
    conn.commit()

    #Inserir dados para o sql server
    for _, row in dataframe.iterrows():
        insert_query = f"""
        INSERT INTO dbo.{table_name} (best_for_wear,count)
        values (?,?)
        """
        cursor.execute(insert_query,row['best_for_wear'],row['count'])

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Dados inseridos na tabela '{table_name}' com sucesso.")


# Função principal
def main():
    # Extração
    data = extract_data()
    
    # Transformação
    count_data = transform_data(data)


    # Carregar os dados no SQL Server
    server = 'OPURODELL\SQLEXPRESS'
    database = 'AdventureWorks2019'
    table_name = 'Tabela_Count_Best_For_Wear'

    load_data_to_sql(count_data, table_name, server, database)

    
    # Exibir os dados transformados
    print(data.head())

if __name__ == "__main__":
    main()




import pyodbc
conn = pyodbc.connect("DRIVER={SQL Server};SERVER=OPURODELL\SQLEXPRESS;DATABASE=AdventureWorks2019;Trusted_Connection=yes;")
print("Conexão bem-sucedida!")
conn.close()