import tkinter as tk
root = tk.Tk()
root.title("Calculadora")
root.geometry("305x380")

botones_texto= ("AC","/","*","-",
                "7","8","9","+",
                "4","5","6","",
                "1","2","3","=",
                "0","",".","")

def click_botones(valor):
    if valor == "=":
        try:
            expresion = resultado.get()
            evaluacion = eval(expresion)
            resultado.delete(0,tk.END)
            resultado.insert(tk.END,str(evaluacion))
            historico.config(text=expresion+"=")

        except Exception as e:
            resultado.delete(0,tk.END)
            resultado.insert(tk.END,"Error")
            historico.config(text="")
    elif valor == "AC":
            resultado.delete(0,tk.END)
            resultado.insert(tk.END,"")
            historico.config(text="")
    else:
        current_text = resultado.get()
        resultado.delete(0,tk.END)
        resultado.insert(tk.END,current_text+valor)


historico = tk.Label(root
                    ,bg="#f2f2f2"
                    ,font="Roboto 14"
                    ,width=15
                    ,bd=0
                    ,justify="right"
                    )

historico.pack(pady=5, padx=5, fill="x")

resultado = tk.Entry(root
                      ,bg="#ffffff"
                      ,bd=1
                      ,font="Roboto 24"
                      ,width=15
                      ,justify="right"
                    )

resultado.pack(padx=10,fill="x")

contenedor_botones = tk.Frame(root,bg="#898787")
contenedor_botones.pack(pady=5,padx=10, fill="both")

acumulador=0
for row in range(5):
    for column in range(4):
        boton = tk.Button(contenedor_botones
                          ,text=botones_texto[acumulador]
                          ,bg="#000000"
                          ,fg="#F3F3F3"
                          ,font="Roboto 20"
                          ,bd=0
                          ,width=4
                          ,command=lambda b=botones_texto[acumulador]: click_botones(b)
                          )
                
        if botones_texto[acumulador]=="AC":
            boton.config(bg="#FF0000")
        elif botones_texto[acumulador] in ("/","*","-","+"):
            boton.config(bg="#006EFF")

        if botones_texto[acumulador] != "":
            
            if botones_texto[acumulador] == "+":
                boton.config(height=3)
                boton.grid(row=row, column=column 
                           , rowspan=2, padx=1, pady=1)
                
            elif botones_texto[acumulador] == "=":
                boton.config(height=3, bg="#E78D16")
                boton.grid(row=row, column=column 
                           , rowspan=2, padx=1, pady=1)
            
            elif botones_texto[acumulador] == "0":
                boton.config(width=8)
                boton.grid(row=row, column=column 
                           , columnspan=2, padx=1, pady=1)
                           
            else:
                boton.grid(row=row, column=column, padx=1, pady=1)

        acumulador+=1

root.mainloop()