import os
import shutil

# Calea către folderul din care vrei să extragi fișierele
source_folder = 'C:/Users/tahio/Desktop/testab'
  # ← schimbă cu calea ta reală
destination_folder = 'C:/Users/tahio/Desktop/Portofoliu Python/file_organizer/examples'


# Creează folderul de destinație dacă nu există
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Parcurge toate fișierele din folderul sursă
for filename in os.listdir(source_folder):
    if filename.lower().endswith('.mp3'):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        # Copiază fișierul în folderul "examples"
        shutil.copy2(source_path, destination_path)
        print(f'Fișierul {filename} a fost copiat în {destination_folder}')
