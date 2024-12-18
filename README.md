# BitmapConverter

# I. Description:
Script is used to convert bitmaps to images. Script works with such file formats as jpg, bmp, gif, and png.

# II. Assumptions:
The code stored in BitmapConverter.py is adapted to ILI9341 settings in my internal project(s):
- Eight bits pixels packed in sixteen bits data,
- Sixteen bits data in big endian format,
- Bitmaps converted to images wrapped in .hpp files.

# III. Structure:
- BitmapConverter
  - Bitmaps
    - folder1
    - ...
  - Images
    - Templates
      - head.h
      - tail.h
    - folder1
    - ...
  - BitmapConverter.py

# IV. Configuration:
- Python 3.12.3 version,
- Python PIL library.

# V. Script execution:
Before executing the script, you should have the file structure as in point III. If you have subfolders in "Bitmaps" you should have same in "Images".

- Go to folder BitmapConverter,
- Open shell console,
- Execute python3 ./BitmapConverter.py,
- Go to the Images location to check the generated files.

The script also displays the found bitmaps and the converted files.

- Usefull bitmaps .jpeg to .bmp converter https://convertio.co/pl/

