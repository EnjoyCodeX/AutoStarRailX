# tesseract-ocr 图像识别文字 https://blog.csdn.net/woshiabc111/article/details/134739325
# from PIL import Image
# import pytesseract
# tesseract_cmd = r'C:\AndrewT\GITHUB\tesseract-ocr\tesseract'
# pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

# img = Image.open('./LocationPhoto/test/1.png')
# print(pytesseract.image_to_string(img))

# import pyautogui
# import time
# pyautogui.useImageNotFoundException()
# def Locate(word,confi,gray=False,way=True):
#     try:
#         """
#         locationCenterOnScreen(图像路径,[匹配精度,灰度匹配])
#         """
#         # 获取按钮位置
#         url = './LocationPhoto/{}.png'.format(word)
#         img = pyautogui.screenshot('test.png')
#         Location = pyautogui.locateCenterOnScreen(url,confidence=confi,grayscale=gray)
#         # logger.info('image found:{}'.format(Location))
#         return Location
#     except pyautogui.ImageNotFoundException:
#         if way:
#             # logger.error('image not found,please check')
#             exit()
#         else:
#             return None
# def IntoGuide():
#     pyautogui.press('esc')
#     time.sleep(2)
#     Location = Locate('Menu',0.8,gray=True)
#     click(Location,1,'left',2)

# def click(Location,cls,but,ti=2):
#     pyautogui.click(Location,clicks=cls,button=but)
#     time.sleep(ti)

# ScreenWidth,ScreenHeight = pyautogui.size()
# pyautogui.click(ScreenWidth/2, ScreenHeight/2,clicks=3,interval=1,button='left')
# time.sleep(2)
# IntoGuide()
