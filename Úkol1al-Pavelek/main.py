import random

#1. pole s 9 nahodnými čísly v rozahu 0 až 100
print("Pole s 9 náhodnými čísly v rozsahu 0 až 100")
arraya = [random.randint(0,100) for _ in range(9)]
print(arraya)

print()

#2. vypsání prvního, prostředního a posledního čísla v poli
print("první, prostřední a poslední čísla pole:")
print(arraya[0], arraya[4], arraya[8])

print()

#3. změněnění 5. indexové hodnoty na číslo 34
arraya[4] = 34
print(arraya)

#4. vypsání 7. indexové hodnoty z pole
print("7. indexová hodnota je:")
print(arraya[6])

#5. vypsání délky pole
print("Délka pole je:")
print(len(arraya))

#6. vypsání minimální a maximální hodnoty pole
print("Minimální hodnota pole je:")
print(min(arraya))
print("Maximální hodnota pole je:")
print(max(arraya))

#7. druhé pole libovolné délky a hodnot
print()
arrayb = [2, 4, 8, 16, 32, 64, 128, 256, 512]

#8.sečtení obou polí
print()
print("Součet obou polí:")
print(sum(arraya+arrayb))

#9. sečtení indoxově 1. a 5. hodnotu z druhého pole
print()
print("Součet 1. a 5. indexové hodnoty 2. pole je:")
print(arrayb[0]+arrayb[4])