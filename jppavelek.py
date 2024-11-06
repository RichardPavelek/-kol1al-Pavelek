#pole s pěti stringovými hodnotami
array = ["pole", "měsíc", "jméno", "přijmení", "datum"]
print(array)
print()
#přidání prvku vítr pomocí append
array.append("vítr")
print(array)
print()
#pomocí remove odstranění druhé hodnoty pole
array.remove("měsíc")
print(array)
print()
#zaměnění 5 hodnoty pole za slovo slunce
array[4] = "slunce"
print(array)
print()
#2 stringové hodnoty přidané pomocí extend
array.extend(["osmani", "lafita"])
print(array)