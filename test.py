from PIL import Image
img = Image.open("./pfp_unedited.png")
print(img.getpixel((img.width,img.height)))