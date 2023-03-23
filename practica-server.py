#!/usr/bin python3

import socket
import random
import pickle
import json
import time


#   Configuracion del servidor
HOST = "127.0.0.1"  # Direccion de la interfaz de loopback estándar (localhost)
PORT = 65432  # Puerto que usa el cliente  (los puertos sin provilegios son > 1023)
buffer_size = 2048

#   Dificultad del juego
principiante = (9, 9, 10)
avanzado = (16, 16, 40)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:  # Creamos el mismo tipo de socket
    TCPServerSocket.bind((HOST, PORT)) # Nos va a ser la liga entre el coket y la dirección IP
    TCPServerSocket.listen() # Para poder aceptar conexciones
    print("Servidor de Buscaminas activo")

    # Al momento de aceptarlo el resultado se va a asignar a dos variables
    Client_conn, Client_addr = TCPServerSocket.accept() # Una vez que el evento de solicitud de conexion pasa
    with Client_conn: # Hacemos un open a esa conexion
        print("Conectado a", Client_addr) # Imprimimos la conección e información del cliente
        print("Enviando mensaje y solicitud")
        Client_conn.sendall(b"Bienvenido al Buscaminas \n (P) Principiante \n (A) Avanzado \nElige la dificultad: ")

        print("Esperando a recibir datos... ")
        dato = Client_conn.recv(buffer_size).decode()
        print("Eligio el nivel " + dato)

        if dato == "p" or dato == "P":
            print("Dificultad principiante \n")
            filas, columnas, minas = principiante
            dificultad = "p"
            tablero_vista = "A B C D E F G H I"
        elif dato == "a" or dato == "A":
            print("Dificultad avanzado \n")
            filas, columnas, minas = avanzado
            dificultad = "a"
            tablero_vista = " A B C D E F G H I J K L M N Ñ O"
        else:
            print("Esta opción no existe \n")


        #   Generamos el juego y colocamos las minas
        tablero = [[0 for j in range(columnas)] for i in range(filas)]  # genera el tablero
        minas_colocadas = 0
        while minas_colocadas < minas:
            fila = random.randint(0, filas - 1)
            columna = random.randint(0, columnas - 1)
            if tablero[fila][columna] != -1:
                tablero[fila][columna] = -1
                minas_colocadas += 1

        #Client_conn.sendall(tablero_vista.encode())
        #Client_conn.recv(buffer_size) # Recibe la cadena "Letra"



        tablero_vista = [[0 for j in range(columnas)] for i in range(filas)]  # genera el tablero que se va a ver
        coordenada = []

        for i in range(filas):
            for j in range(columnas):
                    tablero_vista[i][j] = "- "



        if dificultad == "p":
            gano = 0
            perdio = 0
            llave = 0
            repetir = 0
            while gano != 1 or perdio != 1:

                # Enviamos el tablero
                tablero_v = "\n".join([" ".join(fila) for fila in tablero_vista])
                Client_conn.sendall(tablero_v.encode())

                # ------------------------------------------------------------------------------------------------------------
                # Recibe la coordenada
                print("Esperando a recibir coordenadas...")

                #Se recibe la columna que envio el cliente

                columna_letra = Client_conn.recv(buffer_size).decode()
                print(columna_letra)


                #Se recibe la fila que envio el cliente
                fila_letra = Client_conn.recv(buffer_size).decode()
                print(fila_letra)

                if fila_letra == "1":
                    fila = 0
                elif fila_letra == "2":
                    fila = 1
                elif fila_letra == "3":
                    fila = 2
                elif fila_letra == "4":
                    fila = 3
                elif fila_letra == "5":
                    fila = 4
                elif fila_letra == "6":
                    fila = 5
                elif fila_letra == "7":
                    fila = 6
                elif fila_letra == "8":
                    fila = 7
                elif fila_letra == "9":
                    fila = 8
                else:
                    print("Esta opcion no es valida")


                if columna_letra == "A" or columna_letra == "a":
                    columna = 0
                elif columna_letra == "B" or columna_letra == "b":
                    columna = 1
                elif columna_letra == "C" or columna_letra == "c":
                    columna = 2
                elif columna_letra == "D" or columna_letra == "d":
                    columna = 3
                elif columna_letra == "E" or columna_letra == "e":
                    columna = 4
                elif columna_letra == "F" or columna_letra == "f":
                    columna = 5
                elif columna_letra == "G" or columna_letra == "g":
                    columna = 6
                elif columna_letra == "H" or columna_letra == "h":
                    columna = 7
                elif columna_letra == "I" or columna_letra == "i":
                    columna = 8
                else:
                    print("Esta opcion no es valida")

                print("columna:")
                print(columna)
                print("fila:")
                print(fila)

                tablero_vista[fila][columna] = "X "
                tablero[fila][columna] = 1

                if tablero[fila][columna] == -1:
                    perdio = 1
                    Client_conn.sendall(b"p")
                else:
                    #Client_conn.sendall(b"Estuviste cerca")
                    Client_conn.sendall(b"s")
        else:
            gano = 0
            perdio = 0
            llave = 0
            repetir = 0
            while gano != 1 or perdio != 1:
                # Enviamos el tablero
                tablero_v = "\n".join([" ".join(fila) for fila in tablero_vista])
                Client_conn.sendall(tablero_v.encode())

                # --------------------------------------------------------------------------------
                # Recibe la coordenada
                print("Esperando a recibir coordenadas...")

                # Se recibe la columna que envio el cliente
                columna_letra = Client_conn.recv(buffer_size).decode().strip().lower()
                print(columna_letra)

                # Se recibe la fila que envio el cliente
                fila_letra = Client_conn.recv(buffer_size).decode().strip().lower()
                print(fila_letra)

                if fila_letra == "1":
                    fila = 0
                elif fila_letra == "2":
                    fila = 1
                elif fila_letra == "3":
                    fila = 2
                elif fila_letra == "4":
                    fila = 3
                elif fila_letra == "5":
                    fila = 4
                elif fila_letra == "6":
                    fila = 5
                elif fila_letra == "7":
                    fila = 6
                elif fila_letra == "8":
                    fila = 7
                elif fila_letra == "9":
                    fila = 8
                elif fila_letra == "10":
                    fila = 9
                elif fila_letra == "11":
                    fila = 10
                elif fila_letra == "12":
                    fila = 11
                elif fila_letra == "13":
                    fila = 12
                elif fila_letra == "14":
                    fila = 13
                elif fila_letra == "15":
                    fila = 14
                elif fila_letra == "16":
                    fila = 15
                else:
                    print("Esta opcion no es valida")

                if columna_letra == "A" or columna_letra == "a":
                    columna = 0
                elif columna_letra == "B" or columna_letra == "b":
                    columna = 1
                elif columna_letra == "C" or columna_letra == "c":
                    columna = 2
                elif columna_letra == "D" or columna_letra == "d":
                    columna = 3
                elif columna_letra == "E" or columna_letra == "e":
                    columna = 4
                elif columna_letra == "F" or columna_letra == "f":
                    columna = 5
                elif columna_letra == "G" or columna_letra == "g":
                    columna = 6
                elif columna_letra == "H" or columna_letra == "h":
                    columna = 7
                elif columna_letra == "I" or columna_letra == "i":
                    columna = 8
                elif columna_letra == "J" or columna_letra == "j":
                    columna = 8
                elif columna_letra == "K" or columna_letra == "k":
                    columna = 8
                elif columna_letra == "L" or columna_letra == "l":
                    columna = 8
                elif columna_letra == "M" or columna_letra == "m":
                    columna = 8
                elif columna_letra == "N" or columna_letra == "n":
                    columna = 8
                elif columna_letra == "Ñ" or columna_letra == "ñ":
                    columna = 8
                elif columna_letra == "O" or columna_letra == "o":
                    columna = 8

                else:
                    print("Esta opcion no es valida")

                print("columna:")
                print(columna)
                print("fila:")
                print(fila)

                tablero_vista[fila][columna] = "X "
                tablero[fila][columna] = 1

                if tablero[fila][columna] == -1:
                    perdio = 1
                    Client_conn.sendall(b"p")
                else:
                    # Client_conn.sendall(b"Estuviste cerca")
                    Client_conn.sendall(b"s")

        print("El juego ha terminado")
