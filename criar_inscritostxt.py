import os
inscritos = ['Banana','Mação','Laranja','Limão','Pera','Uva','Mamão','Morango','Melancia','Abacate']

with open('texto.txt','w', newline='') as file:
    for line in inscritos:
        file.write(line + os.linesep)
