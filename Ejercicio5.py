dic = {}
entrada = input(' Introducirá  palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas, al terminar escribe “terminar”: ' )
entrada = entrada.lower()
frase_ing = ''

entrada_s = entrada.split(", ")

for i in range(len(entrada_s)):
    e_i = entrada_s[i]
    e_i_s = e_i.split(':')
    if e_i_s[0] != 'terminar':
        dic[e_i_s[0]] = e_i_s[1]
    else:
        break

entrada_traducir = input('Escribe una frase en español: ')
entrada_traducir = entrada_traducir.lower()
entrada_traducir_s = entrada_traducir.split(' ')


for j in range(len(entrada_traducir_s)):
    if entrada_traducir_s[j] in dic:
        frase_ing += ' '
        frase_ing += dic[entrada_traducir_s[j]]
    else:
        frase_ing += '!error!'
    

if '!error!' in frase_ing:
    print('Tu frase no se puede traducir, faltan palabras.')
else:
    print(frase_ing)