# https://blog.csdn.net/m0_53043024/article/details/133667872
# https://blog.csdn.net/wblylh/article/details/114533120
# https://zhuanlan.zhihu.com/p/266123806
# Creating virtualenv autostar-mkdqbjJF-py3.10 in C:\Users\tracy\AppData\Local\pypoetry\Cache\virtualenvs
import pyautogui
import time
import logging
import configparser

# https://pythonjishu.com/wliymtlxkzknzyw/
# pyautogui.FAILSAFE=False

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
Accessconfidence = config.get('Loading','AccessConfidence')
GameConfidence = config.get('Loading','GameConfidence')
gray = config.get('Loading','Gray')
isgray = True if gray=='1' else False

"""
工作流程:
打开edge浏览器 --> 搜索云崩坏星穹铁道 --> 进入官网 --> 打开游戏 --> 完成每日任务 --> 获得每日奖励
"""
# 打开edge浏览器 --> 搜索云崩坏星穹铁道 --> 进入官网 --> 打开游戏
pyautogui.useImageNotFoundException()

# 定位坐标
def Locate(word,confi,gray=isgray,way=True):
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
def get_position(word,times = 120):
    begintime = time.time()
    found = None
    while found == None:
        found = Locate(word,GameConfidence,way=False)
        accetime = time.time()
        if accetime - begintime >= times:
            logger.error('Can not access')
            exit()
    return found

def click(Location,cls,but,ti=2):
    pyautogui.click(Location,clicks=cls,button=but)
    time.sleep(ti)

# 登录操作
def Loading():
    Location = Locate('Load/edge',Accessconfidence)
    click(Location,1,'left')

    # 窗口最大化
    pyautogui.hotkey('alt','space')
    Location = Locate('Load/sizeup',Accessconfidence)
    click(Location,1,'left',2)
    # 以免已经最大化后出现问题
    click((1000,20),1,'left',1)

    Location = Locate('Load/search',Accessconfidence)
    click(Location,1,'left',5)
    Location = Locate('Load/GOIN',Accessconfidence)
    click(Location,1,'left')

    # 此处应该考虑排队时间 和 网速问题
    begtime = time.time()
    if Location != None:
        Location = Locate('Load/wifi',Accessconfidence,way=False)
        logger.warning('The speed of wifi is poor')
        click(Location,1,'left',2)
        accesstime = time.time()
        if accesstime - begtime >= 60:
            logger.error('Can not get into the game, please change your wifi')
            exit()

    Location = 1
    while Location!=None:
        Location = Locate('Load/wait',Accessconfidence,way=False)
        logger.warning('please wait a while')
        time.sleep(20)
    # 进入游戏
    match type:
        case '1':
            Location = get_position('Load/2')
            click(Location,1,'left',2)
        case '2':
            logger.info('Welcome to use autoplay again')
        case _:
            logger.error('please check your access way, 1 - first time access cloud game  2 -not')
            exit()
    Location = get_position('Load/3')
    click(Location,1,'left')

# 进入指南
def IntoGuide():
    pyautogui.press('esc')
    time.sleep(2)
    Location = Locate('Menu',GameConfidence)
    click(Location,1,'left',2)

# 领取月卡奖励
def getReward():
    ScreenWidth,ScreenHeight = pyautogui.size()
    pyautogui.click(ScreenWidth/2, ScreenHeight/2 + 200 ,clicks=2,interval=2,button='left')
    time.sleep(2)

# 邮箱奖励

# 每日委托
def delegate():
    pyautogui.press('esc')
    time.sleep(2)
    Location = Locate('Daily/delegate',GameConfidence)
    logger.info('正在进入每日委托')
    click(Location,1,'left',2)
    # 若没领取，先进行领取

    # 派遣
    returnHome()
    

# 完成使用支援角色并获取胜利
def helpvictory():
    IntoGuide()
    Location = Locate('Daily/3',GameConfidence,way=False)
    if Location != None:
        click(Location,1,'left',2)
    Location = Locate('Fight/1',GameConfidence)
    click(Location,1,'left',2)
    Location = Locate('Daily/4',GameConfidence)
    click(Location,1,'left',5)
    Location = Locate('Daily/5',GameConfidence)
    click(Location,1,'left',2)
    help()
    Location = Locate('Daily/6',GameConfidence)
    click(Location,1,'left',2)
    Location = get_position('Daily/exit',60)
    click(Location,1,'left',2)
    logger.info('finish help dailywork')

# 每日任务
def dailyWork():
    delegate()
    helpvictory()
    center = CenterBack()
    click(center,1,'left',1)
    getdailyReward()

# 获取每日奖励
def getdailyReward():
    IntoGuide()
    Location = Locate('Daily/1-2',GameConfidence)
    click(Location,1,'left')
    while Location != None:
        Location = Locate('Daily/1-1',GameConfidence,way=False)
        click(Location,1,'left',2)
    Location = Locate('Daily/2',GameConfidence,way=False)
    click(Location,1,'left',1)
    returnHome()

# 支援
def help():
    Location = Locate('help',GameConfidence)
    click(Location,1,'left',2)
    Location = Locate('Helper',GameConfidence)
    click(Location,1,'left',2)

# 纪行
 
# 商城兑换

# 返回屏幕中心
def CenterBack():
    ScreenWidth,ScreenHeight = pyautogui.size()
    pyautogui.moveTo(ScreenWidth/2, ScreenHeight/2)
    return ScreenWidth/2,ScreenHeight/2

# 返回主界面
def returnHome():
    pyautogui.press('esc')
    time.sleep(1)
    center = CenterBack()
    pyautogui.click(center[0],center[1],clicks=1,button='left')
    time.sleep(1)
   
if __name__ == '__main__' :
    Loading()
    getReward()
    # 先进行每日任务，待完成后再清体力
    dailyWork()
