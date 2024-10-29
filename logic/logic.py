import os
import json
import cv2
import torch
from model import App_model
from PyQt5.QtGui import QPixmap
from model.Pre_processing import clahe_apply


def save_image(file_path, user_name):
    """
    负责根据用户名保存图片到指定目录
    :param file_path: 上传的图片路径
    :param user_name: 用户名，用于创建对应文件夹
    """
    if file_path and user_name:
        # 指定保存目录，根据用户名创建子目录
        save_directory = os.path.join('Resource/UploadedImages', user_name)

        # 如果目录不存在，创建目录
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        # 获取文件名并保存图片到指定目录
        file_name = os.path.basename(file_path)
        save_path = os.path.join(save_directory, file_name)
        pixmap = QPixmap(file_path)
        pixmap.save(save_path)
        return save_path
    return None


def process_and_save_image(image_path, user_name):
    """
    处理指定路径的图像，并将处理后的图像保存到指定用户文件夹中
    :param image_path: 输入图像的路径
    :param user_name: 用户名，用于创建存储处理后图像的文件夹
    :return: 处理后的图像保存路径
    """
    # 检查输入图像是否存在
    if not os.path.exists(image_path):
        print(f"图像文件 {image_path} 不存在")
        return None

    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        print(f"无法加载图像: {image_path}")
        return None

    # 预处理图像
    try:
        processed_image = clahe_apply.pre_processing(image)
    except Exception as e:
        print(f"图像预处理失败: {str(e)}")
        return None

    # 创建用户文件夹路径
    save_directory = os.path.join('Resource/Processed_images', user_name)

    # 确保输出文件夹存在
    if not os.path.exists(save_directory):
        try:
            os.makedirs(save_directory)
        except OSError as e:
            print(f"创建文件夹失败: {str(e)}")
            return None

    # 保存处理后的图像
    output_path = os.path.join(save_directory, 'processed_image.jpg')
    try:
        cv2.imwrite(output_path, processed_image)
        print(f"处理后的图像已保存到: {output_path}")
    except Exception as e:
        print(f"保存图像失败: {str(e)}")
        return None

    return output_path


def save_user_info(user_name, gender, age, location, diagnosis_date):
    """
    保存用户信息到本地 JSON 文件
    """
    # 定义用户信息字典
    user_info = {
        "姓名": user_name,
        "性别": gender,
        "年龄": age,
        "诊断地点": location,
        "诊断时间": diagnosis_date
    }

    # 创建一个存储用户信息的文件夹
    info_directory = 'Resource/UserInfo'
    if not os.path.exists(info_directory):
        os.makedirs(info_directory)

    # 将用户信息保存到指定的 JSON 文件
    info_file_path = os.path.join(info_directory, f"{user_name}_info.json")
    with open(info_file_path, 'w', encoding='utf-8') as info_file:
        json.dump(user_info, info_file, ensure_ascii=False, indent=4)

    print(f"用户信息已保存到: {info_file_path}")

# 加载模型并返回
def load_model(model_path = "model/MN_ROP_best_acc_params.pth"):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = App_model.MN_ROP().to(device)
    if os.path.exists(model_path):
        model.load_state_dict(torch.load(model_path))
        model.eval()  # 切换到评估模式
        print("模型加载成功")
    else:
        print(f"模型文件 {model_path} 不存在")
        return None
    return model


# 定义ROP预测的函数
def run_rop_prediction(image_path, model):
    if not os.path.exists(image_path):
        print(f"图片文件 {image_path} 不存在")
        return None, None

    predicted_class, confidence = App_model.predict_rop(image_path, model)

    if predicted_class == 1:
        return "患有ROP", confidence
    else:
        return "未患ROP", confidence







