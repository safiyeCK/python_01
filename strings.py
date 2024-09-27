name="Safiye"
surname="Kara"
age=44

greeting="My name is"+" "+ name +" "+surname+" "+ "and \n I am "+str(age)+" "+"years old."
length=len(greeting)

print(greeting)
print(greeting[0])
#0. indexdeki karakter gelir
print(greeting[2])
print(greeting[3])
#print(len(greeting))
#length ini verir
print(greeting[length-1])

print(len(greeting[-1]))
print(greeting[-1])

print(greeting[3:7])
#3 ile 7 arasindaki karakterler gelir
print(greeting[3:])
#3 ten sonraki tum karakterler gelir
print(greeting[:16])
#bastan 16. karaktere kadar gider
print(greeting[2:40:2])
#2. karakterden baslar 40. karaktere kadar gider ama duzenli almaz. 2 karakterde bir alir

