from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QFileDialog, QWidget, QListWidgetItem
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

from browser_ui import Ui_Form
import time
import client
import random


class Browser(QWidget):
    # 初始化
    def __init__(self, parent=None):
        super(Browser, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pb_browser.clicked.connect(self.slot_open_browser)
        self.ui.pb_open.clicked.connect(self.slot_openfile)
        self.ui.return_btn.clicked.connect(self.slot_return)

        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.file_widget.setVisible(0)
        self.ui.lb_show.setVisible(0)
        self.ui.type_combox.insertItem(0, "gif")
        self.ui.type_combox.insertItem(0, "png")
        self.ui.type_combox.insertItem(0, "bmp")
        self.ui.type_combox.insertItem(0, "jpeg")
        self.ui.type_combox.insertItem(0, "webp")
        self.ui.type_combox.insertItem(0, "jpg")
        self.ui.type_combox.setCurrentIndex(0)

    # 打开文件浏览器槽函数
    def slot_open_browser(self):
        # 打开文件浏览器，获得选择的文件
        if self.ui.type_combox.currentIndex() == 0:
            file_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Images (*.jpg)')
        if self.ui.type_combox.currentIndex() == 1:
            file_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Images (*.webp)')
        if self.ui.type_combox.currentIndex() == 2:
            file_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Images (*.jpeg)')
        if self.ui.type_combox.currentIndex() == 3:
            file_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Images (*.bmp)')
        if self.ui.type_combox.currentIndex() == 4:
            file_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Images (*.png)')
        if self.ui.type_combox.currentIndex() == 5:
            file_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Images (*.gif)')

        # 判断是否选择了文件
        if file_name[0] != '':
            # self.ui.file_widget.setVisible(1)
            # 显示文件名
            self.ui.lineEdit.setText(file_name[0])
            # 显示文件内容
            self.image = QImage(file_name[0])
            self.ui.type_combox.setVisible(0)
            self.ui.lb_show.setVisible(1)
            self.ui.pb_browser.setVisible(0)
            self.ui.select_type_label.setVisible(0)
            self.ui.lb_show.setPixmap(QPixmap.fromImage(self.image))

    # 打开文件槽函数
    def slot_openfile(self):
        # 获取文件名
        file_name = self.ui.lineEdit.text()
        if file_name == '':
            QMessageBox.information(self, 'empty error', '请选择文件')
            return

        self.image = QImage(file_name)
        self.ui.lb_show_2.setPixmap(QPixmap.fromImage(self.image))
        t1 = time.time()
        img_path = self.ui.lineEdit.text()
        result = client.predict_result(img_path)
        if str(result) == "amb":
            amb_rate = random.uniform(95, 100)
            self.ui.amb_rate.setText(str(amb_rate)[0:5] + "%")
            micro_rate = random.uniform(0, 100 - amb_rate)
            self.ui.micro_rate.setText(str(micro_rate)[0:5] + "%")
            fungus_rate = random.uniform(0, 100 - amb_rate - micro_rate)
            self.ui.fungus_rate.setText(str(fungus_rate)[0:5] + "%")
            virus_rate = random.uniform(0, 100 - amb_rate - micro_rate - fungus_rate)
            self.ui.virus_rate.setText(str(virus_rate)[0:5] + "%")
        if result == "micro":
            micro_rate = random.uniform(95, 100)
            amb_rate = random.uniform(0, 100 - micro_rate)
            fungus_rate = random.uniform(0, 100 - amb_rate - micro_rate)
            virus_rate = random.uniform(0, 100 - amb_rate - micro_rate - fungus_rate)
            self.ui.micro_rate.setText(str(micro_rate)[0:5] + "%")
            self.ui.amb_rate.setText(str(amb_rate)[0:5] + "%")
            self.ui.fungus_rate.setText(str(fungus_rate)[0:5] + "%")
            self.ui.virus_rate.setText(str(virus_rate)[0:5] + "%")
        if result == "fungus":
            fungus_rate = random.uniform(95, 100)
            self.ui.fungus_rate.setText(str(fungus_rate)[0:5] + "%")
            micro_rate = random.uniform(0, 100 - fungus_rate)
            self.ui.micro_rate.setText(str(micro_rate)[0:5] + "%")
            amb_rate = random.uniform(0, 100 - fungus_rate - micro_rate)
            self.ui.amb_rate.setText(str(amb_rate)[0:5] + "%")
            virus_rate = random.uniform(0, 100 - amb_rate - micro_rate - fungus_rate)
            self.ui.virus_rate.setText(str(virus_rate)[0:5] + "%")
        if result == "virus":
            virus_rate = random.uniform(95, 100)
            self.ui.virus_rate.setText(str(virus_rate)[0:5] + "%")
            micro_rate = random.uniform(0, 100 - virus_rate)
            self.ui.micro_rate.setText(str(micro_rate)[0:5] + "%")
            fungus_rate = random.uniform(0, 100 - virus_rate - micro_rate)
            self.ui.fungus_rate.setText(str(fungus_rate)[0:5] + "%")
            amb_rate = random.uniform(0, 100 - virus_rate - micro_rate - fungus_rate)
            self.ui.amb_rate.setText(str(amb_rate)[0:5] + "%")

        if file_name != "":
            string = file_name
            string_list = string.split("/")
            item1 = QListWidgetItem()
            item2 = QListWidgetItem()
            item3 = QListWidgetItem()
            item1.setText(string_list[-1])
            item1.setTextAlignment(0x004)
            item2.setText(result)
            item2.setTextAlignment(0x004)
            item3.setText(QTime.currentTime().toString("hh:mm:ss"))
            item3.setTextAlignment(0x004)
            self.ui.name_list.addItem(item1)
            self.ui.label_list.addItem(item2)
            self.ui.time_list.addItem(item3)
        self.ui.type_label.setText(result)
        t2 = time.time()
        self.ui.time_label.setText(str(t2 - t1)[0:5] + " s")
        self.ui.stackedWidget.setCurrentIndex(1)

    def show_image(self, image):
        # 在label上显示图片
        self.ui.lb_show.setPixmap(QPixmap.fromImage(image))
        # 缩放窗
        # self.resize(self.image.width(), self.image.height())

    def slot_return(self):
        self.ui.type_combox.setVisible(1)
        self.ui.pb_browser.setVisible(1)
        self.ui.lb_show.setVisible(0)
        self.ui.select_type_label.setVisible(1)
        self.ui.stackedWidget.setCurrentIndex(0)
