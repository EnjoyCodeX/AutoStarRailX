# tesseract-ocr 图像识别文字 https://blog.csdn.net/woshiabc111/article/details/134739325
from PIL import Image
import pytesseract
tesseract_cmd = r'C:\AndrewT\GITHUB\tesseract-ocr\tesseract'
pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

img = Image.open('./LocationPhoto/GOIN.png')
print(pytesseract.image_to_string(img,lang='chi_sim'))