import sys,os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtGui
import mainUi
import requests
import re

class MainCode(QMainWindow, mainUi.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        mainUi.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.chose_btn.clicked.connect(self.on_open)
        self.pushButton.clicked.connect(self.remove_bg)
        self.save_btn.clicked.connect(self.on_save)
        self.url_text.returnPressed.connect(self.urlPath)
        self.state = 0
    def urlPath(self):
        # 使用正则判断是否是网址
        if(re.search('[a-zA-z]+://[^\s]*',self.url_text.text()) != None):
            self.tips.setText('')
            self.state =2
            # 显示图片
            self.remove_bg(url = self.url_text.text())

        else:
            self.tips.setText('网址错误')


    def on_save(self):
        SaveFileName = QFileDialog.getSaveFileName(self, '文件另存为', r'./', 'PNG (*.png);;JPG (*.jpg);;JPEG (*.jpeg)')
        print(SaveFileName)
        with open(str(SaveFileName[0]), 'wb') as f:
            f.write(self.result)
        if (os.path.exists(str(SaveFileName[0]))):
            os.remove('./temp_no-bg.png')

    def remove_bg(self,url=None):
        API = '2vVEzqj34ekxY4yydSa85ySj'

        # 网络图片
        if(self.state == 2):
            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                data={
                    'image_url': url,
                    'size': 'auto'
                },
                headers={'X-Api-Key': API},
            )
        elif(self.state == 1):
            # 准备抠图-本地文件版
            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                files={'image_file': open(self.imgPath, 'rb')},
                data={'size': 'auto'},
                headers={'X-Api-Key': API},
            )

        if response.status_code == requests.codes.ok:
            with open('./temp_no-bg.png', 'wb') as out:
                out.write(response.content)
            self.result = response.content
            self.img_show2.setPixmap(QtGui.QPixmap('./temp_no-bg.png'))
            self.img_show2.setScaledContents(True)
        else:
            if(response.status_code == '200'):
                self.tips.setText('抠图成功！')
            elif(response.status_code == '400'):
                self.tips.setText('错误：无效参数或输入文件无法处理')
            elif(response.status_code == '402'):
                self.tips.setText('错误：API积分不足（不收取任何积分）')
            elif (response.status_code == '409'):
                self.tips.setText('错误：频率超过上限')
            print("Error:", response.status_code, response.text)
        # photo = ImageTk.PhotoImage(img.resize((400,400)))
        # self.img_path.count() #获取QcomboBox的Item条数

    def on_open(self):
        FullFileName= QFileDialog.getOpenFileName(self, '打开', r'./', 'JPG (*.jpg);;PNG (*.png);;JPEG (*.jpeg)')
        # FullFileName = " ".join(FullFileName[0])
        ChoseImage = str(FullFileName[0])
        self.imgPath = ChoseImage
        # 插入路径到combobox上
        if(len(ChoseImage) != 0):
            self.state = 1
            self.img_path.insertItem(0, ChoseImage)
            # 显示图像
            self.img_show.setPixmap(QtGui.QPixmap(ChoseImage))
            self.img_show.setScaledContents(True)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    md = MainCode()
    md.show()
    sys.exit(app.exec_())