# Esteban Vergara Giraldo
# Análisis Numérico
# Convertidor de número base 10 (con posibles cifras decimales) a número máquina

def conversion_binario(numero_decimal : int | float, exponente10 : int = 0, invertido : bool = False) -> dict:
    '''Convierte el entero decimal que le manden en una lista con las posiciones del binario
    
    Args:
        numero_decimal: Un número base 10 enviado en cualquier tipo numérico.

        exponente10: Exponente en base 10 del número ingresado, así permite el uso de notación científica.

        invertido: Un booleano que indica si se quiere el output con la cifra menos significativa a la izquierda o a la derecha. Por default es False. (4, false) = 100 || (4, true) = 001.

    Returns:
        Un diccionario con los tipos de output que se podrían necesitar de su binario correspondiente.
    '''

    # 0 = negativo || 1 = positivo
    signo = 0 if numero_decimal < 0 else 1  

    if exponente10 != 0:
        numero_decimal = numero_decimal * (10 ** exponente10)
        exponente10 = 0

    exponente2 = 0
    if numero_decimal%1 != 0:
        numero_decimal, exponente2 = buscar_potencia2(numero_decimal)

    # Si el número ya es 0 o 1, no es necesaria la conversión.
    if numero_decimal == 0:
        return {
        'list'      : [0],
        'str'       : '0',
        'int'       : 0,
        'float'     : 0.0,    # Conversión común
        'exponente2': 0,
        'signo'     : 1
    }

    if numero_decimal == 1:
        return {
        'list'      : [1],
        'str'       : '1',
        'int'       : 1,
        'float'     : 1.0,    # Conversión común
        'exponente2': 1,
        'signo'     : 1
    }

    if numero_decimal == -1:
        return {
        'list'      : [1],
        'str'       : '1',
        'int'       : 1,
        'float'     : 1.0,    # Conversión común
        'exponente2': 1,
        'signo'     : 0
    }
    
    lista_binario = []
    while numero_decimal > 1:
        lista_binario.append(int(numero_decimal % 2))
        numero_decimal = numero_decimal//2
    lista_binario.append(int(numero_decimal))

    if not invertido:
        lista_binario.reverse()

    str_binario = ''.join(map(str,lista_binario))

    return {
        'list'      : lista_binario,
        'str'       : str_binario,
        'int'       : int(str_binario),
        'float'     : float(str_binario)*(10**exponente2),    # Conversión común
        'exponente2': exponente2,
        'signo'     : signo
    }


def buscar_potencia2(numero_decimal : float) -> tuple[float, int]:
    exponente2 = 0
    while numero_decimal%1 != 0:
        exponente2 += 1
        numero_decimal += numero_decimal

    return numero_decimal , -exponente2


def punto_flotante(lista_binario, exponente2, bits_mantisa, redondeo : str = 's') -> dict:
    exponente2 = exponente2+len(lista_binario)
    lista_binario = lista_binario[:bits_mantisa+2]

    # Redondeo simétrico, defaut
    if redondeo == 's':
        try:
            if lista_binario[bits_mantisa+1] == 1:
                lista_binario = lista_binario[:-1]
                lista_binario, suma_exponente = binario_plus1(lista_binario)
                exponente2 += suma_exponente    # En caso de que se cree una cifra nueva y haya que correr el punto.
            else:
                lista_binario = lista_binario[:-1]
        except:
            pass
    
    # Redondeo hacia abajo, corte
    elif redondeo == 'c':
        lista_binario = lista_binario[:-1]
    
    # Redondeo hacia arriba, exceso
    elif redondeo == 'e':
        lista_binario = lista_binario[:-1]
        lista_binario, suma_exponente = binario_plus1(lista_binario)
        exponente2 += suma_exponente
    

    return {
        'list'      : lista_binario,
        'float'     : float(''.join(map(str,lista_binario))),
        'exponente2': exponente2
    }
    

def binario_plus1(lista_binario : list) -> tuple[list, int]:

    # Para iterar de izquierda a derecha
    lista_binario.reverse()

    # Se le pone 1 a la primera posición en donde haya un 0.
    # Todos los 1 que se encuentren en el camino se convierten en 0
    for i in range(len(lista_binario)):
        if lista_binario[i] == 1:
            lista_binario[i] = 0
        else: 
            lista_binario[i] = 1
            lista_binario.reverse()
            return lista_binario, 0  # El exponente permanece sin cambios
        
    # Si no se encontró un 0, habrá que crear una cifra más y aumentarle 1 al exponente
    # 111 -> 100 y +1 al exponente
        
    lista_binario[0] = 1
    return lista_binario, 1


def binario_a_decimal(binario : list, signo_mantisa : str, exponente : int) -> list:
    decimal = 0
    for i in [1]+binario:
        exponente -= 1
        decimal += i * (2**exponente)

    return decimal if signo_mantisa == '1' else -decimal



# -----------------------------------------------------------------------------

#print(binario_plus1([1,0,1]))

#print(conversion_binario_con_decimales(float(input())))

#print(conversion_binario(float(input())))

#exit()

if __name__ == '__main__':
    bits_mantisa    = int(input('Ingrese los bits para la mantisa -> '))
    bits_exponente  = int(input('Ingrese los bits para el exponente -> '))
    numero_decimal  = float(input('Ingrese el número decimal -> '))
    exponente10     = input('Ingrese el exponente -> ')                     # No obligatorio.
    redondeo        = input('Ingrese el tipo de redondeo (c/e/s) -> ')      # No obligatorio.

    exponente10 =  0    if exponente10 == ''    else int(exponente10)
    redondeo    = 's'   if redondeo == ''       else redondeo


    diccionario_binario     = conversion_binario(numero_decimal, exponente10)
    numero_binario_exacto   = diccionario_binario['float']
    lista_binario           = diccionario_binario['list']
    exponente2              = diccionario_binario['exponente2']
    signo_mantisa           = diccionario_binario['signo']

    #print(lista_binario, len(lista_binario), exponente2)

    diccionario_flotante    = punto_flotante(lista_binario, exponente2, bits_mantisa, redondeo)
    numero_binario_guardado = diccionario_flotante['float']
    lista_binario_2         = diccionario_flotante['list']
    exponente2              = diccionario_flotante['exponente2']

    #print(lista_binario_2, exponente2)

    diccionario_exponente = conversion_binario(exponente2)
    exponente2_binario  = diccionario_exponente['list']
    signo_exponente     = diccionario_exponente['signo']

    #print(exponente2_binario)

    # El número es tan grande o pequeño que su exponente no cabe en sus bits reservados
    if len(exponente2_binario) > bits_exponente:
        if signo_exponente == 1:
            print('Overflow')
        else:
            print('Underflow')
        exit()

    # Rellenar los ceros a la izquierda en los bits del exponente
    lista_exponente =  [0 for _ in range(bits_exponente-len(exponente2_binario))] + exponente2_binario

    # Rellenar los ceros a la derecha en los bits de la mantisa
    lista_binario_2 = lista_binario_2 + [0 for _ in range(bits_mantisa-len(lista_binario_2))]

    lista_numero_maquina = [signo_mantisa , signo_exponente] + lista_binario_2[1:] + lista_exponente
    numero_maquina = ''.join(map(str,lista_numero_maquina))

    numero_decimal_guardado = binario_a_decimal(lista_binario_2[1:], str(signo_mantisa), exponente2)

    # Comprobación de los pasos
    
    '''
    print(diccionario_binario)
    print(diccionario_flotante)
    print(diccionario_exponente)
    '''

    # --------------------------------------------------------------

    print('-'*50)
    print('Número original:', numero_decimal, '(10) \t| ', numero_binario_exacto, '(2)')
    print('Número guardado:', numero_decimal_guardado, '(10) \t| ' , f'0.{int(numero_binario_guardado)}', f'x2^{exponente2} (2)')
    print('Error absoluto:', abs(numero_decimal - numero_decimal_guardado))
    print('Error relativo:', abs((numero_decimal - numero_decimal_guardado)/numero_decimal))

    # --------------------------------------------------------------
    
    print('\nMantisa:\t', signo_mantisa, ' |  1' ,lista_binario_2[1:])
    print('Exponente:\t', signo_exponente, ' |   ' ,lista_exponente)
    print('Número máquina:', lista_numero_maquina, ' = ', numero_maquina, ' = ', numero_maquina[:2], numero_maquina[2:2+bits_mantisa], numero_maquina[2+bits_mantisa:])

