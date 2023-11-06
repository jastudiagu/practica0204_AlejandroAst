datos = {}
nombre = input('Escribe tu nombre: ')
edad = input('Escribe tu edad: ')
direccion = input('Escribe tu dirección: ')
tlf = input('Escribe tu teléfono: ')

datos['nombre'] = nombre
datos['edad'] = edad
datos['direccion'] = direccion
datos['tlf'] = tlf

print('{} tiene {} años, vive en {} y su número de teléfono es {}. '.format(datos['nombre'], datos['edad'], datos['direccion'], datos['tlf']))