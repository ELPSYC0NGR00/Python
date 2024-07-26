#Se importan librerias
from docxtpl import DocxTemplate
from datetime import datetime
import pandas as pd

#carga la fecha del dia
fecha_hoy = datetime.today().strftime("%d %b, %Y")

#Cargar la data de inventario
df = pd.read_csv('inventario_prestamo.csv', delimiter = ";")

#setea fecha en la plantilla
my_context = { 'fecha_hoy' : fecha_hoy}
    
#imput consulta si es entrega o devolucion
operation = input("Es una entrega o una devolucion? (entrega (e)/devolucion(d)): ").strip().lower()

if operation == 'e':
    template_path = "plantilla_entrega.docx"
    tipo = 'entrega'
elif operation == 'd':
    template_path = "plantilla_devolucion.docx"
    tipo = 'devolucion'
else:
    print("Operación no válida. Por favor, ejecute el programa de nuevo y seleccione 'entrega' o 'devolucion'.")
    exit()

#busca info de las celdas para la plantilla
for index, fila in df.iterrows():
    if fila.notnull().any(): 

        doc = DocxTemplate(template_path)

    context = {
            'nombre_usuario': fila['nombre'] if pd.notnull(fila['nombre']) else " ",
            'perisferico_1A': fila['equipo'] if pd.notnull(fila['equipo']) else " ",
            'perisferico_1B': fila['marca'] if pd.notnull(fila['marca']) else " ",
            'perisferico_1C': fila['modelo'] if pd.notnull(fila['modelo']) else " ",
            'perisferico_1D': fila['numero_serie'] if pd.notnull(fila['numero_serie']) else " ",
            'perisferico_2A': fila['equipo2'] if pd.notnull(fila['equipo2']) else " ",
            'perisferico_2B': fila['marca2'] if pd.notnull(fila['marca2']) else " ",
            'perisferico_2C': fila['modelo2'] if pd.notnull(fila['modelo2']) else " ",
            'perisferico_2D': fila['numero_serie2'] if pd.notnull(fila['numero_serie2']) else " ",
            'perisferico_3A': fila['equipo3'] if pd.notnull(fila['equipo3']) else " ",
            'perisferico_3B': fila['marca3'] if pd.notnull(fila['marca3']) else " ",
            'perisferico_3C': fila['modelo3'] if pd.notnull(fila['modelo3']) else " ",
            'perisferico_3D': fila['numero_serie3'] if pd.notnull(fila['numero_serie3']) else " ",
            'perisferico_4A': fila['equipo4'] if pd.notnull(fila['equipo4']) else " ",
            'perisferico_4B': fila['marca4'] if pd.notnull(fila['marca4']) else " ",
            'perisferico_4C': fila['modelo4'] if pd.notnull(fila['modelo4']) else " ",
            'perisferico_4D': fila['numero_serie4'] if pd.notnull(fila['numero_serie4']) else " ",
        }

    context.update(my_context)
    
    doc.render(context)
    doc.save(f"{tipo}_doc_{fila['nombre']}.docx")



numbers = {
  "first": 1,
  "second": 2,
  "third": 3,
  "fourth": 4,
}
