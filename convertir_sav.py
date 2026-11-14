import os
import glob
import pandas as pd
import pyreadstat

# ---------------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------------
# Carpeta donde están los archivos ('.' significa la carpeta actual)
carpeta_entrada = '.' 
# Carpeta donde se guardarán los .csv (puede ser la misma)
carpeta_salida = '.' 

# Buscar todos los archivos con extensión .sav en la carpeta
archivos_sav = glob.glob(os.path.join(carpeta_entrada, '*.sav'))

if not archivos_sav:
    print("No se encontraron archivos .sav en la carpeta especificada.")
else:
    print(f"Se encontraron {len(archivos_sav)} archivos para convertir.\n")
    
    for archivo in archivos_sav:
        try:
            # Obtener el nombre del archivo sin la ruta y sin la extensión
            nombre_archivo = os.path.basename(archivo)
            nombre_sin_extension = os.path.splitext(nombre_archivo)[0]
            
            # Ruta completa para el nuevo archivo .csv
            archivo_csv = os.path.join(carpeta_salida, f"{nombre_sin_extension}.csv")
            
            print(f"Convirtiendo: {nombre_archivo} ...")
            
            # Leer el archivo .sav
            # pyreadstat devuelve un DataFrame de pandas y un objeto con metadatos
            df, meta = pyreadstat.read_sav(archivo)
            
            # Guardar como CSV
            # utf-8-sig es ideal para que Excel reconozca las tildes y la 'ñ' correctamente
            df.to_csv(archivo_csv, index=False, encoding='utf-8-sig')
            
            print(f"  -> Guardado como: {nombre_sin_extension}.csv (Éxito)")
            
        except Exception as e:
            print(f"  -> Error al convertir {archivo}: {e}")

    print("\n¡Proceso de conversión terminado!")