#!/Library/Frameworks/Python.framework/Versions/3.11/bin python3

import socket
import time
import json
import pickle

HOST = "127.0.0.1"  # The server's hostname or IP address

#   Defiimos el puerto
PORT = 65432  # The port used by the server

#   Tamaño de buffer
buffer_size = 2048
principiante = (9, 9, 10)
avanzado = (16, 16, 40)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT)) # Connect necesita la información del nodo al que se va a conectar y el puerto
    print("Usuario conectado")
    data = TCPClientSocket.recv(buffer_size) # Se bloquea hasta que no se reciva algun dato
    print(data.decode())
    dificultad=str(input())
    TCPClientSocket.sendall(dificultad.encode())    #   Encode() sirve para convertir una cadena de caracteres en un conjunto de bytes

    if dificultad == "p" or dificultad == "P":
        print("Dificultad principiante")
        filas, columnas, minas = principiante

        gano = 0
        perdio = 0
        bandera = 0
        tiempo = time.time()
        while gano != 1 or perdio != 1:

            # Recibe el tablero
            data = TCPClientSocket.recv(buffer_size).decode()
            print(data)


            print("Ingresa la coordenada de la casilla que quiere abrir")
            columna = input("Ingresa la columna (puede ser: A B C D E F G H I): ")
            TCPClientSocket.sendall(columna.encode())


            fila = input("Ingresa la fila (puede ser: 1, 2, 3, 4, 5, 7, 8, 9): ")
            TCPClientSocket.sendall(fila.encode())

            data = TCPClientSocket.recv(buffer_size).decode()
            if data == "p":
                print("Perdiste")
                perdio = 1
            else:
                print("Sigue tu puedes!!")


    elif dificultad == "a" or dificultad == "A":
        filas, columnas, minas = principiante

        gano = 0
        perdio = 0
        bandera = 0
        tiempo = time.time()
        while gano != 1 or perdio != 1:

            # Recibe el tablero
            data = TCPClientSocket.recv(buffer_size).decode()
            print(data)

            print("Ingresa la coordenada de la casilla que quiere abrir")
            columna = input("Ingresa la columna (puede ser: A, B, C, D, E, F, G, H, I, J, K, L, M, N, Ñ, O): ")
            TCPClientSocket.sendall(columna.encode())

            fila = input("Ingresa la fila (puede ser: 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16) : ")
            TCPClientSocket.sendall(fila.encode())

            data = TCPClientSocket.recv(buffer_size).decode()
            if data == "p":
                print("Perdiste")
                perdio = 1
                break
            else:
                print("Sigue tu puedes!!")

    else:
        print("Esta opción no existe")

    print("El juego ha terminado \n")
    print("Duración del juego:", time.time() - tiempo, "segundos")
    print("Gracias por jugar")
