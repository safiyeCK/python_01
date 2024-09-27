x = input('1.sayi:')
y = input('2.sayi:')

total= x+y  
'''

total= x+y  bu sekilde birakirsak string olarak degerlendirir o nedenle basina int eklemeliyiz
CTRL+K+C ile tumunu yoruma al, CTRL+Z ile de geri alinir
''' 
total_1= int(x)+int(y) 
print(total)
 
x= 5
y= 2.5
name= "Safiye"
isOnline= True

print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))

x= float(x)
print(x)

print(type(x))

result= x+y
print(result)
print(type(result))
 
result= str(x)+str(y)
print(result)
print(type(result))
 