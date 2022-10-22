from variables import *

def bienvenida():
    print("\b")
    alias = input("Ingresa su Alias del usuario: ".upper())
    print(f"{'El alias del usuario es:'.upper()} {alias}")
    print("\b")
    return alias

def seccion_1():
    print(banner)
    print("\b")
    print(f"1) {titulo1.upper()} {nombre} ")
    print("\b")

def seccion_2():
    print(f"2) {titulo2.upper()} {version} ")
    print("\b")

def seccion_3():
    print(f"3) {mensaje.upper()} {mensaje_verano} ")
    print("\b")

def seccion_4(alias):
    print(f"4) {'Hey'.upper()} {alias} {mensaje_tips.upper()} {nombre.upper()}: ")
    print("\b")
    for item in lista_ayuda: 
        print(f"- {item.title()}")

    print("\b")

    print(banner)