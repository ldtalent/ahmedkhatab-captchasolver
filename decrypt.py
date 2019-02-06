
from PIL import Image
from scipy.ndimage.filters import gaussian_filter
import numpy
import pytesseract
from PIL import ImageFilter
# thresold1 on the first stage
th1 = 140
th2 = 140 # threshold after blurring 
sig = 1.5 # the blurring sigma

from scipy import ndimage
original = Image.open("image.png")
original.save("original.png") # reading the image from the request
black_and_white =original.convert("L") #converting to black and white 
black_and_white.save("black_and_white.png")
first_threshold = black_and_white.point(lambda p: p > th1 and 255)
first_threshold.save("first_threshold.png")
blur=numpy.array(first_threshold) #create an image array
blurred = gaussian_filter(blur, sigma=sig)
blurred = Image.fromarray(blurred)
blurred.save("blurred.png")
final = blurred.point(lambda p: p > th2 and 255)
final = final.filter(ImageFilter.EDGE_ENHANCE_MORE)
final = final.filter(ImageFilter.SHARPEN)
final.save("final.png")
number = pytesseract.image_to_string(Image.open('final.png'))
print number
