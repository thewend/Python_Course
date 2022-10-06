def calcula_distancia_Manhattan(x1,x2,y1,y2):
    ModuloX = x1 - x2
    if ModuloX < 0:
        ModuloX = ModuloX * (-1)
    ModuloY = y1-y2
    if ModuloY < 0:
        ModuloY = ModuloY * (-1)
    return ModuloX + ModuloY

x1 = 6
y1 = 11
print('O ponto um eh: (' , x1 , ', ' , y1 , '). ')
x2 = int( input( 'Digide X do segundo ponto. '))
y2 = int( input( 'Digide Y do segundo ponto. '))

print( 'A distancia Manhattan entre os dois pontos eh: ' , calcula_distancia_Manhattan(x1,x2,y1,y2))