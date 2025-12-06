import tkinter as tk
from tkinter import font, filedialog, messagebox
from config import TITULO, COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_PANEL_PRINCIPAL
from util.util_ventana import centrar_ventana, cargar_fuente_memoria, resolver_ruta
from util.util_imagenes import leer_imagen
import pygame
import os

ruta = ""
estado = ""
nombre_archivo = "<No se ha seleccionado un archivo>"

def bind_hover_events(button):
    button.bind("<Enter>", lambda event:on_enter(event,button))
    button.bind("<Leave>",lambda event:on_leave(event,button))

def on_enter(event,button):
    button.config(bg="#575858")

def on_leave(event,button):
    button.config(bg=COLOR_MENU_LATERAL)

def toggle_panel():
    if menu_lateral.winfo_ismapped():
        menu_lateral.pack_forget()
    else:
        menu_lateral.pack(side=tk.LEFT, fill="y")

def limpiar_panel(panel):
    for widget in panel.winfo_children():
        widget.destroy()

def mostrar_inicio():
    limpiar_panel(panel_principal)
    tk.Label(panel_principal, text="Inicio", font=("fontawesome", 22)).pack(pady=20)

def mostrar_ventas():
    limpiar_panel(panel_principal)
    tk.Label(panel_principal, text="Ventas", font=("fontawesome", 22)).pack(pady=20)

def mostrar_productos():
    limpiar_panel(panel_principal)
    tk.Label(panel_principal, text="Productos", font=("fontawesome", 22)).pack(pady=20)

def mostrar_reportes():
    limpiar_panel(panel_principal)
    tk.Label(panel_principal, text="Reportes", font=("fontawesome", 22)).pack(pady=20)

def mostrar_usuarios():
    limpiar_panel(panel_principal)
    tk.Label(panel_principal, text="Usuarios", font=("fontawesome", 22)).pack(pady=20)

def salir_app():
    root.destroy()  

root = tk.Tk()
root.title(TITULO)

icon = tk.PhotoImage(file="C:/Users/USUARIO/Desktop/Practicas 3 programacion/graficos/imagenes/sales.png")
root.iconphoto(False, icon)

centrar_ventana(root, 1024, 600)

barra_superior = tk.Frame(root, height=50, bg=COLOR_BARRA_SUPERIOR)
barra_superior.pack(side=tk.TOP, fill="both")

menu_lateral = tk.Frame(root, width=150, bg=COLOR_MENU_LATERAL)
menu_lateral.pack(side=tk.LEFT, fill="both", expand=False)

panel_principal = tk.Frame(root, bg=COLOR_PANEL_PRINCIPAL)
panel_principal.pack(side=tk.RIGHT, fill="both", expand=True)

fontawesome = font.Font(family="Font Awesome 7 Free", size=20)

btn_menu = tk.Button(
    barra_superior, text="\uf0c9", font=fontawesome,
    bg=COLOR_BARRA_SUPERIOR, fg="#000000",
    bd=0, command=toggle_panel
)
btn_menu.pack(padx=10, pady=10, side=tk.LEFT)

label = tk.Label(
    barra_superior, text="Menu de Supermercado", font="Roboto 24",
    bg=COLOR_BARRA_SUPERIOR, fg="#000000"
)
label.pack(padx=10, pady=10, side=tk.LEFT)

imagen_perfil = leer_imagen(
    "C:/Users/USUARIO/Desktop/Practicas 3 programacion/graficos/imagenes/profile.png",
    (100, 100)
)
label_perfil = tk.Label(menu_lateral, bg=COLOR_MENU_LATERAL, image=imagen_perfil)
label_perfil.pack(side=tk.TOP, pady=20)

btn_inicio = tk.Button(menu_lateral, text="\uf015 Inicio", bg=COLOR_MENU_LATERAL,
                       fg="#4DA6FF", bd=0, width=12, font=fontawesome,
                       command=mostrar_inicio)
btn_inicio.pack(side=tk.TOP)

btn_ventas = tk.Button(menu_lateral, text="\uf4c0 Ventas", bg=COLOR_MENU_LATERAL,
                       fg="#1C8B00", bd=0, width=12, font=fontawesome,
                       command=mostrar_ventas)
btn_ventas.pack(side=tk.TOP)

btn_productos = tk.Button(menu_lateral, text="\uf468 Productos", bg=COLOR_MENU_LATERAL,
                          fg="#CC7A00", bd=0, width=12, font=fontawesome,
                          command=mostrar_productos)
btn_productos.pack(side=tk.TOP)

btn_reportes = tk.Button(menu_lateral, text="\uf201 Reportes", bg=COLOR_MENU_LATERAL,
                         fg="#6b0000", bd=0, width=12, font=fontawesome,
                         command=mostrar_reportes)
btn_reportes.pack(side=tk.TOP)

btn_usuarios = tk.Button(menu_lateral, text="\uf007 Usuarios", bg=COLOR_MENU_LATERAL,
                         fg="#751ACA", bd=0, width=12, font=fontawesome,
                         command=mostrar_usuarios)
btn_usuarios.pack(side=tk.TOP)

btn_salir = tk.Button(menu_lateral, text="\uf2f6 Salir", bg=COLOR_MENU_LATERAL,
                      fg="#ff0000", bd=0, width=12, font=fontawesome,
                      command=salir_app)
btn_salir.pack(side=tk.BOTTOM)

for b in [btn_inicio, btn_ventas, btn_productos, btn_reportes, btn_usuarios, btn_salir]:
    bind_hover_events(b)

root.mainloop()