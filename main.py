#1-misol
a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))
c = float(input("3-sonni kiriting: "))

eng_katta = max(a, b, c)
print("Eng katta son:", eng_katta)

#2-misol
yil = int(input("Yilni kiriting: "))

if (yil % 400 == 0) or (yil % 4 == 0 and yil % 100 != 0):
    print("Kabisa yili")
else:
    print("Oddiy yil")

#3-misol
a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))
c = float(input("3-sonni kiriting: "))

eng_kichik = min(a, b, c)
print("Eng kichik son:", eng_kichik)

#4-misol
n = int(input("Raqam kiriting: "))

if n == 0:
    print("0")
elif n == 1:
    print("1")
else:
    print("Boshqa raqam")
#5-misol
a = float(input("1-tomonni kiriting: "))
b = float(input("2-tomonni kiriting: "))

if a == b:
    print("Kvadrat")
else:
    print("To'rtburchak")
#6-misol
n = float(input("Son kiriting: "))

if n <= 100:
    print("Kichik yoki teng 100")
else:
    print("Katta")
