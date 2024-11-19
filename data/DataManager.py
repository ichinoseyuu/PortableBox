import os, json
from PySide6.QtGui import QFont
class UserData():
    appDataFileName = './data/app_data.json'
    settingsDataFileName = './data/settings.json'
    appDocker = {}
    settingsData = {}    

    def initialize(size: tuple[int,int]):
        UserData.appDocker = {
            row: {col: {'path': 'none'} for col in range(0,size[1])}
            for row in range(0,size[0])
        }
        UserData.settingsData = {
            'theme': 'light',
            'font': '微软雅黑',
        }

    @staticmethod
    def checkDataPathIsExist():
        # 检查文件夹是否存在，如果不存在则创建
        dataDir = os.path.dirname(UserData.appDataFileName)
        
        # 确保 Data 文件夹存在
        if not os.path.exists(dataDir):
            os.makedirs(dataDir)  # 创建文件夹

        # 检查 appData 文件是否存在，如果不存在则创建, 并初始化
        if not os.path.exists(UserData.appDataFileName):
           with open(UserData.appDataFileName, 'w', encoding='utf-8') as jsonFile:
               json.dump(UserData.appDocker, jsonFile, indent=4)
 
        # 检查 settingsData 文件是否存在，如果不存在则创建, 并初始化
        if not os.path.exists(UserData.settingsDataFileName):
           with open(UserData.settingsDataFileName, 'w', encoding='utf-8') as jsonFile:
                json.dump(UserData.settingsData, jsonFile, indent=4)

    # 加载数据
    @ staticmethod
    def loadUserData():    
        # 读取 appData 文件并加载数据
        with open(UserData.appDataFileName, 'r', encoding='utf-8') as jsonFile:
            datas = json.load(jsonFile)
            for row, col_data in datas.items():
                row = int(row)
                UserData.appDocker[row] = {}
                for col, value in col_data.items():
                    col = int(col)
                    UserData.appDocker[row][col] = value

        # 读取 settingsData 文件并加载数据
        with open(UserData.settingsDataFileName, 'r', encoding='utf-8') as jsonFile:
            UserData.settingsData = json.load(jsonFile)

        # 显示读取的数据
        UserData.displayData()

    
    # 保存数据
    @ staticmethod
    def saveUserData():
        # 检查文件夹是否存在，如果不存在则创建
        dataDir = os.path.dirname(UserData.appDataFileName)
        # 确保 Data 文件夹存在
        if not os.path.exists(dataDir):
            os.makedirs(dataDir) # 创建文件夹
        # 保存数据
        with open(UserData.appDataFileName, 'w', encoding='utf-8') as jsonFile:
            json.dump(UserData.appDocker, jsonFile, indent=4)
        with open(UserData.settingsDataFileName, 'w', encoding='utf-8') as jsonFile:
            json.dump(UserData.settingsData, jsonFile, indent=4)
  
    # 更新数据
    @ staticmethod
    def updateAppDockerPath(row: int, col: int, path: str):
        if row in UserData.appDocker and col in UserData.appDocker[row]:
            UserData.appDocker[row][col]['path'] = path

    # 显示数据
    @ staticmethod
    def displayData():
        for row in UserData.appDocker:
            for col in UserData.appDocker[row]:
                if UserData.appDocker[row][col]['path'] != 'none':
                    print(f"{row}:{col}: {UserData.appDocker[row][col]}")
        print(f"{UserData.settingsData}")
        print(f"================")

# 定义一个 Enum 来表示不同的主题
class StyleSheetData():
    lightTheme = None
    darkTheme = None
    macaronTheme = None
    themeMap ={}

    fontMap = {
        '微软雅黑': QFont("微软雅黑"),
        '宋体': QFont("宋体"),
        '楷体': QFont("楷体"),
        '黑体': QFont("黑体"),
        '幼圆': QFont("幼圆"),
        }
    themeMap2CN = {
        'light': '浅色模式',
        'dark': '深色模式',
        'macaron': '马卡龙',
        }
    themeMap2EN = {
        '浅色模式': 'light',
        '深色模式': 'dark',
        '马卡龙': 'macaron',
        }

    @ staticmethod
    def getThemeNameCN(englishTheme):
        return StyleSheetData.themeMap2CN.get(englishTheme)

    @ staticmethod
    def getThemeNameEN(chineseTheme):
        return StyleSheetData.themeMap2EN.get(chineseTheme)


    @ staticmethod
    def loadStyleSheetData(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()

    
    @ staticmethod
    def initialize():
        StyleSheetData.lightTheme = StyleSheetData.loadStyleSheetData("theme\\lightTheme.qss")
        StyleSheetData.darkTheme = StyleSheetData.loadStyleSheetData("theme\\darkTheme.qss")
        StyleSheetData.macaronTheme = StyleSheetData.loadStyleSheetData("theme\\MacaronTheme.qss")
        StyleSheetData.themeMap = {
            'light':StyleSheetData.lightTheme,
            'dark': StyleSheetData.darkTheme,
            'macaron':StyleSheetData.macaronTheme,
            }