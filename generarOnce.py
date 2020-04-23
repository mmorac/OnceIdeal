import obtenerInformacion
import pandas as pd


def generarOnce(j_inicio, j_fin, formacion):

    #Lista de clubes
    clubes = {1:"SAP", 2:"LDA", 3:"CSH", 4:"CSC", 5:"MPZ", 6:"SAN", 7:"ADSC", 8:"BEL", 9:"PUN",
    10:"LFC", 11:"ADC", 12:"CSU", 13:"LAU", 14:"ASP", 15:"LIB", 16: "GFC", 17:"GRE", 18:"JIC"}

    key = obtenerInformacion.obtenerApiKey()

    descargar = False

    #Se obtiene la base de datos consolidada
    info = obtenerInformacion.obtenerInformacion(descargar, key)

    #Se obtiene la lista de jugadores con la respectiva posición
    jugadores = obtenerInformacion.obtenerJugadores()


    reg_jornada = info.loc[(info['id_jornada'] >= float(j_inicio)) & (info['id_jornada'] <= float(j_fin))]

    porteros = {}
    defensas = {}
    volantes = {}
    delanteros = {}


    once = reg_jornada.sort_values(["IRJ_General"], ascending = False)

    #Se separan los puntajes por posición de jugador
    for index, fila in once.iterrows():
    	info_basica = jugadores.loc[jugadores["IDJugador"] == fila["id_jugador"]]
    	posicion = info_basica.iloc[0]["Posición"]
    	if(posicion == "Portero"):
    		if(fila["id_jugador"] in porteros.keys()):
    			porteros[fila["id_jugador"]][2] += fila["IRJ_General"]
    		else:
    			porteros[fila["id_jugador"]] = [fila["NombreJugador"], clubes[fila["id_club"]], fila["IRJ_General"], posicion]
    	if(posicion == "Defensa"):
    		if(fila["id_jugador"] in defensas.keys()):
    			defensas[fila["id_jugador"]][2] += fila["IRJ_General"]
    		else:
    			defensas[fila["id_jugador"]] = [fila["NombreJugador"], clubes[fila["id_club"]], fila["IRJ_General"], posicion]
    	if(posicion == "Volante"):
    		if(fila["id_jugador"] in volantes.keys()):
    			volantes[fila["id_jugador"]][2] += fila["IRJ_General"]
    		else:
    			volantes[fila["id_jugador"]] = [fila["NombreJugador"], clubes[fila["id_club"]], fila["IRJ_General"], posicion]
    	if(posicion == "Delantero"):
    		if(fila["id_jugador"] in delanteros.keys()):
    			delanteros[fila["id_jugador"]][2] += fila["IRJ_General"]
    		else:
    			delanteros[fila["id_jugador"]] = [fila["NombreJugador"], clubes[fila["id_club"]], fila["IRJ_General"], posicion]


    #Se obtiene una vista ordenada de las diferentes posiciones
    porteros_o = sorted(porteros.items(), key = lambda kv:kv[1][2], reverse = True)
    defensas_o = sorted(defensas.items(), key = lambda kv:kv[1][2], reverse = True)
    volantes_o = sorted(volantes.items(), key = lambda kv:kv[1][2], reverse = True)
    delanteros_o = sorted(delanteros.items(), key = lambda kv:kv[1][2], reverse = True)

    df = formacion[0]
    mc = formacion[1]
    dl = formacion[2]

    onceideal = []

    onceideal.append(porteros_o[0])

    for i in range(0, df):
    	onceideal.append(defensas_o[i])

    for i in range(0, mc):
    	onceideal.append(volantes_o[i])

    for i in range(0, dl):
    	onceideal.append(delanteros_o[i])
