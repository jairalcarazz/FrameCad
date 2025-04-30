import ezdxf

# Cargar el archivo DXF exportado desde AutoCAD
doc = ezdxf.readfile("Stud.dxf")
msp = doc.modelspace()

# Leer las entidades del cubo 3D
for entity in msp:
    print(entity)

# Escalar o manipular las medidas (Ejemplo para entidades específicas)
for entity in msp.query('LINE'):
    start_point = entity.dxf.start
    end_point = entity.dxf.end
    print(f"Start: {start_point}, End: {end_point}")
    
    # Cambiar las coordenadas para redimensionar el cubo
    new_start_point = (start_point[0] * 2, start_point[1] * 2, start_point[2] * 2)
    new_end_point = (end_point[0] * 2, end_point[1] * 2, end_point[2] * 2)
    
    # Actualizar el cubo con las nuevas dimensiones
    entity.dxf.start = new_start_point
    entity.dxf.end = new_end_point

# Guardar los cambios
doc.saveas("cubo_redimensionado.dxf")
