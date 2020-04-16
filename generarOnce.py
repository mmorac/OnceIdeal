import obtenerInformacion



#Lista de clubes
clubes = {1:"Saprissa", 2:"Alajuelense", 3:"Herediano", 4:"Cartaginés", 5:"Pérez Zeledón", 6:"Santos", 7:"San Carlos", 8:"Belén", 9:"Puntarenas",
10:"Limón", 11:"Carmelita", 12:"Uruguay", 13:"La U", 14:"As Puma Generaleña", 15:"Liberia", 16: "Guadalupe FC", 17:"Municipal Grecia", 18:"Jicaral Sercoba"}

key = obtenerInformacion.obtenerApiKey()
descargar = False

obtenerInformacion.obtenerInformacion(descargar, key)
