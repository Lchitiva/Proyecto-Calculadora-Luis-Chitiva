import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

window = tk.Tk() 
select=tk.IntVar()

def init_window():
    
    
    window.title('Mi primera aplicación')  
    window.geometry('400x250') 
 

    label = tk.Label(window, text='Calculadora', font =('Arial bold',15))
    label.grid(column=0,row=0)

    entrada1 = tk.Entry(window,width=10)
    entrada2 = tk.Entry(window,width=10)
    entrada1.grid(column=1,row=1)
    entrada2.grid(column=1,row=2)
    
    label_entrada1 = tk.Label(window, text='Ingrese primer número', font =('Arial bold',10))
    label_entrada1.grid(column=0,row=1)

    label_entrada2 = tk.Label(window, text='Ingrese segundo número', font =('Arial bold',10))
    label_entrada2.grid(column=0,row=2)

    label_operador=tk.Label(window,text= 'Escoja un operador',font=('Arial bold',10))
    label_operador.grid(column=0,row=3)

    combo_operadores=ttk.Combobox(window)
    combo_operadores['values']=['+','-','*','/','^']
    combo_operadores.current(0)
    combo_operadores.grid(column=1,row=3)

    label_resultado=tk.Label(window, text='Resultado: ',font=('Arial bold',15))
    label_resultado.grid(column=0,row=5)
    
    chk_state = IntVar()

    chk = Checkbutton(window, text='Con decimales', var=chk_state)

    chk.grid(column=2, row=5)
    
    boton= tk.Button(window,
                    command=lambda : click_calcular(
                        label_resultado,
                        entrada1.get(),
                        entrada2.get(),
                        combo_operadores.get(),
                        chk_state.get()),
                        text='Calcular',
                        bg='blue',
                        fg='cyan')
    boton.grid(column=1,row=5)
    
    rad1 = Radiobutton(window,text='Modo Fuxia', value=1,variable=select,command=fondo)
    rad2 = Radiobutton(window,text='Modo Cyan',value=2, variable=select,command=fondo)
    rad3 = Radiobutton(window,text='Modo Oscuro',value=3, variable=select,command=fondo)
    rad4 = Radiobutton(window,text='Modo Claro',value=4, variable=select,command=fondo)

    rad1.grid(column=2, row=1)
    rad2.grid(column=2, row=2)
    rad3.grid(column=2, row=3)
    rad4.grid(column=2, row=4)
    
    ayuda = Button(window,text='Ayuda', command=ayudame)

    ayuda.grid(column=1,row=6)




    window.mainloop() 
def ayudame():

    messagebox.showinfo('Ayuda', 'Buen día, recuerde no dividir entre 0 ya que el resultado está indeterminado.\nPara cambiar el color de fondo use los botones de modo que se encuentran a la derecha.\nRecuerde que si quiere su resultado con decimales, solo debe hacer click en el botón "Con decimales".\nEl símbolo "^" sirve para elevar un número a una potencia.')


def fondo():
    if select.get()==1:
        window.config(bg='#DF29FF')
        
    elif select.get()==2:
        window.config(bg='#00FFA9')
    elif select.get()==3:
        window.config(bg='#00200F')
    else:
        window.config(bg='white')

    

def calculadora(num1,num2,operador):
    if operador == '+':
        resultado=num1+num2
    elif operador == '-':
        resultado=num1-num2
    elif operador == '*':
        resultado=num1*num2
    elif operador == '/':
        resultado=round(num1/num2,2)
    else:
        resultado=num1**num2
    return resultado
def click_calcular(label,num1,num2,operador,n):
    valor1=float(num1)
    valor2=float(num2)

    res=calculadora(valor1, valor2, operador)
    resul=int(res)
    if n==1 or n==True:
        label.configure(text='Resultado: '+str(res))
    else:
        label.configure(text='Resultado: '+str(resul))



    
    
def main():
    init_window()
main()
