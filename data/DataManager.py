from enum import Enum
import os, json
from PySide6.QtCore import QFile, QTextStream

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
        }

    # 加载数据
    @ staticmethod
    def loadUserData():    
        if not os.path.exists(UserData.appDataFileName):
            with open(UserData.appDataFileName, 'w', encoding='utf-8') as jsonFile:
                json.dump(UserData.appDocker, jsonFile, indent=4)
        if not os.path.exists(UserData.settingsDataFileName):
            with open(UserData.settingsDataFileName, 'w', encoding='utf-8') as jsonFile:
                json.dump(UserData.settingsData, jsonFile, indent=4)    
        # 读取文件并加载数据
        with open(UserData.appDataFileName, 'r', encoding='utf-8') as jsonFile:
            datas = json.load(jsonFile)
            for row, col_data in datas.items():
                row = int(row)
                UserData.appDocker[row] = {}
                for col, value in col_data.items():
                    col = int(col)
                    UserData.appDocker[row][col] = value
        with open(UserData.settingsDataFileName, 'r', encoding='utf-8') as jsonFile:
            UserData.settingsData = json.load(jsonFile)
        UserData.displayData()

    
    # 保存数据
    @ staticmethod
    def saveUserData():
        if not os.path.exists(UserData.appDataFileName):
            # 创建文件（不写入任何内容）
            with open(UserData.appDataFileName, 'w', encoding='utf-8') as jsonFile:
                json.dump(UserData.appDocker, jsonFile, indent=4)
        if not os.path.exists(UserData.settingsDataFileName):
            with open(UserData.settingsDataFileName, 'w', encoding='utf-8') as jsonFile:
                json.dump(UserData.settingsData, jsonFile, indent=4)
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
        print(f"================")

# 定义一个 Enum 来表示不同的主题
class StyleSheetData():
    lightTheme = None
    darkTheme = None
    macaronTheme = None
    themeStyle ={}

    @ staticmethod
    def loadStyleSheetData(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()

    
    @ staticmethod
    def initialize():
        StyleSheetData.lightTheme = StyleSheetData.loadStyleSheetData("theme\\lightTheme.qss")
        StyleSheetData.darkTheme = StyleSheetData.loadStyleSheetData("theme\\darkTheme.qss")
        StyleSheetData.macaronTheme = StyleSheetData.loadStyleSheetData("theme\\MacaronTheme.qss")
        StyleSheetData.themeStyle = {
            "light": StyleSheetData.lightTheme,
            "dark": StyleSheetData.darkTheme,
            "macaron": StyleSheetData.macaronTheme
            }