monedas =  {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

while True:
    divisa = input('Escribe el nombre de la divisa: (Solo "Euro", "Dollar" o "Yen"): ')
    if divisa == 'Euro':
        print('El signo de tu divisa es: {}'.format(monedas[divisa]))
        break

    if divisa == 'Dollar':
        print('El signo de tu divisa es: {}'.format(monedas[divisa]))
        break

    if divisa == 'Yen':
        print('El signo de tu divisa es: {}'.format(monedas[divisa]))
        break