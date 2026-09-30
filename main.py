ism = 'Diyor'
print(ism.upper())

print(ism.lower())
name = 'ali'
print(name.title())
print(name.capitalize())

matn = "salom Asadbek yahshimisan jo`ra"
print(matn.title())
print(matn.capitalize())

ismlar = ['nodir', 'asadbek', 'nodirbek', 'bexruzbek']
ismlar.sort()
print(ismlar)

print(sorted(ismlar))
print(sorted(ismlar, reverse=True))
del ismlar[2]
print(ismlar)
ismlar.append('sobir')
ismlar.append('vali')
print(ismlar)
ismlar.insert(1, 'jo`rabek')
print(ismlar)
print(ismlar.pop(3))
print(ismlar)
ismlar.remove('asadbek')
print(ismlar)

