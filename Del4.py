n = int(input("Ge mig siffror!! "))
a = 0
b = (1729-(a**3))**(1/3)
while (a**3 + b**3 != n):
 a = a + 1
 print((a**3)+(b**3))
if ((a**3)+(b**3)==n):
 print (a, b)
