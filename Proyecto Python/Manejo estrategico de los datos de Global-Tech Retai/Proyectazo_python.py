'''
## CHICOS PARA QUE ESTO QUEDE melo esto... (lean comentarios y ejecuten codigo)



entrada = input(f'si o no? sapo🐸\f si no sabe  que coja oficio y lea el documento👹 \f ')

if 'si' == entrada.lower():
    print(f'ta melitico pa 😎🔥')
#*!  BIEN MELITICO INTALEN
if 'no' == entrada.lower():
    print(f'muy paraito pa, se va a hacer dañar?👹👺🗡️🔫')

elif 'sapo' == entrada.lower():
    print(f'sapa su madre, pirobo🐸')
#//? tienen que instalar el plugin de better comments en vscode
print(f'\f \f Vaguen estudiosos 🤠👌🏽')

#TODO:Aqui les dejo la poderosa https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments

'''
#//! IMPORTAMOS LOS PACKETES NECESARIOS PARA EL PROYECTO
#*? RECUERDEN instalarlos poninendo pip install nombre_del_paquete en la terminal de vscode
import pandas as pd
import numpy as np
import sqlite3 #esto es para leer bases de datos sqlite

#import seaborn as sn  #? este no lo vamos a usar por ahora
#import matplotlib.pyplot as plt

#//! LEEMOS LOS CSV QUE NECESITAMOS PARA EL PROYECTO
productos_df = pd.read_csv('Proyecto Python/Documentos/productos.csv')
ventas_df = pd.read_csv('Proyecto Python/Documentos/ventas.csv')

#? LEEMOS EL DB DE CLIENTES, PERO NO LO VAMOS A USAR POR AHORA
conexion = sqlite3.connect('ruta/al/archivo.db')
cursor = conexion.cursor()

# Ver tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("🗂️ Tablas disponibles:", cursor.fetchall())



#? MUESTRA LOS PRIMEROS 10 DATOS DEL DATAFRAME
print('MUESTRA LA CABECERA Y LOS PRIMEROS 10 DATOS DEL DATAFRAME','\f',productos_df.head(11),'\f \f')
#? MUESTRA UN RESUMEN ESTADISTICO DEL DATAFRAME
print('MUESTRA UN RESUMEN ESTADISTICO DEL DATAFRAME','\f',productos_df.describe(include='all'),'\f \f')
#? MUESTRA INFORMACION DEL DATAFRAME
print('MUESTRA INFORMACION DEL DATAFRAME','\f',productos_df.info(),'\f \f')    


