#Enunciado 
# Una tienda necesita un programa que lea el nombre y el precio de un producto
# calcule el impuesto de ventas del 13 % 
# y muestre el nombre del producto y su precio final con el impuesto incluido.
# Problema 3: Precio final de un producto con impuesto
 
# ----- Entrada -----
nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
# ----- Proceso -----
tasa_impuesto = 0.13    # constante: 13 % de impuesto
monto_impuesto = precio_producto * tasa_impuesto
precio_final = precio_producto + monto_impuesto
# ----- Salida -----
print("Producto:", nombre_producto)
print("Impuesto (13%): ₡" + format(monto_impuesto, ",.2f"))
print("Precio final: ₡" + format(precio_final, ",.2f"))

