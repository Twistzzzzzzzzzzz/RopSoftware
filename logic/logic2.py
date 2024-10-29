import os
import json
import cv2
import torch
from model import App_model
from PyQt5.QtGui import QPixmap
from model.Pre_processing import clahe_apply


def register_user(user_name, user_password, user_info_path):
        # 注册用户
        os.makedirs(user_info_path)
        user_info = {
            "user_name": user_name,
            "user_password": user_password
        }
        with open(os.path.join(user_info_path, 'user_info.json'), 'w') as f:
            json.dump(user_info, f)