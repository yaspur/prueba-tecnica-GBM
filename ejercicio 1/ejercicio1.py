def palindromo(texto):
    cadena = texto.replace(' ', '')
    return cadena == cadena[::-1]

def main():
    texto = input("Ingrese palabra o frase a verificar: ")
    print(palindromo(texto))

if __name__ == '__main__':
    main()