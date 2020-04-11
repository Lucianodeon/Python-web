print("Decime tu name papu")
user=input()
print(f"hola {user}")
print("¿que edad tenes?")
edad=input()
print(f"asi que sos {user} con {edad} años")
#print("dame un numero")
x=-28
if x>0:
    print(f"x is positive and {x} ")
elif x<0:
    print(f"x is negative and {x} ")
else:
    print('x is zero')

nombre="lucho"
coordinates=(10.0,20.0) #coordenadas x e y
nombres=["luchi","bob","alice"]
coordinates[0]
coordinates[1]
nombre[1]
nombres[1]
print(f"los nombres son: {nombres}")
print(f"las coordenadas son: {coordinates}")
print(f"coordenadas en el eje x {coordinates[0]}")
print(f"coordenadas en el eje y {coordinates[1]}")
print(f"la primera letra de tu nombre es: {user[0]}")
print(f"la segunda persona del array es {nombres[1]}")
for i in range(7):
    print(i)
names=["luchi","bob","alice"]
print("impresion del loop names")
for name in names:
    print(name)
#dictionaries
ages={"Alice":22, "Bob": 27}
ages["Charlie"]=30
ages['Alice']+=1
print(ages)

#funciones
print("aca empieza una funcion cuadrada")
def square(x):
    return x*x
for i in range (10):
    print("{} square is {}".format(i,square(i))) #esta es una notacion media vieja
#class clases
print("aca voy a usar clases y genero un punto en x e y")
class Point:
    def __init__(self, x, y):#con init llamo a la funcion cuando creo un objeto de la clase
        self.x= x
        self.y= y
p= Point(3,5)
print(p.x)
print(p.y)

#Flask es un micro framework para python ir a application.py.
