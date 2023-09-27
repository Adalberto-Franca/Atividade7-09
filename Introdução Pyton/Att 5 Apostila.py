valor = float(input('Digite o valor do produto: '))
disconto = int(input('Digite o valor do disconto: '))
total = valor - (valor * disconto)/100
print ('o valor final do produto é de:',total)