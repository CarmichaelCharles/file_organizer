import os
import shutil

# Calea către folderul din care vrei să extragi fișierele
source_folder = "input_folder"
  # ← schimbă cu calea ta reală
destination_folder = "examples/jpg"


# Creează folderul de destinație dacă nu există
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Parcurge toate fișierele din folderul sursă
for filename in os.listdir(source_folder):
    if filename.lower().endswith('.jpg'):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        # Copiază fișierul în folderul "examples"
        shutil.copy2(source_path, destination_path)
        print(f'Fișierul {filename} a fost copiat în {destination_folder}')
