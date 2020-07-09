from PIL import Image
from tqdm import tqdm
from glitch.color_offset import channel_offset
from glitch.jitter import jitter
from glitch.pixel_drag import pixeldrag
off_zero = [0, 0, 0, 0, 0, 0]
input_img = Image.open("./loona4.png")

for f in tqdm(range(120), desc="rendering frame"):
    jimg = jitter(input_img, 20, -10, 10, 2)
    pimg = pixeldrag(jimg, 1000, 2, 60, 0)
    cimg = channel_offset(pimg, -15, -15, 15, 15, True, [1, 0, 1], off_zero)
    cimg.save("./frames/" + str(f) + ".png")