MonitorIRP=80000000
sueldo= int(input("Ingrese cuanto es su sueldo"))

sueldoAnual= (sueldo * 12)
if sueldo <80000000:
    print(f"su sueldo anual es",{sueldoAnual}, "no pagas impuesto")
else:
    print(f"su sueldo anual es",{sueldoAnual}, "debes pagar impuestos")
