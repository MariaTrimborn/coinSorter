from PIL import Image
import glob

def flip():
    
    filename = 'front.png'
    colorImage  = Image.open(filename) 
    rotated     = colorImage.rotate(30) 
    test = rotated.save('front.png')
