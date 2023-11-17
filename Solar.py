import tkinter as tk
from tkinter import  *
import os
from tkinter import messagebox

def abrir_calculo():
    calculo = tk.Toplevel()
    calculo.title("EcoThink - Calculadora Solar")
    calculo.geometry("350x350")
    calculo.config(bg="#8CB243")
    calculo.iconphoto(False, PhotoImage(file="icon_EcoThink.png"))

    def calcular_sol():
        Qtd = entry_QTD.get()
        Potencia = entry_Potencia.get()
        Horas = entry_HorasSol.get()

        Qtd = float(Qtd)
        Potencia = float(Potencia)
        Horas = float(Horas)

        resul = ((((Potencia * Horas) * 30) * Qtd) * 0.69) / 1000
        messagebox.showinfo("Resultado", f"A quantidade de energia mensal gerada é de {resul} kW")

    label_CalculaSolar = Label(calculo, width=43, height=2, text="Calculadora Solar", font=("Arial 10 bold"), fg="#ffffff", bg="#333333")
    label_CalculaSolar.grid(row=0, column=0, padx=0, pady=0)

    label_QTDPainel = Label(calculo, width=20, height=2, text="Quantidade de Painéis:", font=("Arial 8 bold"), fg="#ffffff", bg="#333333")
    label_QTDPainel.place(x=40,y=90)

    entry_QTD = tk.Entry(calculo, font=("Arial 8 bold"))
    entry_QTD.place(x=190, y=90)
    entry_QTD.pack

    label_Potencia = Label(calculo, width=20, height=2, text="Potência em Watts:", font=("Arial 8 bold"), fg="#ffffff", bg="#333333")
    label_Potencia.place(x=40,y=140)

    entry_Potencia = tk.Entry(calculo,  font=("Arial 8 bold"))
    entry_Potencia.place(x=190,y=140)
    entry_Potencia.pack

    label_HorasSol = Label(calculo, width=20, height=2, text="Horas de Sol:", font=("Arial 8 bold"), fg="#ffffff", bg="#333333")
    label_HorasSol.place(x=40,y=190)

    entry_HorasSol = tk.Entry(calculo,  font=("Arial 8 bold"))
    entry_HorasSol.place(x=190,y=190)
    entry_HorasSol.pack

    botao_Calcular = tk.Button(calculo, width=20, height=2, text= "Calcular", relief="flat", fg="#333333", font=("Arial 8 bold"), bg="#ffffff", command = calcular_sol)
    botao_Calcular.place(x=110, y=240)

    botao_voltar = tk.Button(calculo, width=7, height=2, text= "Fechar", relief="flat", fg="#333333", font=("Arial 8 bold"), bg="#ffffff", command = calculo.destroy)
    botao_voltar.place(x=265, y=295)

   
def abrir_carbonico():
    carbonico = tk.Toplevel()
    carbonico.title("EcoThink - Calculadora de Carbono")
    carbonico.geometry("350x350")
    carbonico.config(bg="#8CB243")
    carbonico.iconphoto(False, PhotoImage(file="icon_EcoThink.png"))
  
    def calcular_carbo():
        resultado = selecionado_1.get()
        energia = entry_energ.get()

        resultado = float(resultado)
        energia = float(energia)


        resposta = resultado*energia
        resposta2 = resposta/1000
        
        messagebox.showinfo("Resultado", f"A quantidade de CO2 mensal que seria gerada é de {resposta:.3f} kg.CO2, e a quantidade de Crédito de Carbono gerada é de {resposta2:.3f}")

    selecionado_1 = DoubleVar()  

    label_CalculaCarbono = Label(carbonico, width=43, height=2, text="Calculadora de Carbono", font=("Arial 10 bold"), fg="#ffffff", bg="#333333")
    label_CalculaCarbono.grid(row=0, column=0, padx=0, pady=0)

    label_energia = Label(carbonico, width=20, height=2, text="Energia mensal (kW):", font=("Arial 8 bold"), fg="#ffffff", bg="#333333")
    label_energia.place(x=40,y=70)

    entry_energ = tk.Entry(carbonico, font=("Arial 8 bold"))
    entry_energ.place(x=190, y=70)

    radio_natural = Radiobutton(carbonico, width=10, height=2, text="Gás natural", font=("Arial 8 bold"), fg="#333333", bg="#c0c0c0", value=0.202, variable=selecionado_1) 
    radio_natural.place(x=75, y=120)

    radio_diesel = Radiobutton(carbonico, width=10, height=2, text="Óleo diesel", font=("Arial 8 bold"), fg="#333333", bg="#c0c0c0", value=0.267, variable=selecionado_1) 
    radio_diesel.place(x=75, y=160)

    radio_petro = Radiobutton(carbonico, width=10, height=2, text="GLP", font=("Arial 8 bold"), fg="#333333", bg="#c0c0c0", value=0.227, variable=selecionado_1) 
    radio_petro.place(x=75, y=200)

    radio_Madeira = Radiobutton(carbonico, width=10, height=2, text="Madeira", font=("Arial 8 bold"), fg="#333333", bg="#c0c0c0", value=0.531, variable=selecionado_1) 
    radio_Madeira.place(x=175, y=120)

    radio_Gasolina = Radiobutton(carbonico, width=10, height=2, text="Gasolina", font=("Arial 8 bold"), fg="#333333", bg="#c0c0c0", value=0.249, variable=selecionado_1) 
    radio_Gasolina.place(x=175, y=160)

    radio_Etanol = Radiobutton(carbonico, width=10, height=2, text="Etanol", font=("Arial 8 bold"), fg="#333333", bg="#c0c0c0", value=0.248, variable=selecionado_1) 
    radio_Etanol.place(x=175, y=200)

    botao_Comparar = tk.Button(carbonico, width=20, height=2, text= "Calcular", relief="flat", fg="#333333", font=("Arial 8 bold"), bg="#ffffff", command = calcular_carbo)
    botao_Comparar.place(x=100, y=250)

    botao_voltarCarbonico = tk.Button(carbonico, width=7, height=2, text= "Fechar", relief="flat", fg="#333333", font=("Arial 8 bold"), bg="#ffffff", command = carbonico.destroy)
    botao_voltarCarbonico.place(x=265, y=295)

def abrir_simula():
    simula = tk.Toplevel()
    simula.title("EcoThink - Simulação")
    simula.geometry("350x350")
    simula.config(bg="#8CB243")
    simula.iconphoto(False, PhotoImage(file="icon_EcoThink.png"))


    def calcular_simula():
        Gasto = entry_Gasto.get()
        Valor = entry_Valor.get()
        Gerada = entry_Gerada.get()

        Gasto = float(Gasto)
        Valor = float(Valor)
        Gerada = float(Gerada)

        GastoTotal = Gasto * Valor
        ValorGerado = Gerada * Valor
        Porcentagem = (ValorGerado / GastoTotal) * 100

        messagebox.showinfo("Resultado", f"O seu gasto mensal com energia é de R${GastoTotal:.2f}. O valor da energia solar gerada é de R${ValorGerado:.2f}, e esse valor representa uma economia de {Porcentagem:.2f}% sobre seu gasto mensal")

    label_Simula = Label(simula, width=43, height=2, text="Simulação", font=("Arial 10 bold"), fg="#ffffff", bg="#333333")
    label_Simula.grid(row=0, column=0, padx=0, pady=0)

    label_Gasto = Label(simula, width=20, height=2, text="Gasto mensal (kW):", font=("Arial 8 bold"), fg="#ffffff", bg="#333333")
    label_Gasto.place(x=40,y=70)

    entry_Gasto = tk.Entry(simula, font=("Arial 8 bold"))
    entry_Gasto.place(x=190, y=70)

    label_Valor = Label(simula, width=20, height=2, text="Valor do kW (R$):", font=("Arial 8 bold"), fg="#ffffff", bg="#333333")
    label_Valor.place(x=40,y=110)

    entry_Valor = tk.Entry(simula, font=("Arial 8 bold"))
    entry_Valor.place(x=190, y=110)

    label_Gerada = Label(simula, width=20, height=2, text="Energia gerada (kW):", font=("Arial 8 bold"), fg="#ffffff", bg="#333333")
    label_Gerada.place(x=40,y=150)

    entry_Gerada = tk.Entry(simula, font=("Arial 8 bold"))
    entry_Gerada.place(x=190, y=150)

    botao_Compa = tk.Button(simula, width=20, height=2, text= "Calcular", relief="flat", fg="#333333", font=("Arial 8 bold"), bg="#ffffff", command = calcular_simula)
    botao_Compa.place(x=100, y=210)
    
    botao_voltarSimula = tk.Button(simula, width=7, height=2, text= "Fechar", relief="flat", fg="#333333", font=("Arial 8 bold"), bg="#ffffff", command = simula.destroy)
    botao_voltarSimula.place(x=265, y=295)

janela = tk.Tk()
janela.title("EcoThink - Menu")
janela.geometry("350x350")
janela.config(bg="#8CB243")
janela.iconphoto(False, PhotoImage(file="icon_EcoThink.png"))


label_menu = Label(janela, width=43, height=2, text="MENU", font=("Arial 10 bold"), fg="#ffffff", bg="#333333")
label_menu.grid(row=0, column=0, padx=0, pady=0)

imgCalculo=PhotoImage(file="icon_sol.png")
l_calculo=Label(janela, width=35, height=35, image=imgCalculo, bg="#f6ea99")
l_calculo.place(x=80, y=90)

botao_calculo = tk.Button(janela,width=20, height=2, text= "Calculadora Solar", fg="#333333", font=("Arial 8 bold"), bg="#ffffff", relief="flat", command = abrir_calculo)
botao_calculo.place(x=119, y=90)

imgCarbonico=PhotoImage(file="icon_carbono.png")
l_Carbonico=Label(janela, width=35, height=35, image=imgCarbonico, bg="#9c9980")
l_Carbonico.place(x=80, y=140)

botao_carbonico = tk.Button(janela,width=20, height=2, text= "Calculadora de Carbono", fg="#333333", font=("Arial 8 bold"), bg="#ffffff", relief="flat", command = abrir_carbonico)
botao_carbonico.place(x=119, y=140)

imgSimula=PhotoImage(file="icon_simula.png")
l_Simula=Label(janela, width=35, height=35, image=imgSimula, bg="#698a96")
l_Simula.place(x=80, y=190)

botao_simulacao = tk.Button(janela,width=20, height=2, text= "Simulação", relief="flat", fg="#333333", font=("Arial 8 bold"), bg="#ffffff", command = abrir_simula)
botao_simulacao.place(x=119, y=190)

imgFechar=PhotoImage(file="icon_fechar.png")
l_Fechar=Label(janela, width=35, height=35, image=imgFechar, bg="#ffdbbf")
l_Fechar.place(x=80, y=240)


botao_fechar = tk.Button(janela,width=20, height=2, text= "Fechar", relief="flat", fg="#333333", font=("Arial 8 bold"), bg="#ffffff", command = janela.destroy)
botao_fechar.place(x=119, y=240)

janela.mainloop()
