# https://blog.csdn.net/m0_53043024/article/details/133667872
# https://zhuanlan.zhihu.com/p/266123806
# Creating virtualenv autostar-mkdqbjJF-py3.10 in C:\Users\tracy\AppData\Local\pypoetry\Cache\virtualenvs
import pyautogui
import time
import logging
import configparser

# https://pythonjishu.com/wliymtlxkzknzyw/

config = configparser.ConfigParser()
config.read('config.ini')

# 创建loggger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 创建handler，写入日志文件
logfile = './log.txt'
fh = logging.FileHandler(logfile,mode='a')
fh.setLevel(logging.DEBUG)

#  创建handler，用于输出控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)

# 定义handler 输出格式
format = logging.Formatter("%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s : %(message)s")
fh.setFormatter(format)
ch.setFormatter(format)

# 将logger添加到handler
logger.addHandler(fh)
logger.addHandler(ch)

type = config.get('Loading','AccessType')

"""
工作流程:
打开edge浏览器 --> 搜索云崩坏星穹铁道 --> 进入官网 --> 打开游戏 --> 完成每日任务 --> 获得每日奖励
"""
# 打开edge浏览器 --> 搜索云崩坏星穹铁道 --> 进入官网 --> 打开游戏
pyautogui.useImageNotFoundException()

def Locate(word,confi,gray=False,way=True):
    try:
        """
        locationCenterOnScreen(图像路径,[匹配精度,灰度匹配])
        """
        # 获取按钮位置
        url = './LocationPhoto/{}.png'.format(word)
        img = pyautogui.screenshot('test.png')
        Location = pyautogui.locateCenterOnScreen(url,confidence=confi,grayscale=gray)
        logger.info('image found:{}'.format(Location))
        return Location
    except pyautogui.ImageNotFoundException:
        if way:
            logger.error('image not found,please check')
            exit()
        else:
            return None
    
# 没找到图像一直找
def get_position(word):
    begintime = time.time()
    found = None
    while found == None:
        found = Locate(word,0.8,way=False)
        accetime = time.time()
        if accetime - begintime >= 60:
            logger.error('Can not access')
            exit()
    return found

def click(Location,cls,but,ti=2):
    pyautogui.click(Location,clicks=cls,button=but)
    time.sleep(ti)

Location = Locate('edge',0.8)
click(Location,1,'left')

Location = Locate('search',0.9)
pyautogui.moveTo(Location)
# 窗口最大化
pyautogui.hotkey('alt','space','x')

click(Location,1,'left',5)
Location = Locate('GOIN',0.7)
click(Location,1,'left')

# 进入游戏
match type:
    case '1':
        Location = get_position(2)
        click(Location,1,'left',2)
    case '2':
        logger.info('Welcome to use autoplay again')
    case _:
        logger.error('please check your access way, 1 - first time access cloud game  2 -not')
        exit()

Location = get_position(3)
click(Location,1,'left')

"""
配置文件 config
1、模拟宇宙   
2、拟造花萼(金)
3、拟造花萼(赤)
4、凝滞虚影
5、侵蚀隧洞
6、历战余响
7、每日任务
8、队伍配置
9、纪行
"""

# 测试完成自动化战斗
