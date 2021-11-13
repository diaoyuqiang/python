from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QMessageBox


# 统计薪资的类
class Statics(object):
    def __init__(self):
        self.window = QMainWindow()  # 主窗口对象
        self.window.resize(600, 500)  # 指定窗口大小
        self.window.move(900, 200)  # 偏移量(x, y)
        self.window.setWindowTitle('薪资统计')  # 窗口标题

        self.textEdit = QPlainTextEdit(self.window)  # 在主窗口创建纯文本对象
        self.textEdit.setPlaceholderText("请输入薪资表")  # 占位文本
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('统计', self.window)  # 统计按钮
        self.button.move(380, 80)
        self.button.clicked.connect(self.button_click)  # 点击事件的signal交给button_click函数(slot)处理

    # 统计薪资2000以上及以下的员工名单
    def button_click(self):
        text = self.textEdit.toPlainText()  # 获取文本编辑框的内容

        upper_20 = ''
        lower_20 = ''

        for line in text.splitlines():  # 返回各行作为元素的列表
            parts = line.split()  # 以空格分隔
            # print(parts)
            name, salary, age = parts
            if int(salary) > 20000:
                upper_20 += name + '; '
            else:
                lower_20 += name + '; '

        QMessageBox.about(self.window, '统计薪资', f'2w以上的名单: {upper_20}\n2w以下的名单: {lower_20}')  # 在主窗加载消息提示框


app = QApplication([])  # QApplication图形界面程序的底层管理
win = Statics()
win.window.show()  # 主窗口控件, show()方法
app.exec_()  # 事件循环处理