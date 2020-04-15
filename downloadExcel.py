import dropbox
import os
import pandas as pd

#SE GENERA EL ACCESO A DROPBOX USANDO LA CLAVE QUE GENERO DESDE MI CUENTA
dbx = dropbox.Dropbox("JK894OVzkD8AAAAAAAABql5v19mpIfSZx9k8I6cZCwkoSb7l-2tB9MAZw0hl2uVT")

#Lista de digitadores
digitadores = ["Alejandro", "Cristian", "Gabriel", "Greivin", "Gustavo", "Irving", "Jonathan", "Mario"]

download_required = False

if(download_required):
    #Se recorre la lista de digitadores para descargar sus archivos respectivos
    for digitador in digitadores:
        with open(digitador + ".xlsx", "wb") as f:
            #Se usará el método files_download de la librería de DROPBOX para la descarga
            metadata, res = dbx.files_download(path="/2020 Torneo de Clausura/Control de jornadas de jugadores y clubes TC 2020 " + digitador + ".xlsx")
            f.write(res.content)
            print("¡Archivo de", digitador, "exitosamente descargado!")


df = pd.read_excel(r"Mario.xlsx")
jugadores = pd.DataFrame(df, columns=["id_jugador"])
print(jugadores)
