import bil

looping = True #för att avslute programmet
volvo_svart = bil.Bil("Volvo", "Svart", 5)
volvo_vit = bil.Bil("Volvo", "vit", 2)
ferrari_röd = bil.Bil("Ferrari", "röd", 4)

while looping:
    print("---------------------------------")
    print("\n-:BilAutomat:-\n")

    #avsluta programmet
    go = input("\n Vill du avsluta programmet? j/n ")

    if (go == "j"):
        break