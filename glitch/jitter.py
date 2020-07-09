from PIL import Image
import random
import math

#slices an image into slices with a set size and max offset. Modes: 0 = none, 1 = wrap around, 2 = reflect from side
def jitter(image, slice_size, min_off, max_off, mode):
    #load the image into a 2d-array
    pixels = image.load()

    #make output image base
    output_image = Image.new("RGB", image.size, "black")

    #load output image into 2d-array
    output_pixels = output_image.load()
    
    #loop over rows in image
    for py in range(image.height):
        #if row is start of new slice -> generate new random offset
        if py%slice_size == 0:
            offset = random.randint(min_off, max_off)
        #loop over pixels in row
        for px in range(image.width):
            #apply random offset
            cpx = px + offset

            #check if pixel is in image
            if cpx >= 0 and cpx < image.width:
                color = image.getpixel((cpx, py))
            else:
                #is mode none?
                if mode == 0:
                    #set to black
                    color = (0, 0, 0)

                #is mode wrap?
                if mode == 1:
                    #loop negative
                    if cpx < 0:
                        color = image.getpixel((cpx + image.width - 1, py))
                    #loop positive
                    if cpx > image.width - 1:
                        color = image.getpixel((cpx - image.width, py))
                #is mode reflect?
                if mode == 2:
                    #reflect negative
                    if cpx < 0:
                        color = image.getpixel((cpx * -1, py))
                    #reflect positive
                    if cpx > image.width - 1:
                        color = image.getpixel((image.width - (cpx - image.width) - 1, py))
            output_pixels[px, py] = color
    return output_image