from tkinter import *
import json
import time
import requests
import datetime

#enviando requisição
requisicao = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
cotacao = json.loads(requisicao.text)

def bt1_click():

    valor= float(ed1.get())
    dolar = float(cotacao['valores']['USD']['valor'])
    total = valor * dolar
    lb2["text"]= '= $ %.2lf Dólares' %total

def bt2_click():

    valor= float(ed1.get())
    euro = float(cotacao['valores']['EUR']['valor'])
    total = valor * euro
    lb2["text"]= '= € %.2lf Euros' %total

def bt3_click():

    valor= float(ed1.get())
    libra = float(cotacao['valores']['GBP']['valor'])
    total = valor * libra
    lb2["text"]= '= £ %.2lf Libras' %total

def bt4_click():
    dolar = float(cotacao['valores']['USD']['valor'])
    euro = float(cotacao['valores']['EUR']['valor'])
    libra = float(cotacao['valores']['GBP']['valor'])
    bitcoin = float(cotacao['valores']['BTC']['valor'])
    lb3["text"] = "Dólar: $ %.2lf" %dolar
    lb4["text"] = "Euro: € %.2lf" %euro
    lb5["text"] = "Libra: £ %.2lf" %libra
    lb6["text"] = "Bitcoin: BTC %.2lf" %bitcoin
    lb7["text"] = "Ultima atualização", datetime.datetime.now()

#Criando janela
janela = Tk()

lb1 = Label(janela, text="Valor: R$")
lb1.place(x=50, y=50)
#impressão do valor
lb2 = Label(janela, text="-")
lb2.place(x=170, y=50)
#cotacao
lb3 = Label(janela, text="-")
lb3.place(x=50, y=150)
lb4 = Label(janela, text="-")
lb4.place(x=50, y=170)
lb5 = Label(janela, text="-")
lb5.place(x=50, y=190)
lb6 = Label(janela, text="-")
lb6.place(x=50, y=210)
lb7 = Label(janela, text="-")
lb7.place(x=50, y=230)

#entrada do valor
ed1 = Entry(janela, width= 10)
ed1.place(x=100, y=50)

#moedas
bt1 = Button(janela, text="Dólar", command= bt1_click)
bt1.place(x=100, y=80)
bt2 = Button(janela, text="Euro", command= bt2_click)
bt2.place(x=150, y=80)
bt3 = Button(janela, text="Libra", command= bt3_click)
bt3.place(x=200, y=80)
#cotacao
bt4 = Button(janela, text="Consultar Cotação", command= bt4_click)
bt4.place(x=50, y=120)

#janela["bg"]="blue"
janela.title("Cotação")
janela.geometry("350x300+100+100")
janela.mainloop()