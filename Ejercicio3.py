articulos = {'pan': 1.4, 'huevos': 2.3, 'cebolla': 0.85, 'aceite': 4.35 }

art = input('Escribe un árticulo que quieras comprar: ')
art = art.lower()

while art not in articulos:
    print('No tenemos el árticulo {}, lo sentimos. '.format(art))
    art = input('Escribe un árticulo que quieras comprar (Pan, huevos, cebolla o aceite): ')
    art = art.lower()
    if art in articulos:
        break

cantidad = int(input('Escribe la cantidad que quieres del producto seleccionado: '))
precio = float(cantidad * articulos[art])
print('El valor a pagar será de {}€.'.format(round(precio, 2)))