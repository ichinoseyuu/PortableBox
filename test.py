class AppDockerManager:
    def __init__(self, appDocker):
        self.appDocker = appDocker

    # 自动排序并添加空元素
    def autoSortAndAddEmpty(self, row: int, col: int):
        newColDocker = {}
        
        # 遍历当前行，进行元素前移
        for k, v in self.appDocker[row].items():
            if k > col:
                newColDocker[k - 1] = v  # 如果索引大于col，索引减一
            else:
                newColDocker[k] = v  # 小于或等于col的索引保持不变

        # 获取最后一个非空元素的位置
        rowEnd, colEnd = self.whatsRowHaveNoneElement(row)
        if rowEnd == row:
            # 如果最后一个非空元素在当前行，则直接在新行末尾添加空元素
            emptyIndex = max(newColDocker.keys(), default=-1) + 1
            newColDocker[emptyIndex] = {'name': 'none', 'path': 'none', 'app': None}
        else:
            # 如果最后一个非空元素在下方行，则在该行末尾添加空元素
            emptyIndex = max(self.appDocker[rowEnd].keys(), default=-1) + 1
            self.appDocker[rowEnd][emptyIndex] = {'name': 'none', 'path': 'none', 'app': None}

        # 更新当前行
        self.appDocker[row] = newColDocker
        self.updateIndex()

    # 获取从指定行开始的最后一个包含非空元素的位置
    def whatsRowHaveNoneElement(self, rowStart: int):
        for row in range(rowStart, len(self.appDocker)):
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

    # 更新索引的占位符函数
    def updateIndex(self):
        pass  # 实现更新索引的逻辑（如有必要）

# 初始化 appDocker
appDocker = {
    0: {0: {'name': 'app1'}, 1: {'name': 'app2'}, 2: {'name': 'app3'}},
    1: {0: {'name': 'app4'}, 1: {'name': 'app5'}, 2: {'name': 'app6'}},
    2: {0: {'name': 'app7'}, 1: {'name': 'app8'}, 2: {'name': 'none'}},
    3: {0: {'name': 'none'}, 1: {'name': 'none'}, 2: {'name': 'none'}},
}

manager = AppDockerManager(appDocker)

# 删除位于 [1, 1] 的元素
del appDocker[1][1]  # 删除 app5

# 调用自动排序和添加空元素的方法
manager.autoSortAndAddEmpty(1, 1)

# 打印最终的 appDocker 状态
print(appDocker)
