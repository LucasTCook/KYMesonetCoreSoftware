##      Kentucky Mesonet Core Software -- CS 496 WKU
##
##      Scope: To develop a dynamic map to visualize different weather data
##
##      Contributers: Dylan Howard

from PIL import Image

class Overlayer(object):
    def __init__(self,mask_path):
        self.mask = self.load(mask_path)

    def save(self,in_file,out_file):
        self.overlay = self.load(in_file)

        self.new_img = self.composite(self.overlay, self.mask)

        self.new_img.save(out_file,"PNG")

    def convert(self,img):
        return img.convert("RGBA")

    def load(self,img_path):
        return self.convert(Image.open(img_path))

    def composite(self,overlay,mask):
        return Image.alpha_composite(self.overlay, self.mask)
