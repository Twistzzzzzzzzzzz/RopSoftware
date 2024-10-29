import json
import os
import time
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from logic import logic2  # 引入后端逻辑

class RopClientLogin:

    def __init__(self):
        # 从文件中加载UI定义
        # 注意：里面的控件对象也成为窗口对象的属性了
        self.ui = uic.loadUi("ui/login_page.ui") # 窗口对象

        # self.model = logic.load_model()  # 加载模型

        # 初始化保存处理后的图片路径的变量
        self.processed_image_path = None

        self.ui.pushButton_clearContent.clicked.connect(self.clear_content) # 清除密码输入框
        self.ui.pushButton_login.clicked.connect(self.login_register) # 登录按钮

        self.main_page = None

    def clear_content(self):
        self.ui.lineEdit_password.clear()

    def go_to_main_page(self, user_name, user_password, user_info_path):
        self.ui.hide()
        main_page = RopClientMain(user_name, user_password, user_info_path)  # 保存实例
        main_page.ui.show()


    def login_register(self):
        user_name = self.ui.lineEdit_username.text()
        user_password = self.ui.lineEdit_password.text()

        # 检查用户名和密码是否为空
        if not user_name:
            self.ui.lineEdit_username.setFocus()
            return
        if not user_password:
            self.ui.lineEdit_password.setFocus()
            return

        # 检查用户名是否已经存在, 若不存在，则在UserInfo文件夹中新建一个名为用户名的文件夹，
        # 并在其中新建一个json文件，存储用户名和密码
        user_info_path = os.path.join('Resource/UserInfo', user_name)
        if not os.path.exists(user_info_path):
            logic2.register_user(user_name, user_password, user_info_path)
            QMessageBox.information(self.ui, "提示", "注册成功！")
            self.go_to_main_page(user_name, user_password, user_info_path)  # 切换页面
        else:
            # 若用户存在，则检查密码是否正确
            with open(os.path.join(user_info_path, 'user_info.json'), 'r') as f:
                user_info = json.load(f)
                if user_info['user_password'] == user_password:
                    QMessageBox.information(self.ui, "提示", "登录成功！")

                    self.go_to_main_page(user_name, user_password, user_info_path) # 切换页面

                else:
                    QMessageBox.information(self.ui, "提示", "密码错误！")
                    self.ui.lineEdit_password.clear()
                    self.ui.lineEdit_password.setFocus()
                    return

class RopClientMain:

    def __init__(self, user_name, user_password, user_info_path):

        self.ui = uic.loadUi("ui/profile_page.ui")

        self.user_name = user_name
        self.user_password = user_password
        self.user_info_path = user_info_path

class RopProfilePage:

    def __init__(self):
        self.ui = uic.loadUi("ui/profile_page.ui")

        self.ui.pushButton_cancel.clicked.connect(self.go_back)
        self.ui.pushButton_submit.clicked.connect(self.submit)
        self.ui.pushButton_avatar.clicked.connect(self.change_avatar)
        self.ui.pushButton_check_username.clicked.connect(self.check_username)



    def go_back(self):
        pass

    def submit(self):
        pass

    def change_avatar(self):
        pass

    def check_username(self):
        pass














app = QApplication([])
first_page = RopClientLogin()
first_page.ui.show()
app.exec_()