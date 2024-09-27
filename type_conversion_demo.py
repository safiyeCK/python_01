'''
Daire Alani : πr²
Daire Cevresi : 2πr
*Yari capi verilen bir dairenin alan ve cevresini hesaplayiniz(r:3.14)
** 2 dersek, karesini aliyoruz
'''

r=float(input('Yaricap:'))
pi=3.14

daireAlan=pi*(r**2)
print("Alan:", daireAlan)
daireCevre=2*pi*r
print("Cevre:",daireCevre)
print("Alan:"+str(daireAlan)+ " "+ "Cevre:"+str(daireCevre))