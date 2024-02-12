def binario_a_decimal(binario : list, signo_mantisa : str, exponente : int) -> list:
    decimal = 0
    for i in [1]+binario:
        exponente -= 1
        decimal += i * (2**exponente)

    return decimal if signo_mantisa == '1' else -decimal

    

if __name__ == '__main__':
    signo_mantisa   = input('Ingrese el signo de la mantisa (-0 | 1+) -> ')
    signo_exponente = input('Ingrese el signo del exponente (-0 | 1+) -> ')
    bits_mantisa    = input('Ingrese los bits de la mantisa -> ')
    bits_exponente  = input('Ingrese los bits del exponente -> ')

    print(signo_mantisa, signo_exponente, bits_mantisa, bits_exponente)
    c = input('Es este el número que desea convertir? (s/n) -> ')

    # Mero raro nea
    if c == 'n':
        print('La re buena pa')
        exit()


    # Se puede convertir directamente
    exponente = int(bits_exponente, 2) if signo_exponente == '1' else -int(bits_exponente, 2)

    lista_mantisa = list(map(int, list(bits_mantisa)))

    decimal = binario_a_decimal(lista_mantisa, signo_mantisa, exponente)

    print(decimal)



    
