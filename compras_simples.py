##  sudo apt-get install python-tk
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
    from Tkinter import ttk
    from Tkinter import messagebox
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
    from tkinter import ttk
    from tkinter import messagebox


def botao_novo_click():
    label_Fim["text"] = '...'
    label_produtocompra["text"] =  '...'
    label_precocompra["text"] =  '...'
    label_qtdcompra["text"] = '...'
    label_TotalCompra["text"] = '...'
    produto_nome.delete(0, 'end')
    produto_preco.delete(0, 'end')
    produto_qtde.delete(0, 'end')
    valor_recebido.delete(0, 'end')
    produto_nome.focus()

def botao_verficar_troco_click():
    total_compra = float(produto_preco.get()) * float(produto_qtde.get())
    troco = float(valor_recebido.get())-float(total_compra)
    if float(valor_recebido.get()) > total_compra:
       label_Fim["text"] = " Obrigado! Seu troco é: " + str(troco)
    elif float(valor_recebido.get()) < total_compra:
        messagebox.showwarning("Atenção","Valor recebido é menor do que o Total da Compra, Socilite o restante: "+ str(troco*-1))
    else:
       label_Fim["text"] = " Obrigado! Volte Sempre!" 

def botao_calcular_click():
    print("botao_calcular_click")
    label_produtocompra["text"] = "P= "+ produto_nome.get()
    label_precocompra["text"] = "R$ " + produto_preco.get()
    label_qtdcompra["text"] = " X " + produto_qtde.get()
    total_compra = float(produto_preco.get()) * float(produto_qtde.get())
    label_TotalCompra["text"]="Total da Compra: " + str(total_compra)


formulario =Tk()
formulario.title("Sistema de Compras - Simples")

#- Solicitar o nome do produto
label_nome_produto= Label(formulario, text="Qual é o nome do produto?")
label_nome_produto.place(x=20,y=30)
produto_nome = Entry(formulario)
produto_nome.place(x=20, y=50)

#- Solicitar o preço do produto
label_preco_produto = Label(formulario, text="Qual é o preço do produto?")
label_preco_produto.place(x=20,y=70)
produto_preco = Entry(formulario)
produto_preco.place(x=20, y=90)

# - Solicitar o qtde do produto
label_qtd_produto = Label(formulario, text="Qual é o qtde do produto?")
label_qtd_produto.place(x=20,y=110)
produto_qtde = Entry(formulario)
produto_qtde.place(x=20, y=130)
# - Calcular 
botao_calcular = Button(formulario,text="Calcular", width=18, command=botao_calcular_click)
botao_calcular.place(x=20,y=150)
# - Total Compra
label_TotalCompra = Label(formulario, text="..." )
label_TotalCompra.place(x=220,y=180)
# - Solicitar o valor de pagamento (dinheiro)
label_valor_recebido = Label(formulario, text="Valor a receber em dinheiro:")
label_valor_recebido.place(x=20,y=210)
valor_recebido = Entry(formulario)
valor_recebido.place(x=20, y=240)  
# - Troco 
botao_fecha_compra = Button(formulario,text="Fechar Compra", width=18, command=botao_verficar_troco_click)
botao_fecha_compra.place(x=20,y=260)
# - Nova compra 
botao_nova_compra = Button(formulario,text="Nova Compra", width=18, command=botao_novo_click)
botao_nova_compra.place(x=20,y=300)

label_mensagem = Label(formulario, text=".....:: R E C I B O ::......")
label_mensagem.place(x=220,y=30)
label_produtocompra = Label(formulario, text="...")
label_produtocompra.place(x=220,y=50)
label_precocompra = Label(formulario, text="...")
label_precocompra.place(x=220,y=90)
label_qtdcompra = Label(formulario, text="...")
label_qtdcompra.place(x=220,y=130)
label_Fim = Label(formulario, text="..." )
label_Fim.place(x=220,y=200)

formulario.geometry("500x400+220+220")
formulario.mainloop()


