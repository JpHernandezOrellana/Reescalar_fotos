import os
from PIL import Image
from PIL import UnidentifiedImageError


def reescalar_imagen(ruta_imagen, ruta_destino, max_alto=1200, calidad=90):
    try:
        with Image.open(ruta_imagen) as img:
            ancho, alto = img.size
            if alto > max_alto:
                nuevo_ancho = int(ancho * (max_alto / alto))
                img = img.resize((nuevo_ancho, max_alto), Image.LANCZOS)

            nombre_archivo, extension = os.path.splitext(os.path.basename(ruta_imagen))
            nueva_ruta = os.path.join(ruta_destino, nombre_archivo + '_reescalada' + extension)

            if extension.lower() in ['.jpg', '.jpeg', '.heic', '.heif']:
                img.save(nueva_ruta, 'JPEG', quality=calidad, optimize=True)
            else:
                img.save(nueva_ruta, quality=calidad, optimize=True)
    except UnidentifiedImageError:
        print(f"No se pudo abrir la imagen: {ruta_imagen}")


def reescalar_imagenes_en_carpeta(ruta_carpeta, distintivo='_reescaladas'):
    for root, dirs, files in os.walk(ruta_carpeta):
        for dir in dirs:
            ruta_origen = os.path.join(root, dir)
            ruta_destino = os.path.join(root, dir + distintivo)
            os.makedirs(ruta_destino, exist_ok=True)

            for file in os.listdir(ruta_origen):
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.heic', '.heif')):
                    ruta_imagen = os.path.join(ruta_origen, file)
                    reescalar_imagen(ruta_imagen, ruta_destino)


# Obtener la ruta del proyecto actual en PyCharm
ruta_proyecto = os.path.dirname(os.path.abspath(__file__))

# Llamar a la función para reescalar las imágenes en todas las carpetas y subcarpetas del proyecto
reescalar_imagenes_en_carpeta(ruta_proyecto)

print("Reescalado de imágenes completado.")