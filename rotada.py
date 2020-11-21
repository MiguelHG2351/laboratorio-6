matrix = [
        [0,0,0,0,1,0,0],
        [0,0,0,0,1,1,0],
        [1,1,1,1,1,1,1],
        [0,0,0,0,1,1,0],
        [0,0,0,0,1,0,0],
        ]

def rotar(matriz):
    rotada = []
    for i in range(len(matriz[0])):
        rotada.append([])
        for j in range(len(matriz)):
            rotada[i].append(matriz[len(matriz)-1-j][i])
    return rotada

for fila in matrix:
    for e in fila:
        print(e, end=" ")
        print()
        
print("-----------------------------")
    
rotada= rotar(matrix)

for fila in rotada:
    for e in fila:
        print(e, end=" ")
        print()
        
print("-----------------------------")
    
rotada2= rotar(matrix)

for fila in rotada2:
    for e in fila:
        print(e, end=" ")
        print()