

import numpy as np
lista = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
print(lista)
numero_colonna = int(input('colonna da visualizzare: '))
print([row[numero_colonna] for row in lista])


