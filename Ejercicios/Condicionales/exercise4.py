compra = float(input("cuanto compraste?:"))
descuento = .80


if compra>=300:
    compra = compra*descuento
else:
    compra = compra*1.0

print(f"el total de tu compra es de: {compra}")