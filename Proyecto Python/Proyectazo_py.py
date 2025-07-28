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
#//? IMPORTAMOS LOS PACKETES NECESARIOS PARA EL PROYECTO
#*! RECUERDEN instalarlos poninendo pip install nombre_del_paquete en la terminal de vscode
import pandas as pd
import numpy as np
# import seaborn as sn *!este no lo vamos a usar por ahora
#import matplotlib.pyplot as plt
productos_df = pd.read_csv('Proyecto Python/Documentos/productos.csv')


productos_df.describe() #! MUESTRA UN RESUMEN ESTADISTICO DEL DATAFRAME
productos_df.info() #! MUESTRA INFORMACION DEL DATAFRAME

print(productos_df.head(),'\f') #! MUESTRA LOS PRIMEROS 10 DATOS DEL DATAFRAME