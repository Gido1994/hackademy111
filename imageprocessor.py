from PIL import Image
import code
import os

def rotate_box(an_image):
    box = (100,100,400,400)
    region_im = an_image.crop(box)
    transposed_im = region_im.transpose(Image.ROTATE_180)
    an_image.paste(transposed_im,box)
    return an_image

def to_grayscale(an_image):
    grayscale_im = an_image.convert('L')
    return grayscale_im




pic_list = code.get_filenames("C:\\Users\\GiDo1994\\Desktop\\pictures")
num = 0
for pic_name in pic_list:
    im = Image.open(pic_name)
    im = to_grayscale(im)

    newfilename = "pic_gray_" + str(num) + ".jpg"
    num = num + 1
    newfullpath = os.path.join("C:\\Users\\GiDo1994\\Desktop\\pictures\\grayscale",newfilename)

    im.save(newfullpath)

    