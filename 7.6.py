#6
def wieksza(liczba1, liczba2, liczba3):
    najwieksza=0
    if liczba1>=liczba2:
        najwieksza=liczba1
    else:
        najwieksza=liczba2

    if najwieksza<=liczba3:
        najwieksza=liczba3

    return najwieksza

a=2
b=5
c=3
print(wieksza(a,b,c))
