from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

# 假设 OverQLabel 是 QLabel 的子类
class OverQLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)

def get_over_labels(layout):
    return [layout.itemAt(i).widget() for i in range(layout.count())]

app = QApplication([])

# 创建主窗口和布局
window = QWidget()
layout = QVBoxLayout()

# 添加一些 OverQLabel
layout.addWidget(OverQLabel("标签 1"))
layout.addWidget(OverQLabel("标签 2"))

# 将布局设置到窗口
window.setLayout(layout)

# 获取所有 OverQLabel
over_labels = get_over_labels(layout)

# 打印获取到的 OverQLabel
for label in over_labels:
    print(label.text())

window.show()
app.exec()
