# pip3.10 install openpyxl
import openpyxl
import io

# Ruta al archivo byte descargado
archivo_byte = 'data2.net_7e80c8ad-b3b2-4fd9-90e6-35791b123e5e'

# Abre el archivo byte
with open(archivo_byte, 'rb') as f:
    contenido_byte = io.BytesIO(f.read())

# Carga el archivo byte en openpyxl
libro_excel = openpyxl.load_workbook(filename=contenido_byte)

# Haz algo con el archivo de Excel
hoja = libro_excel.active
print(hoja['A1'].value)

# Guarda el archivo de Excel
libro_excel.save('newexcel2.xlsx')
