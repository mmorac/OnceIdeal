import obtenerInformacion
import pandas as pd


#Lista de clubes
clubes = {1:"SAP", 2:"LDA", 3:"CSH", 4:"CSC", 5:"MPZ", 6:"SAN", 7:"ADSC", 8:"BEL", 9:"PUN",
10:"LFC", 11:"ADC", 12:"CSU", 13:"LAU", 14:"ASP", 15:"LIB", 16: "GFC", 17:"GRE", 18:"JIC"}

key = obtenerInformacion.obtenerApiKey()

descargar = False

#Se obtiene la base de datos consolidada
info = obtenerInformacion.obtenerInformacion(descargar, key)

#Se obtiene la lista de jugadores con la respectiva posición
jugadores = obtenerInformacion.obtenerJugadores()


jornada = int(input("Elija una jornada de inicio:"))
jornada_fin = int(input("Elija una jornada de cierre:"))


reg_jornada = info.loc[(info['id_jornada'] >= float(jornada)) & (info['id_jornada'] <= float(jornada_fin))]

porteros = {}
defensas = {}
volantes = {}
delanteros = {}


once = reg_jornada.sort_values(["IRJ_General"], ascending = False)

for index, fila in once.iterrows():
    info_basica = jugadores.loc[jugadores["IDJugador"] == fila["id_jugador"]]


once = once.head(11)
