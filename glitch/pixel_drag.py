from PIL import Image
import random

#pixel drag, it drags pixels. Modes: 0 - drag to right, 1 - drag to left
def pixeldrag(image, count, minsize, maxsize, direction):
    #load image into 2d-array
    pixels = image.load()
    
    #make output image base
    output_image = image.copy()

    #load output image into 2d-array
    output_pixels = output_image.load()

    #loop over every pixel it needs to drag.
    for n in range(count):
        #generate random size
        size = random.randint(minsize, maxsize)
        #choose random starting pixel
        lx = random.randint(0, image.width-1)
        ly = random.randint(0, image.height-1)
        #get color from starting pixel
        color = image.getpixel((lx, ly))
        #loop over every adjacent pixel in correct direction
        for s in range(size):
            #right
            if direction == 0:
                cx = lx + s
            #left
            if direction == 1:
                cx = lx - s
            #only change color if pixel falls in image
            if cx >= 0 and cx < image.width:
                output_pixels[cx, ly] = color
    # return the output
    return output_image