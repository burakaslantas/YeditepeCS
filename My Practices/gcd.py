a = int(input("(Please give an integer) a= "))
b = int(input("(Please give an integer) b= "))
c = 0
while b != 0:
    c = a
    a = b
    b = c%b
print(a)