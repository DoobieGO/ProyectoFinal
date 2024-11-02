#Calculadora de horas pagas
horas= int(input("Digite las horas trabajadas: "))
pagoph= int(input("Digite el pago por hora: "))
Operacion= horas*pagoph
print("Su salario por las horas trabajadas es de:",Operacion)

nombre=input("Digite su nombre: ")
estatura= float(input("digite su estatura en Metros: "))
peso= float(input("digite su peso en Kg: "))

IMC= peso/estatura*estatura
print("Hola ",nombre, "su indice de Masa corporal es de: ",IMC)