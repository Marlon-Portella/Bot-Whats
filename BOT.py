# 1 - abrir a planilha
import openpyxl
import pandas as pd

caminho_arquivo = 'C:\\Users\\marlon.portella\\Documents\\GitHub\\Bot\\contatos.xlsx'
#
##
###  2 - ler a planilha
#### 3 - guardar os dados
###  4 - organizar e mostrar os dados da planilha
##
#
df = pd.read_excel(caminho_arquivo)

#print(df.head())

# 5 - verificar datas e organizar pela mais proxima
# Verificar se a coluna 'Data' está no formato de data
# df['Data'] = pd.to_datetime(df['Data'], format ='%d/%m/%Y')

# Ordenar a planilha pela coluna 'Data' (mais recente para a mais antiga)
df_ordenado = df.sort_values(by='Data', ascending = True)
 
print(df_ordenado.head())

# 6 - programar o horario para enviar a mensagem
# 7 - Escrever e enviar a mensagem
# 8 - ir para o proximo contato

