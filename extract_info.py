import os
import shutil
import zipfile

def extract_content_json(source_folder, destination_folder):
    # Crear la carpeta de destino si no existe
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterar sobre los archivos en la carpeta de origen
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.h5p'):
                h5p_file = os.path.join(root, file)
                # Crear una carpeta para extraer el contenido
                destination_path = os.path.join(destination_folder, os.path.splitext(file)[0])
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)
                # Extraer solo el archivo content.json del archivo h5p
                with zipfile.ZipFile(h5p_file, 'r') as zip_ref:
                    for item in zip_ref.namelist():
                        if 'content.json' in item:
                            zip_ref.extract(item, destination_path)

# Carpeta de origen de los archivos h5p
source_folder = 'h5p-exercises'

# Carpeta de destino para la extracción
destination_folder = 'h5p-content-json'

# Extraer los archivos content.json de los archivos h5p
extract_content_json(source_folder, destination_folder)
print("Proceso completado.")
