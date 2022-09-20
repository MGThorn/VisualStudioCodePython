i = 0
j = 0
while(i < 100000):
    Zahl = str(i)
    temp1 = 0
    temp2 = 1
    
    for Symbol in Zahl:
        temp1 += int(Symbol)
        temp2 *= int(Symbol)
        
    if(len(Zahl)<5):
        temp2 = 0
    if(temp1==temp2):
        print(f"QSumme {temp1}")
        print(f"PSumme {temp2}")
        print(f"Zahl {i}")
        j+=1
        print(f"ZNummer {j}")
    i+=1
