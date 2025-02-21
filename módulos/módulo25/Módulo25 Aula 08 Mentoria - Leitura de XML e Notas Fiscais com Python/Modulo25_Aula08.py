'''
xmltodict
- biblioteca do python, ou seja, um pacote presente dentro do python

- instalação: pip3 install xmltodict
- funcionalidade: tranforma um arquivo xml em um dicionário python

Ordered Dict vs. Dict
- até mais ou menos a versão 3.7 do python, os dicionários do python não tinham ordem definida, ou seja, poderia ocorrer uma troca de ordem

- o Ordered Dict, sempre tem um ordem definida

Informações necessárias exercício:
valor_total, produtos/servicos, cnpj_vendedor, nome_vendedor, cpf/cnpj_comprador, nome_comprador

'''

import xmltodict
import pandas as pd
import os

def ler_xml_danfe(nota_fiscal):
    # rb -> lendo arquivo em formato binário
    # abrindo e lendo arquivo
    with open(nota_fiscal, 'rb') as arquivo_danfe:
        documento = xmltodict.parse(arquivo_danfe)

    # print(documento)

    # caso não seja possível por algum motivo visualizar a árvore do xml, pode ser feito da seguinte forma:
    # a cada iteração, busque visualizar qual informação é necessário e add ao documento
    # for item in documento['nfeProc']['NFe']['infNFe']:
    #     print(item)

    dict_notafiscal = documento['nfeProc']['NFe']['infNFe']

    
    valor_total = dict_notafiscal['total']['ICMSTot']['vNF']
    cnpj_vendedor = dict_notafiscal['emit']['CNPJ']
    nome_vendedor = dict_notafiscal['emit']['xNome']
    cpf_comprador = dict_notafiscal['dest']['CPF']
    nome_comprador = dict_notafiscal['dest']['xNome']
    produtos = dict_notafiscal['det']

    lista_produtos = []

    for produto in produtos:
        nome_produto = produto['prod']['xProd']
        valor_produto = produto['prod']['vProd']
        lista_produtos.append((nome_produto, valor_produto))

    dados_resposta_NF = {
        'valor_total': [valor_total],
        'cnpj_vendedor': [cnpj_vendedor],
        'nome_vendedor': [nome_vendedor],
        'cpf_comprador': [cpf_comprador],
        'nome_comprador': [nome_comprador],
        'lista_produtos': [lista_produtos]
    }

    return dados_resposta_NF


def ler_xml_servico(nota_fiscal):
    # rb -> lendo arquivo em formato binário
    # abrindo e lendo arquivo
    with open(nota_fiscal, 'rb') as arquivo_danfe:
        documento = xmltodict.parse(arquivo_danfe)

    # print(documento)

    # caso não seja possível por algum motivo visualizar a árvore do xml, pode ser feito da seguinte forma:
    # a cada iteração, busque visualizar qual informação é necessário e add ao documento
    # for item in documento['nfeProc']['NFe']['infNFe']:
    #     print(item)

    dict_notafiscal = documento['ConsultarNfseResposta']['ListaNfse']['CompNfse']['Nfse']['InfNfse']

    
    valor_total = dict_notafiscal['Servico']['Valores']['ValorServicos']
    cnpj_vendedor = dict_notafiscal['PrestadorServico']['IdentificacaoPrestador']['Cnpj']
    nome_vendedor = dict_notafiscal['PrestadorServico']['RazaoSocial']
    cpf_comprador = dict_notafiscal['TomadorServico']['IdentificacaoTomador']['CpfCnpj']['Cnpj']
    nome_comprador = dict_notafiscal['TomadorServico']['RazaoSocial']
    produtos = dict_notafiscal['Servico']['Discriminacao']

    dados_resposta_NF = {
        'valor_total': [valor_total],
        'cnpj_vendedor': [cnpj_vendedor],
        'nome_vendedor': [nome_vendedor],
        'cpf_comprador': [cpf_comprador],
        'nome_comprador': [nome_comprador],
        'lista_produtos': [produtos]
    }

    return dados_resposta_NF

    # print(dados_resposta_NF)
    # print(f'Valor total da NF: R$ {valor_total}\n\nCNPJ do vendedor: {cnpj_vendedor}\nVendedor: {nome_vendedor}\n\nCPF do Comprador: {cpf_comprador}\nComprador: {nome_comprador}\n\nLista de produtos: {lista_produtos}')

# armazenando o nome de todos os arquivos presente na pasta NFs_Finais
lista_arquivos = os.listdir('NFs_Finais')

# for arquivo in lista_arquivos:
#     if 'xml' in arquivo:
#         if 'DANFE' in arquivo:
#             ler_xml_danfe(f'NFS_Finais/{arquivo}')
#         else:
#             ler_xml_servico(f'NFS_Finais/{arquivo}')

for arquivo in lista_arquivos:
    if arquivo.endswith('.xml'):
        caminho = f'NFs_Finais/{arquivo}'
        print(f'Processando: {caminho}')
        if 'DANFE' in arquivo:
            print(ler_xml_danfe(caminho))
            print('\n')
        else:
            print(ler_xml_servico(caminho))
            print('\n')

# o pandas, tem uma ferramenta nativa que transforma um dict em uma tabela do excel

# para que seja apresentado uma única linha contendo as informações dentro do banco de dados,
# é necessário definir todos os elementos/dados como lista, pois desta forma, não será gerado,
# três registros dentro do banco, por exemplo, para cada item presente na lista de compras, 
# como é o exemplo da DANFE da Nespresso
# tabela_NF = pd.DataFrame.from_dict(dados_resposta_NF)
# tabela_NF.to_excel('NFs.xlsx')
