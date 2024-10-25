import os, json

class AppData:
    def __init__(self):
        self.dataFileName = './data/app_data.json'
        self.appDocker = {
            row: {col: {'name': 'none', 'path': 'none', 'app': None} 
                   for col in range(1, 12)}
            for row in range(1, 7)
        }
        self.count = self.getCount()
        self.appDocker.values()
        

    # 加载数据
    def loadAppData(self):
        if os.path.exists(self.dataFileName):
            with open(self.dataFileName, 'r', encoding='utf-8') as file:
                dataInLoad = json.load(file)
                for row, col_data in dataInLoad.items():
                    row = int(row)
                    self.appDocker[row] = {}
                    for col, value in col_data.items():
                        # 添加空的 'app'
                        col = int(col)
                        self.appDocker[row][col] = {**value, 'app': None}
            #     self.appDocker = {
            #     int(row): {int(col): value for col, value in cols.items()}
            #     for row, cols in self.appDocker.items()
            # }
        else:
            with open(self.dataFileName, 'w'):
                pass
    
    
    # 保存数据
    def saveAppData(self):
        if not os.path.exists(self.dataFileName):
            with open(self.dataFileName, 'w') as jsonFile:
                jsonFile.write('{}')  # 创建一个空的 JSON 对象
        dataToSave = {
            row: {col: {'name': value['name'], 'path': value['path']}
                for col, value in col_data.items()}
            for row, col_data in self.appDocker.items()
        }
        with open(self.dataFileName, 'w') as jsonFile:
            json.dump(dataToSave, jsonFile, indent=4)

    # 更新某个元素的内容
    def updateElement(self, row: int, col: int, name, path, app):
        if row in self.appDocker and col in self.appDocker[row]:
            self.appDocker[row][col] = {'name': name, 'path': path, 'app': app}
            self.count += 1

        
    # 添加元素值，其他元素值不变
    def updateElementValue(self, row: int, col: int, itemName, value):
        if row in self.appDocker and col in self.appDocker[row]:
            self.appDocker[row][col][itemName] = value


    # 根据int索引删除元素
    def removeElement(self, row: int, col: int):
        if row in self.appDocker and col in self.appDocker[row]:
            del self.appDocker[row][col]
            self.autoSortAndAddEmpty(row , col)
            self.count -= 1

    # 根据tuple索引删除元素
    def removeElementInTuple(self, index: tuple[int,int]):
        row = index[0]
        col = index[1]
        self.removeElement(row, col)

    # 获取第一个空元素的位置
    def getFisrtEmpty(self):
        for row in self.appDocker:
            for col in self.appDocker[row]:
                if self.appDocker[row][col]['name'] == 'none':
                    return row, col
        return None, None
    
    # 计算非空元素数量
    def getCount(self)-> int:
        count = 0
        for row in self.appDocker:
            for col in self.appDocker[row]:
                if self.appDocker[row][col]['name'] != 'none':
                    count += 1
        return count
    
    # 获取所有非空元素
    def getNonEmptyElements(self)-> dict:
        allNonEmptyElements = {}
        for row in self.appDocker:
            nonEmptyElements = {col: item for col, item in self.appDocker[row].items() if item['name'] != 'none'}
            if not nonEmptyElements:
                break
            allNonEmptyElements.update(nonEmptyElements)
        return allNonEmptyElements
        
    # 根据索引获取元素
    def getElement(self, row: int, col: int):
        if row in self.appDocker and col in self.appDocker[row]:
            return self.appDocker[row][col]
        else:
            return

    # 自动排序
    def autoSortAndAddEmpty(self, row: int, col: int):
        newRowDocker = {}
        for k, v in self.appDocker[row].items():
            if k >= col:
                newRowDocker[k - 1] = v  # 大于或等于col的键减一
            else:
                newRowDocker[k] = v  # 小于col的键保持不变
        self.appDocker[row] = newRowDocker # 替换当前行
        for i in self.appDocker[row]:
            print(f'{i}:{self.appDocker[row][i]['name']}')
        print('------------------')
        # 获取最后一个非空元素的位置
        point = self.whatsRowHaveNoneElement(row)
        print(point)
        if point[0] == row :
            # 在末尾添加空元素
            newRowDocker[max(newRowDocker.keys()) + 1] = {'name': 'none', 'path': 'none', 'app': None}
            self.appDocker[row] = newRowDocker # 更新当前行
            for i in self.appDocker[row]:
                print(f'{i}:{self.appDocker[row][i]['name']}')
            print('------------------')
        elif point[0] - row == 1 :
            element = self.translateElementsLeft(row + 1, 1)
            element[0 + max(newRowDocker.keys()) + 1] = element[1]
            self.appDocker[row].update(element)
            for i in self.appDocker[row]:
                print(f'{i}:{self.appDocker[row][i]['name']}')
            print('------------------')
        else:
            # 如果最后一个非空元素的位置不在当前行，则将元素依次前移
            for i in range(row + 1, point[0]):
                element = self.translateElementsLeft(i, 1)
                for k, v in element.items():
                    element[k + max(newRowDocker.keys()) + 1] = v
                self.appDocker[i-1].update(element)
        self.updateIndex()
        self.displayDataAccordingToProperty('app')


    # 判断某一行是否全为空
    def thisRowIsNoneCompletely(self, row: int)-> bool:
        for col in self.appDocker[row]:
            if self.appDocker[row][col]['name'] != 'none':
                return False
        return True

    # 从指定行开始，获取最后一个非空元素的位置
    def whatsRowHaveNoneElement(self, rowStart: int):
        for row in range(rowStart, len(self.appDocker)+1):
            isNone = False
            colEnd = 0
            for col in self.appDocker[row]:
                if self.appDocker[row][col]['name'] != 'none':
                    colEnd = col
                else:
                    isNone = True
                    break
            if isNone:
                return row, colEnd   
        return False
    
    # 将元素移动到上一个位置
    def pasteToLast(self, row: int, col: int):
        # 判断上一个位置是否存在
        if col > 1:
            # 将当前元素移动到上一个位置
            self.appDocker[row][col - 1] = self.appDocker[row][col] 
        else:
            # 如果当前元素是第一个元素，则移到上一行的最后一个位置
            self.appDocker[row - 1][max(self.appDocker[row - 1].keys()) + 1] = self.appDocker[row][col]
            pass

    # 向左平移某行元素，并返回多余的元素集合
    def translateElementsLeft(self, row: int, step: int):
        newRowDocker = {}
        backElements = {}
        for k, v in self.appDocker[row].items():
            if k - step < 1:
                backElements[k] = v
            else:
                newRowDocker[k-step] = v
        for k in range(step):
            newRowDocker[max(newRowDocker.keys()) + 1] = {'name': 'none', 'path': 'none', 'app': None}
        self.appDocker[row] = newRowDocker # 更新当前行
        print(backElements)
        print('===============')
        return backElements

    # 更新索引
    def updateIndex(self):
        for row in self.appDocker:
            for col in self.appDocker[row]:
                if self.appDocker[row][col]['app'] is None:
                    break
                self.appDocker[row][col]['app'].index = (row, col)

    # 显示数据
    def displayData(self):
        for row in self.appDocker:
            for col in self.appDocker[row]:
                print(f"{row}:{col}: {self.appDocker[row][col]}")
    
    # 根据传入的属性显示数据
    def displayDataAccordingToProperty(self, name):
        
        for row in self.appDocker:
            for col in self.appDocker[row]:
                if self.appDocker[row][col]['name'] == 'none':
                    break
                print(f"{row}:{col}: {self.appDocker[row][col][name].index}")



class StyleSheetData():
    def __init__(self):
        pass

    @ staticmethod
    def loadStyleSheetData(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
        