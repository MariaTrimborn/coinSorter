from PIL import Image
import glob
image_list = []
x = 1
y = 18111
z = 28222
a = 37333
b = 49444
c = 52555
d = 61766
e = 76777
f = 80888
g = 97999
h = 1221111

for filename in glob.glob('pics/*.jpg' and 'pics/*.png'):
    
 
    colorImage  = Image.open(filename)
    rotated     = colorImage.rotate(20)
   
    
    test = rotated.save('pics/15/coin%d.png' % x)

    x = x + 1


for filename in glob.glob('pics/15/*.png'):
    
 
    colorImage  = Image.open(filename)
    rotated     = colorImage.rotate(20)
    test = rotated.save('pics/45/coin%d.png' % y)

    y = y + 1

for filename in glob.glob('pics/45/*.png'):
    
 
    colorImage  = Image.open(filename)
    rotated     = colorImage.rotate(20)
    test = rotated.save('pics/90/coin%d.png' % z)

    z = z + 1

for filename in glob.glob('pics/90/*.png'):
   
 
    colorImage  = Image.open(filename)
    rotated     = colorImage.rotate(20)
    test = rotated.save('pics/120/coin%d.png' % a)

    a = a + 1

for filename in glob.glob('pics/120/*.png'):
    
 
    colorImage  = Image.open(filename)
    rotated     = colorImage.rotate(20)
    test = rotated.save('pics/150/coin%d.png' % b)

    b = b + 1

for filename in glob.glob('pics/150/*.png'):
    
 
    colorImage  = Image.open(filename)
    rotated     = colorImage.rotate(20)
    test = rotated.save('pics/180/coin%d.png' % c)

    c = c + 1

for filename in glob.glob('pics/180/*.png'):
   
 
    colorImage  = Image.open(filename)
    rotated     = colorImage.rotate(20)
    test = rotated.save('pics/210/coin%d.png' % d)

    d = d + 1

for filename in glob.glob('pics/210/*.png'):
    
    colorImage  = Image.open(filename)
    rotated     = colorImage.rotate(20)
    test = rotated.save('pics/240/coin%d.png' % e)

    e = e + 1

for filename in glob.glob('pics/240/*.png'):
    
 
    colorImage  = Image.open(filename)
    rotated     = colorImage.rotate(20)
    test = rotated.save('pics/270/coin%d.png' % f)

    f = f + 1

for filename in glob.glob('pics/270/*.png'):
    
 
    colorImage  = Image.open(filename)
    rotated     = colorImage.rotate(30)
    test = rotated.save('pics/300/coin%d.png' % g)

    g = g + 1

for filename in glob.glob('pics/300/*.png'):
    
 
    colorImage  = Image.open(filename)
    rotated     = colorImage.rotate(30)
    test = rotated.save('pics/330/coin%d.png' % g)

    g = g + 1