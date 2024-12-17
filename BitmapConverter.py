from PIL import Image
import os

class BitmapConverter:
    def __init__ (self):
        print ('__init__')
        
        self.currentPath      = os.getcwd ()
        self.bitmapExtensions = ('.jpg', '.bmp', '.gif', '.png')
        self.imageExtension   = '.hpp'
        self.fileHead         = self.__getFileContent (self.currentPath + '/Images/Template/head.hpp')
        self.fileTail         = self.__getFileContent (self.currentPath + '/Images/Template/tail.hpp')
        
    def __getFileContent (self, v_filePath):
        handle  = open (v_filePath, 'r')
        content = handle.read ()
        handle.close()  
        return content      

    def __getImageContent (self, vBitmapPathWithName):
        handle  = Image.open (vBitmapPathWithName).convert ('RGB')
        self.bitmapWidth, self.bitmapHeight = handle.size
        content = tuple (handle.getdata ())
        handle.close ()
        return content

    def __swapBytes (self, vWord):
        hByte = (vWord & 0xFF00) >> 8
        lByte = (vWord & 0x00FF)
        return ((lByte << 8) + hByte)

    def __converPixelToBigEndian (self, vPixel):
        red          = (vPixel [0] >> 3) & 0x1F
        green        = (vPixel [1] >> 2) & 0x3F
        blue         = (vPixel [2] >> 3) & 0x1F
        littleEndian = ((red << 11) + (green << 5) + blue)
        return self.__swapBytes (littleEndian)
            
    def __createImage (self, vBitmapName, vBitmapPathWithName, vImagePathWithName):
        pixels      = self.__getImageContent (vBitmapPathWithName)
        imageHandle = open (vImagePathWithName, 'w')
        imageHandle.write (self.fileHead)
        imageHandle.write ('\n\nstatic const uint16_t ' + vBitmapName + ' [] = \n{ \n    ')
        imageHandle.write ('0x{:04x}'.format (self.bitmapWidth) + ', ')
        imageHandle.write ('0x{:04x}'.format (self.bitmapHeight) + ', ')
        imageHandle.write ('\n    ')
            
        pixelNum = 1
        for pixel in pixels:
            bigEndian = self.__converPixelToBigEndian (pixel)
            imageHandle.write ('0x{:04x}'.format (bigEndian) + ', ')
            
            if pixelNum % 16 == 0:
                imageHandle.write ('\n    ')

            pixelNum = pixelNum + 1
            
        imageHandle.write ('\n};\n\n')
        imageHandle.write (self.fileTail)
        imageHandle.close ()
        
    def __searchFiles (self, vPath, vExtension):
        filesList = []
        for root, dirs, files in os.walk (vPath):
            for file in files:
               if file.endswith (vExtension):
                   filesList.append (root + '/' + file)
        return filesList
        
                    
    def ConvertBitmapsToImages (self):
        print ('ConvertBitmapsToImages')

        for bitmapExtension in self.bitmapExtensions:
            bitmaps = self.__searchFiles (self.currentPath + '/Bitmaps', bitmapExtension)

            for bitmap in bitmaps:
                image = bitmap [:-4] + self.imageExtension
                image = image.replace ("Bitmaps", "Images")
                
                print ('Convert: \n {0} to \n {1} \n'.format (bitmap, image))
                self.__createImage (self.__getBitmapName (bitmap), bitmap, image)
              
    def __getBitmapName (self, vBitmapPath):
        splitedPath            = vBitmapPath.split ('/')
        bitmapNameWihExtension = splitedPath [len (splitedPath) - 1]
        bitmapNameExtension    = bitmapNameWihExtension [-4:]
        return bitmapNameWihExtension [:-len (bitmapNameExtension)]
              
def main ():
    bitmapConverter = BitmapConverter ()
    bitmapConverter.ConvertBitmapsToImages ()
        
if __name__ == "__main__": 
    main()
