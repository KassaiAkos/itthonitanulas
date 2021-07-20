#lists (mutable) - listak (modosithato)


lista1 = []

print('lista1')

lista1.append(100)
lista1.append(101)
lista1.append(102)
lista1.append(103)
lista1.append(104)

print(lista1)
    
lista1.append('Enikő')
lista1.append('Aniko')
lista1.append('Eniko')


print(lista1)

lista1.remove('Eniko')

print(lista1)

#lista1.clear()

lista1.insert(5, 'Bozsi')

print(lista1)

lista1.reverse()


print(lista1 )

#számok szerint sorba állítja
lista2=[15, 8, 78, 23, 1, 65, 184,]
lista2.sort()
print(lista2)

#ABC szerint sorba álítja
lista3=['Xena','Bozsi', 'Vica', 'Eni','Ildi']
lista3.sort()
print(lista3)

#Megmutatja hogy az adott listában hány elem van
print(len(lista3))



