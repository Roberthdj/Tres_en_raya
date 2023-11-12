
from random import randrange


def mostrar_tablero(tablero):
    for row in range(len(tablero)):
        print('+-------+-------+-------+')
        print('|       |       |       |', end='\n|')
        for col in range(len(tablero[row])):
            print('  ', str(tablero[row][col]), end='   |')
        print('\n|       |       |       |')
    print('+-------+-------+-------+')


def movimiento_persona(tablero):
    campos_libres = crear_lista_de_campos_libres(tablero)

    try:
        seleccionar_celda = int(input('Ingresa tu movimiento:'))
        if (seleccionar_celda > 0 and seleccionar_celda < 10) and (seleccionar_celda not in lista_de_celdas_seleccionadas):
            for i in range(len(campos_libres)):
                row, col = campos_libres[i]
                if seleccionar_celda == tablero[row][col]:
                    lista_de_celdas_seleccionadas.append(tablero[row][col])
                    tablero[row][col] = 'O'

            mostrar_tablero(tablero)
            return victoria_para(tablero, 'O')

        else:
            print('Error!, ingrese un valor valido!...')
            movimiento_persona(tablero)
            return True
    except:
        print('Error!, ingrese un valor valido!')
        movimiento_persona(tablero)
        return True


def crear_lista_de_campos_libres(tablero):
    lista_de_campos_libres = []
    for row in range(len(tablero)):
        for col in range(len(tablero[row])):
            if tablero[row][col] != 'X' and tablero[row][col] != 'O':
                lista_de_campos_libres.append((row, col))
    return lista_de_campos_libres


def victoria_para(tablero, sign):
    campos_libres = crear_lista_de_campos_libres(tablero)

#   Comprobando diagonales
    contador_1 = contador_2 = 0
    for pos in range(len(tablero)):
        if sign == tablero[pos][pos]:
            contador_1 += 1
        if sign == tablero[pos][2-pos]:
            contador_2 += 1
    if contador_1 == 3 or contador_2 == 3:
        print('Las ' + sign + ' han ganado!')
        return False

#   Comprobando filas y columnas
    for row in range(len(tablero)):
        contador_1 = contador_2 = 0
        for column in range(len(tablero[row])):
            if sign == tablero[column][row]:
                contador_1 += 1
            if sign == tablero[row][column]:
                contador_2 += 1
        if contador_1 == 3 or contador_2 == 3:
            print('Las ' + sign + ' han ganado!')
            return False

#   Comprobar empate
    if len(campos_libres) == 0:
        print('Ha sido un empate!')
        return False

    return True


def movimiento_maquina(tablero):
    if tablero[1][1] == 5:
        tablero[1][1] = 'X'
        mostrar_tablero(tablero)
        return True

    campos_libres = crear_lista_de_campos_libres(tablero)
    number = randrange(len(campos_libres))
    row, col = campos_libres[number]
    lista_de_celdas_seleccionadas.append(tablero[row][col])
    tablero[row][col] = 'X'
    mostrar_tablero(tablero)
    return victoria_para(tablero, 'X')


if __name__ == '__main__':

    tablero = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    lista_de_celdas_seleccionadas = [5]
    flag = True

    while flag:
        flag = (movimiento_maquina(tablero) and movimiento_persona(tablero))
