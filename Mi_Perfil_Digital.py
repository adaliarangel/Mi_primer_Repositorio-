#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "Adalía Fernanda Palomino Rangel"
edad = 15
estatura = 1.57
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("Adaliarangel", "Ferrxngel")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "Idilio", "artista": "Willie Colón", "duracion": "5:08"},
{"titulo": "Tengo Ganas", "artista": "Víctor Manuelle", "duracion": "4:26"},
{"titulo": "Manos de Tijera", "artista": "Yiyo Sarante", "duracion": "3:50"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
print(f"{cancion["titulo"]} - {cancion["artista"]})({cancion["duracion"]})min")
print ("----------------------------------")
