from functions.inputs import *

def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False

def run():
    palabra = get_input(str, "Escribe una palabra: ", "un texto valido")
    es_palindromo = palindromo(palabra)

    if es_palindromo == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")

if __name__ == '__main__':
    run()