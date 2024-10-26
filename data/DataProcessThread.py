from PySide6.QtCore import QThread, Signal, QDir


class FolderSizeThread(QThread):
    sizeCalculated = Signal(float)

    def __init__(self):
        super().__init__()

    def start(self, folderPath):
        self.folderPath = folderPath  # 保存路径
        super().start()  # 调用基类的 start 方法

    def run(self):
        totalSize = self.getFolderSize(self.folderPath)  # 使用保存的路径
        self.sizeCalculated.emit(totalSize)

    def getFolderSize(self, folderPath):
        dir = QDir(folderPath)
        totalSize = 0
        for fileInfo in dir.entryInfoList(QDir.AllEntries | QDir.NoDotAndDotDot):
            if fileInfo.isFile():
                totalSize += fileInfo.size()
            elif fileInfo.isDir():
                totalSize += self.getFolderSize(fileInfo.absoluteFilePath())
        return totalSize