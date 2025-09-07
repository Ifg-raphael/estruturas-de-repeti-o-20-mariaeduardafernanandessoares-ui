massa_inicial = float(input())
massa_final = 0.5
tempo_segundos = 0

massa_atual = massa_inicial #variavel para registrar as mudanças 
while massa_atual >= massa_final:
    massa_atual /= 2
    tempo_segundos += 50

horas = int(tempo_segundos / 3600) #para saber as horas
minutos = int((tempo_segundos % 3600) / 60)# para saber os minutos 
segundos = int(tempo_segundos % 60)# segundos que faltam

print(f"{horas}h {minutos}m {segundos}s")
