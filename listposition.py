lista = ['a','c','r','tg','qwe','l','bv','nnb']
valor = 'w'
encontrado = None
if valor in lista:
    encontrado = lista.index(valor)
if encontrado is not None:
    print(encontrado)
else:
    print('Nao encontrado')