#Zdanie 1
a = float(input("Ile punktów otrzymaw: "))

if a > 80:
    print("zalicza egzamin w terminie 0")
elif a > 50:
    print("możesz poprawić jego wynik")
else:
    print("musisz poprawić.")

#Zad 2

x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

if x>y:
    x,y = y,x
if x>z:
    x,z = z,x
if y>z:
    y,z = z,y
print(x,y,z)

#Zad 3

Nazwa_pliku= 'Raport_maj.xlsx'
if Nazwa_pliku.endswith('.xlsx'):
    print("Tak")
else:
    print("Nie")

#Zad 4

gol = int(input("Ile golów było zabito: "))
bonus = int(input("możliwe punkty bonusowe dla drużyny: "))

punkty = gol * 10

punkty_bonusowe = 0
if gol > 10:
    punkty_bonusowe += 10
elif gol < 5:
    punkty_bonusowe += 5
elif gol < 10:
    punkty_bonusowe +=10
wynik_pierwszy = gol + bonus
print("Końcowy wynik drużyny:", wynik_pierwszy)

punkty = gol * 10 
if gol > 10:
    punkty += 10 + 5  
elif gol > 5:
    punkty += 5       

wynik_drugi = punkty + bonus + punkty_bonusowe
print("\nCałkowity wynik drużyny:", wynik_drugi)

#Zad 5a

with open('notwania_gieldowe.txt','r') as plik:
    for line in plik:
        print(line, end="")
print ('\n\n')
#Zad 5b
with open('notwania_gieldowe.txt','a') as plik:
     plik.write("ALR, 113")
with open("notwania_gieldowe.txt",'r') as plik:
    for line in plik:
        print(line, end='')

#Zad 6
litera = input("\n\n\nWprowadż literę: ")
if litera.isalpha() and len(litera) == 1:
    if litera.isupper():
        print("Litera:", litera, "jest duża")
    elif litera.islower():
        print("Litera:", litera, "jest mała")
else:
    print("Wprowadzony znak nie jest pojedyncą literą")
 
#Zad 7

Hasło = "pk47!jy0893"
if len(Hasło) >= 11 and '!' in Hasło:
    print("Hasło jest poprawne")
else:
    print("Hasło jest nie poprawne")

#Zad 8
text = 'Studiuje-Informatykę'
print("Trzy pierwsze znaki w tekscie:", text[:3])
print("Dwa ostatnie znaki w tekscie:", text[-2:])

#Zad 9
tekst = input("Wprowadź tekst:")
zmieniony_tekst = tekst.swapcase()
print("Tekst po zmianie wielkości liter:", zmieniony_tekst)


 

