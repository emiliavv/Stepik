#5
def wieksza(liczba1, liczba2):
    if liczba1>liczba2:
        return(liczba1)
    elif liczba1==liczba2:
        return("liczby są sobie równe")
    else:
        return(liczba2)

a = wieksza(10, 4)
print(a)