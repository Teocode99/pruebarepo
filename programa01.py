edad = int(input ( ))
if edad < 4:
    print("la entrada es gratis")
elif edad > 4 and edad < 12:
    print("paga boleto infantil,costo 40")
elif edad > 12 and edad < 59:
    print("paga boleto general,costo 70")
else:
    print("adulto mayor,costo 35")


