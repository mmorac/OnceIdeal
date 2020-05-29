import obtenerInformacion
import pandas as pd


def generarOnce(jornadas, equipos, formacion):

    #Lista de clubes
    clubes = {1:"SAP", 2:"LDA", 3:"CSH", 4:"CSC", 5:"MPZ", 6:"SAN", 7:"ADSC", 8:"BEL", 9:"PUN",
    10:"LFC", 11:"ADC", 12:"CSU", 13:"LAU", 14:"ASP", 15:"LIB", 16: "GFC", 17:"GRE", 18:"JIC"}

    key = obtenerInformacion.obtenerApiKey()

    descargar = False

    #Se obtiene la base de datos consolidada
    info = obtenerInformacion.obtenerInformacion(descargar, key)

    #Se obtiene la lista de jugadores con la respectiva posición
    jugadores = obtenerInformacion.obtenerJugadores()

    p_equipos = pd.DataFrame()
    reg_jornada = pd.DataFrame()

    #Filtrar por equipos
    for e in equipos:
        j_equipo = info.loc[(info['id_club'] == float(e))]
        frames = [p_equipos, j_equipo]
        p_equipos = pd.concat(frames)

    #Obtener información de las jornadas que se buscan
    for j in jornadas:
        jornada = p_equipos.loc[(p_equipos['id_jornada'] == float(j))]
        frames = [reg_jornada, jornada]
        reg_jornada = pd.concat(frames)

    porteros = {}
    defensas = {}
    volantes = {}
    delanteros = {}


    once = reg_jornada.sort_values(["IRJ_General"], ascending = False)

    try:
        #Se separan los puntajes por posición de jugador
        for index, fila in once.iterrows():
            if not (fila["id_jugador"] > 0):
                continue

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

    except Exception as ex:
        print("Error", ex)

    df = int(formacion.split("-")[0])
    mc = int(formacion.split("-")[1])
    dl = int(formacion.split("-")[2])

    onceideal = []

    onceideal.append(porteros_o[0])

    for i in range(0, df):
        onceideal.append(defensas_o[i])

    for i in range(0, mc):
        onceideal.append(volantes_o[i])

    for i in range(0, dl):
        onceideal.append(delanteros_o[i])

    lista = []

    for j in onceideal:
        j = list(j[1])
        nombre = j[0]
        print("Jugador:", nombre)
        nombre = nombre.split()
        if(len(nombre) > 3):
            nombre = str(nombre[0][0]) + ". " + str(nombre[2])
        else:
            nombre = str(nombre[0][0]) + ". " + str(nombre[1])

        j[0] = nombre
        j[2] = int(j[2])
        lista.append(j)

    return lista

generarOnce([16, 17, 18], [1, 2, 3, 4, 5, 6, 7, 10, 13, 16, 17, 18], "3-5-2")
