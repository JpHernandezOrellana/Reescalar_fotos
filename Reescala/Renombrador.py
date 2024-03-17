import os

def renombrar_imagenes_en_carpeta(ruta_carpeta):
    for root, dirs, files in os.walk(ruta_carpeta):
        for dir in dirs:
            ruta_carpeta_actual = os.path.join(root, dir)
            contador = 1

            for file in os.listdir(ruta_carpeta_actual):
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.heic', '.heif')):
                    nombre_archivo, extension = os.path.splitext(file)
                    nuevo_nombre = f"{dir}_{contador}{extension}"
                    ruta_imagen_actual = os.path.join(ruta_carpeta_actual, file)
                    ruta_imagen_nueva = os.path.join(ruta_carpeta_actual, nuevo_nombre)
                    os.rename(ruta_imagen_actual, ruta_imagen_nueva)
                    contador += 1


# Obtener la ruta del proyecto actual en PyCharm
ruta_proyecto = os.path.dirname(os.path.abspath(__file__))

# Llamar a la función para renombrar las imágenes en todas las carpetas y subcarpetas del proyecto
renombrar_imagenes_en_carpeta(ruta_proyecto)

print("Renombrado de imágenes completado.")