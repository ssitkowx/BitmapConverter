# BitmapConverter

# I. Description:
Script is used to convert bitmaps to images. Script works with such file formats as jpg, bmp, gif, and png.

# II. Assumptions:
The code stored in BitmapConverter.py is adapted to ILI9341 settings in EvolutionBoard project:
- Eight bits pixels packed in sixteen bits data,
- Sixteen bits data in big endian format,
- Bitmaps converted to images wrapped in .h files.

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
Before executing the script, you should:
- Have the file structure as in point III. If you have subfolders in "Bitmaps"" folder you should have same in "Images"
- Execute BitmapConverter.py:

1. Go to folder BitmapConverter,
2. Open shell console,
3. Execute python3 ./BitmapConverter.py,
4. Go to the Images location to check the generated files.

The script also displays the found bitmaps and the converted files.

- Usefull bitmaps .jpeg to .bmp converter https://convertio.co/pl/download/c70856bc9489ba23ef58070dd9255ee7f828eb/

