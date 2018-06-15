# coding=utf-8

from captcha.image import ImageCaptcha

img = ImageCaptcha()
image = img.generate_image("python")
c = img.generate("aaaa")
p = c.read()
print(p)
image.show()
import pdb;pdb.set_trace()
image.save("python.jpg")