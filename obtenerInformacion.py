import dropbox
import os
import pandas as pd

#SE GENERA EL ACCESO A DROPBOX USANDO LA CLAVE QUE GENERO DESDE MI CUENTA

#Lista de digitadores
digitadores = ["Alejandro", "Cristian", "Gabriel", "Greivin", "Gustavo", "Irving", "Jonathan", "Mario"]

def obtenerApiKey():
    f=open("archivos/api_key.txt", "r")
    key = f.read()
    return key


def obtenerInformacion(descarga_requerida, api_key):
    api_key = api_key.strip()

    try:
        dbx = dropbox.Dropbox(api_key)
    except ValueError as ve:
        print(ve.message)

    info = pd.DataFrame({})

    if(descarga_requerida):
        #Se recorre la lista de digitadores para descargar sus archivos respectivos
        for digitador in digitadores:
            with open("archivos/" + digitador + ".xlsx", "wb") as f:
                #Se usará el método files_download de la librería de DROPBOX para la descarga
                metadata, res = dbx.files_download(path="/2020 Torneo de Clausura/Control de jornadas de jugadores y clubes TC 2020 " + digitador + ".xlsx")
                f.write(res.content)
                print("¡Archivo de", digitador, "exitosamente descargado!")


    for digitador in digitadores:
        df = pd.read_excel("archivos/" + digitador + ".xlsx", "Jugadores")
        info = pd.concat([info, df])
    return info

#Función para obtener la lista completa de jugadores con código y posición
def obtenerJugadores():
    df = pd.read_excel("archivos/Listado de Jugadores con Código TC 2020.xlsx", "Listado jugadores")
    return df
