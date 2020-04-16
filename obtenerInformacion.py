import dropbox
import os
import pandas as pd

#SE GENERA EL ACCESO A DROPBOX USANDO LA CLAVE QUE GENERO DESDE MI CUENTA

#Lista de digitadores
digitadores = ["Alejandro", "Cristian", "Gabriel", "Greivin", "Gustavo", "Irving", "Jonathan", "Mario"]

def obtenerApiKey():
    f=open("api_key.txt", "r")
    key = f.read()
    return key


def obtenerInformacion(descarga_requerida, api_key):
    dbx = dropbox.Dropbox(api_key)

    if(descarga_requerida):
        #Se recorre la lista de digitadores para descargar sus archivos respectivos
        for digitador in digitadores:
            with open(digitador + ".xlsx", "wb") as f:
                #Se usará el método files_download de la librería de DROPBOX para la descarga
                metadata, res = dbx.files_download(path="/2020 Torneo de Clausura/Control de jornadas de jugadores y clubes TC 2020 " + digitador + ".xlsx")
                f.write(res.content)
                print("¡Archivo de", digitador, "exitosamente descargado!")


    df = pd.read_excel(r"Mario.xlsx", "Jugadores")
    id = 1
    while(id != 0):
        try:
            id = int(input("Ingrese un ID de jugador: "))
        except ValueError:
            print("Debe ingresar un valor numérico entero")
            id = int(input("Ingrese un ID de jugador: "))

        if(df.id_condicion[id] == "1"):
            condicion = "local"
        else:
            condicion = "visitante"

        jugadores = [df.NombreJugador[id], df.IRJ_General[id], df.id_club[id], condicion, df.id_jornada[id]]
        print(jugadores[0], "de", jugadores[2], "logró un IRJ de:", jugadores[1], "en su partido como", jugadores[3], "de la jornada", jugadores[4])
