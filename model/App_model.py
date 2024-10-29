import torch
import cv2
import os
import torch.nn as nn  # 添加此行以导入 torch.nn
from torchvision import models
from torchvision import transforms
# from Pre_processing.clahe_apply import pre_processing  # 预处理函数
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class MN_ROP(nn.Module):
    def __init__(self, num_classes=2):
        super(MN_ROP, self).__init__()
        self.MNV2 = models.mobilenet_v2(weights="IMAGENET1K_V1")
        self.fc = nn.Linear(1000, num_classes)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        out = self.MNV2(x)
        out = self.fc(out)
        out = self.softmax(out)
        return out



# 进行ROP检测的函数
def predict_rop(image_path, model):
    model.eval()  # 切换到评估模式
    image = cv2.imread(image_path)
    image = torch.from_numpy(image).float().permute(2, 0, 1).unsqueeze(0) / 255
    image = image.to(device)
    with torch.no_grad():
        outputs = model(image)
        _, predicted_class = torch.max(outputs, 1)  # 获取预测结果类别
        confidence = torch.softmax(outputs, dim=1)[0, predicted_class].item()  # 获取预测置信度

    return predicted_class.item(), confidence

# 主函数
if __name__ == "__main__":
    # 加载模型
    student_model = MN_ROP().to(device)
    student_model.load_state_dict(torch.load("MN_ROP_best_acc_params.pth"))  # 加载已训练好的学生模型

    # 输入图像路径进行ROP检测

    current_dir = os.path.dirname(os.path.abspath(__file__))  # 获取当前脚本所在目录
    image_path = os.path.join(current_dir, '..', 'Resource', 'Picture', 'Stage_1_ROP_60.jpg')  # 替换为要检测的眼底图像路径
    predicted_class, confidence = predict_rop(image_path, student_model)

    if predicted_class == 1:
        print(f"检测结果: 患有ROP (置信度: {confidence:.2f})")
    else:
        print(f"检测结果: 未患ROP (置信度: {confidence:.2f})")
