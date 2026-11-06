# importar librerias
import pandas as pd
import numpy as np
print("Analisis de tansacciones fraudolentas Daniel Nieves NC=1343 ")
transacciones = {
    "Id_Transaccion": ["T01", "T02", "T03", "T04", "T05", "T06"],
    "Monto": [15.50, 2500.00, 45.00, 890.00, 12.00, 3400.00],
    "Ubicacion_Inusual": [False, True, False, True, False, True],
    "Es_Fraude": [False, True, False, False, False, True]
}
df=pd.DataFrame(transacciones)
print(df)
print(" -+-+-+ Agrupar una sola columna Id Transaccion +-+-+-")
agrupado = df.groupby('Id_Transaccion')
print(agrupado)
#
print(" -+-+-+ Por agregacion +-+-+-")
# transaccion promedio
print(agrupado['Monto'].mean())

# Monto Maximo en cada transaccion
print(agrupado['Es_Fraude'].max())
