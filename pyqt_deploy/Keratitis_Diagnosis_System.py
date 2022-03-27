import sys
from PyQt5.QtWidgets import QApplication
from MainWidget import Browser
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)
my_window = Browser()
my_window.setWindowIcon(QIcon('logo2.png'))  # 路径错误找不到问题所在
my_window.show()
sys.exit(app.exec_())
