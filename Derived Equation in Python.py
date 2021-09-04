


tempo = input("valor de t: ")
t = float(tempo)

I = input("valor de I: ") 
corrente = float(I)

L = 0.1

diferencialI = diff(I)
diferencialt = diff(t)

di = float(diferencialI)
dt = float(diferencialt)

derivada = (di/dt)

final = L*derivada




print("A derivada é igual á: ", final)

