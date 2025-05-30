# File Organizer 📁

This project automatically organizes files in a source folder by extension (ex: `.jpg`, `.png`) and moves them into dedicated subfolders.

## 🔧 Functionality

- Moves files with certain extensions from one folder to another.
- Automatically creates destination folders (`jpg/`, `png/` etc.) if they do not exist.
- Can be extended for other file types.

## 📂 Project structure

file_organizer/
│
├── main.py # The main script that handles file moving
├── README.md # This file
└── examples/ # Destination folder where files will be organized

## ▶️ How to Use

1. Open `main.py` in Visual Studio Code (or any Python editor).
2. Replace `source_folder` in the code with the path to your folder containing the files to sort.
3. Run the script:
   ```bash
   python main.py

📝 Additional Notes
Make sure to modify and use your own directory path in the source_folder and destination_folder variables.

The examples/ folder is kept empty — you can use your own files for testing.

You can easily change the file extension filter in the code to organize other formats (not just .jpg).
