import os
import time
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtGui import QPixmap
from ui.ui_form import Ui_Form  # 引入由 pyuic5 生成的 UI 文件
from logic import logic  # 引入后端逻辑

class MainWindow(Ui_Form):
    def __init__(self, form):
        super().setupUi(form)
        # 连接上传按钮的点击事件
        self.pushButton_upload_image.clicked.connect(self.upload_image)
        self.pushButton_upload_info.clicked.connect(self.upload_info)
        self.pushButton_predict.clicked.connect(self.run_rop_diagnosis)  # 连接判断按钮的点击事件

        # 加载模型
        self.model = logic.load_model()  # 加载模型

        # 初始化保存处理后的图片路径的变量
        self.processed_image_path = None

    def upload_image(self):
        """
        上传图片并调用逻辑保存图片，完成预处理但不立即判断
        """
        # 获取用户输入的姓名
        user_name = self.lineEdit_name.text()  # 获取"姓名"的输入值

        if not user_name:
            print("请先输入姓名！")
            return

        # 打开文件选择对话框
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(None, "选择图片", "",
                                                   "Images (*.png *.jpg *.bmp *.gif);;All Files (*)", options=options)

        if file_path:
            # 在界面上显示原始图片
            pixmap = QPixmap(file_path)
            self.label_upload_image.setPixmap(pixmap)

            # 调用后端逻辑保存图片，并传递用户名
            save_path = logic.save_image(file_path, user_name)

            if save_path:
                print(f"图片已保存到: {save_path}")

                # 检查文件是否已保存完成（确保文件已经存在于磁盘上）
                max_retries = 10  # 尝试检查文件的最大次数
                retry_interval = 0.5  # 每次重试的间隔时间（秒）

                for _ in range(max_retries):
                    if os.path.exists(save_path):
                        # 一旦文件存在，处理图像
                        self.processed_image_path = logic.process_and_save_image(save_path, user_name)
                        if self.processed_image_path:
                            # 检查处理后的图片是否已经保存
                            for _ in range(max_retries):
                                if os.path.exists(self.processed_image_path):
                                    # 加载并在界面上显示处理后的图片
                                    processed_pixmap = QPixmap(self.processed_image_path)
                                    self.label_processed_image.setPixmap(processed_pixmap)
                                    print(f"处理后的图片已保存并显示: {self.processed_image_path}")
                                    break
                                else:
                                    time.sleep(retry_interval)
                            else:
                                print(f"在 {max_retries * retry_interval} 秒后，仍未能确认处理后的图片保存。")
                        else:
                            print("图像处理失败")
                        break
                    else:
                        # 文件尚未保存完成，等待然后重试
                        time.sleep(retry_interval)
                else:
                    print(f"在 {max_retries * retry_interval} 秒后，仍未能确认图片保存。")
            else:
                print("保存图片失败")

    def run_rop_diagnosis(self):
        """
        等待用户按下判断按钮后执行ROP预测并显示结果
        """
        if not self.processed_image_path or not os.path.exists(self.processed_image_path):
            print("请先上传并预处理有效的图片")
            return

        # 运行ROP预测
        diagnosis, confidence = logic.run_rop_prediction(self.processed_image_path, self.model)

        if diagnosis is not None:
            # 在界面上显示预测结果
            self.label_prediction_result.setText(f"诊断结果: {diagnosis} (置信度: {confidence:.2f})")
        else:
            self.label_prediction_result.setText("预测失败，请检查输入")
        print("诊断结束")

    def upload_info(self):
        """
        上传用户信息，并进行相关处理
        """
        # 获取用户输入的信息
        user_name = self.lineEdit_name.text()
        gender = self.comboBox_gender.currentText()
        age = self.lineEdit_age.text()
        location = self.lineEdit_location.text()
        diagnosis_date = self.dateEdit_diagnosis.text()

        # 检查所有必填项是否已填
        if not user_name or not age or not location:
            print("请填写完整的个人信息")
            return

        # 打印信息到控制台（或调用后端逻辑保存信息）
        print(f"姓名: {user_name}, 性别: {gender}, 年龄: {age}, 诊断地点: {location}, 诊断时间: {diagnosis_date}")

        # 这里可以将信息保存到本地文件或数据库
        logic.save_user_info(user_name, gender, age, location, diagnosis_date)

        print("用户信息上传成功！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QtWidgets.QWidget()
    window = MainWindow(form)
    form.show()
    sys.exit(app.exec_())
