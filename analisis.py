import numpy as np
import pandas as pd
#Abrimos la carpeta vgchartz-2024
df=pd.read_csv("vgchartz-2024.csv")
print(df.shape)
"""Limpieza de datos con Python:
Detección y eliminación de valores duplicados:
Asegúrate de que cada registro en el dataset sea único."""
df=df.drop_duplicates(subset=['img','title', 'console'])#Use como referencia las tres primeras columnas
print(df.shape)
"""Verificación y ajuste de tipos de datos: 
Asegúrate de que todas las columnas coincidan con los tipos de 
datos indicados en el diccionario de datos.
"""
print(df.dtypes) #Coincide
"""Detección de datos anómalos: Identifica y corrige cualquier punto de
dato inapropiado o inusual (por ejemplo, un videojuego con ventas negativas).
"""
aux=df[df.critic_score<0]
print(aux.shape) #no hay en critic_score
aux=df[df.total_sales<0]
print(aux.shape) #no hay en total_sales



