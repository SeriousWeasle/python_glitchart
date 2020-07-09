from PIL import Image
import random

#function to add color channel offset to an image.
def channel_offset(image:Image, min_x:int, min_y:int, max_x:int, max_y:int, rand_offset:bool, colorflags, custom_offsets):
    #load image as 2d-array containing pixel data
    pixels = image.load()
    
    #make color channels from image
    color_channels = Image.Image.split(image)

    #make output image base
    output_image = Image.new("RGB", image.size, "black")

    #load output image into 2d-array
    output_pixels = output_image.load()

    #if random is True, do random offsets
    if rand_offset == True:

        #generate random offsets based on min/max bounds for red channel
        #check if red needs random offset
        if colorflags[0] == 0:
            #no random offsets
            r_off_x = 0
            r_off_y = 0
        else:
            #random offsets
            r_off_x = random.randint(min_x, max_x)
            r_off_y = random.randint(min_y, max_y)
        
        #generate random offsets based on min/max bounds for green channel
        #check if green needs random offsets
        if colorflags[1] == 0:
            #no random offsets
            g_off_x = 0
            g_off_y = 0
        else:
            #random offsets
            g_off_x = random.randint(min_x, max_x)
            g_off_y = random.randint(min_y, max_y)

        #generate random offsets based on min/max bounds for blue channel
        if colorflags[2] == 0:
            #no random offsets
            b_off_x = 0
            b_off_y = 0
        else:
            #random offsets
            b_off_x = random.randint(min_x, max_x)
            b_off_y = random.randint(min_y, max_y)
    
    if rand_offset == False:
        #get red offsets
        r_off_x = custom_offsets[0]
        r_off_y = custom_offsets[1]

        #get green offsets
        g_off_x = custom_offsets[2]
        g_off_y = custom_offsets[3]
        
        #get blue offsets
        b_off_x = custom_offsets[4]
        b_off_y = custom_offsets[5]

    #applying color channel offset
    #loop over rows in image:
    for py in range(image.height):
        #loop over pixels in row:
        for px in range(image.width):
            #calculate current red channel position
            cpx_r = px + r_off_x
            cpy_r = py + r_off_y

            #calculate current green channel position
            cpx_g = px + g_off_x
            cpy_g = py + g_off_y

            #calculate current blue channel position
            cpx_b = px + b_off_x
            cpy_b = py + b_off_y

            #check if red pixel falls in image:
            if cpx_r >= 0 and cpx_r < image.width and cpy_r >= 0 and cpy_r < image.height:
                r = color_channels[0].getpixel((cpx_r, cpy_r))
            else:
                r = 0
            
            #check if green pixel falls in image:
            if cpx_g >= 0 and cpx_g < image.width and cpy_g >= 0 and cpy_g < image.height:
                g = color_channels[1].getpixel((cpx_g, cpy_g))
            else:
                g = 0
            
            #check if blue pixel falls in image:
            if cpx_b >= 0 and cpx_b < image.width and cpy_b >= 0 and cpy_b < image.height:
                b = color_channels[2].getpixel((cpx_b, cpy_b))
            else:
                b = 0
            
            #add pixel to output
            output_pixels[px, py] = (r, g, b)
    #give the distorted image back as image
    return output_image
