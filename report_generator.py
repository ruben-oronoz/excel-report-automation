import pandas as pd

archivo = input("Ingresa el nombre del archivo Excel: ")
df = pd.read_excel(archivo)

df["producto"] = df["producto"].str.strip()
df["producto"] = df["producto"].str.title()

df["total"] = df["cantidad"] * df["precio"]

ventas_producto = df.groupby("producto")["total"].sum().sort_values(ascending=False)
ventas_fecha = df.groupby("fecha")["total"].sum()

print("----------- REPORTE DE VENTAS -----------")
print("Ventas totales:", df["total"].sum())

print("\nVentas por producto:")
print(ventas_producto)

print("\nVentas por fecha:")
print(ventas_fecha)

with pd.ExcelWriter("reporte_ventas.xlsx") as writer:
    df.to_excel(writer, sheet_name="Datos", index=False)
    ventas_producto.to_excel(writer, sheet_name="Ventas_por_producto")
    ventas_fecha.to_excel(writer, sheet_name="Ventas_por_fecha")
