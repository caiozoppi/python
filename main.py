import pandas as pd
import openpyxl
import twilio
from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC424a1a8c24d81f791daaea3d3a635f00"
# Your Auth Token from twilio.com/console
auth_token  = "9d5f52b4fede810abe5cb62566ba781e"
client = Client(account_sid, auth_token)
lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês de {mes} encontramos alguém que vendeu mais de R$ 55.000,00! O vendedor foi {vendedor} e ele vendeu R$ {vendas}!")
        message = client.messages.create(
            to = "+5519974079457",
            from_ = "+16812532386",
            body = f"No mês de {mes} encontramos alguém que vendeu mais de R$ 55.000,00! O vendedor foi {vendedor} e ele vendeu R$ {vendas}!")
        print(message.sid)












