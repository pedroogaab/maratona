#Codigo inicial com minha logica
interacoes = int(input())

exibe = []

for i in range(interacoes):
	result = 1
	value = int(input())
    
	for n in range(1, value):
		result += result*n
	exibe.append(result)
    
for ex in range(len(exibe)):
	print(exibe[ex])
	
	
	
#Codigo mais otimizado 
import math

interacoes = int(input())
exibe = []

for i in range(interacoes):
    value = int(input())
    result = math.factorial(value)
    exibe.append(str(result))

output = '\n'.join(exibe)
print(output)
