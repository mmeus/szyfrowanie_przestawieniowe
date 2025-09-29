dane = [w.strip() for w in open('sygnaly.txt').readlines()]
wynik = ''

for i in range(39, 1000, 40):
    wynik += dane[i][9]

print(wynik)
