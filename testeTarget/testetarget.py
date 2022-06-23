
########### TESTE TARGET  #####################

# 2

# Sequência de Fibonacci


valor = int(input("Digite um valor e veremos se ele está na sequência de Fibonacci "))



    # Calculando a sequência

sequencia = [0, 1]

i = 1
while sequencia[i] < valor:
    elemento = sequencia[i] + sequencia[i-1]
    sequencia.append(elemento)
    i += 1
print(sequencia)

if valor in sequencia:
    print(f'O valor {valor}, pertence à sequência.')
else:
    print(f'O valor {valor}, não pertence à sequência.')
    
    
    
# 3 

# Faturamento anual    
    
import json

arquivo = open('dados.json', 'r')
data = json.load(arquivo)

FAT_ANU = []
FAT_LIQ = []

for i in range(len(data)):
    FAT_ANU.append(data[i]['valor'])

zeros = 0

for j in range(len(FAT_ANU)):
    if FAT_ANU[j] == 0: zeros += 1
    else: FAT_LIQ.append(FAT_ANU[j])

dias_uteis = len(FAT_ANU) - zeros
soma_fat = sum(FAT_ANU)

media = soma_fat/dias_uteis
menor = min(FAT_LIQ)
maior = max(FAT_LIQ)

sup = 0

for fatu in FAT_ANU:
    if fatu > media: sup += 1

print(f"Menor valor de faturamento ocorrido em um dia no mês: {menor};\nMaior valor de faturamento ocorrido em um dia no mês: {maior};\nQuantidade de dias em que o faturamento diario foi superior a média mensal :{sup}")



# 4

# Faturamento mensal

faturamento = dict(SP=67836.43, RJ=36678.66, MG=29229.88, ES=27165.48, Outros=19849.53)

total = sum(faturamento.values()) # Somar todos os valores

for key in faturamento:
    percentual = ((faturamento[key])/total)*100
    print(f"O percentual de contribuição de {key} foi de {percentual:.2f}%")
        
        
        
# 5 inverter palavra

string = input(str("Digite uma palavra: "))
n = len(string)
stringR = string[n-1]

for i in range(n-2,-1,-1):
    stringR = stringR + string[i]
print(stringR)



