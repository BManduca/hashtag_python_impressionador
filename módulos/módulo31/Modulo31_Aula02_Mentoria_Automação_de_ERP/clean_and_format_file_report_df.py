import pandas as pd

''' LEITURA DO ARQUIVO '''
dataframe_products = pd.read_excel("Products.ods", engine="odf")

''' LIMPEZA DA TABELA '''
dataframe_products.dropna(how="all", inplace=True) # removendo linhas totalmente vazias
dataframe_products.dropna(axis=1, how="all", inplace=True) # removendo colunas totalmente vazias

''' REMOVENDO COLUNA ID '''
dataframe_products.drop(columns=["ID"], inplace=True)

''' REMOVENDO COLUNAS DUPLICADAS '''
# IDENTIFICANDO COLUNAS QUE CONTÊM "Price" e "Stock"
price_columns = [column for column in dataframe_products.columns if "Price" in column]
stock_columns = [column for column in dataframe_products.columns if "Stock" in column]

price_to_keep = "Price (1)" if "Price (1)" in price_columns else price_columns[0] if price_columns else None
stock_to_keep = "Stock" if "Stock" in stock_columns else stock_columns[0] if stock_columns else None

columns_to_remove = [
    column for column in price_columns + stock_columns
    if column not in [price_to_keep, stock_to_keep]
]

dataframe_products.drop(columns=columns_to_remove, inplace=True)

''' REMOVENDO COLUNAS COM TODOS OS VALORES ZERADOS '''
columns_with_all_zero_values = dataframe_products.columns[(dataframe_products == 0).all()]
dataframe_products.drop(columns=columns_with_all_zero_values, inplace=True)

''' RENOMEANDO AS COLUNAS '''
dataframe_products.rename(columns={
    "Item Number": "id",
    "Name": "Nome Produto",
    "Category": "Categoria",
    "Description": "Descrição",
    price_to_keep: "Preço",
    stock_to_keep: "Estoque",
    "Date": "Data cadastro"
}, inplace=True)

''' SALVANDO COMO ARQUIVO EXCEL '''
name_file = "relatorio_produtos_formatado"
dataframe_products.to_excel(f"{name_file}.xlsx", index=False, engine="openpyxl")

print(f"Arquivo Excel gerado com sucesso: {name_file}.xlsx")
