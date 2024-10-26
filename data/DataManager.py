import os, json

class UserData():
    def __init__(self,size:tuple[int,int]):
        self.dataFileName = './data/app_data.json'
        self.appDocker = {
            row: {col: {'path': 'none'} for col in range(0,size[1])}
            for row in range(0,size[0])
            }

    # 加载数据
    def loadUserData(self): 
        if not os.path.exists(self.dataFileName):
            # 创建文件（不写入任何内容）
            with open(self.dataFileName, 'w', encoding='utf-8') as jsonFile:
                json.dump(self.appDocker, jsonFile, indent=4)
                pass
        else:
            # 读取文件并加载数据
            with open(self.dataFileName, 'r', encoding='utf-8') as jsonFile:
                datas = json.load(jsonFile)
                for row, col_data in datas.items():
                    row = int(row)
                    self.appDocker[row] = {}
                    for col, value in col_data.items():
                        col = int(col)
                        self.appDocker[row][col] = value
        self.displayData()

    
    # 保存数据
    def saveUserData(self):
        if not os.path.exists(self.dataFileName):
            # 创建文件（不写入任何内容）
            with open(self.dataFileName, 'w', encoding='utf-8') as jsonFile:
                json.dump(self.appDocker, jsonFile, indent=4)
        else:
            with open(self.dataFileName, 'w', encoding='utf-8') as jsonFile:
                json.dump(self.appDocker, jsonFile, indent=4)
  
    # 更新数据
    def updateAppDockerPath(self, row: int, col: int, path: str):
        if row in self.appDocker and col in self.appDocker[row]:
            self.appDocker[row][col]['path'] = path

    # 显示数据
    def displayData(self):
        for row in self.appDocker:
            for col in self.appDocker[row]:
                if self.appDocker[row][col]['path'] != 'none':
                    print(f"{row}:{col}: {self.appDocker[row][col]}")
        print(f"================")


class StyleSheetData():
    def __init__(self):
        pass

    @ staticmethod
    def loadStyleSheetData(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
        