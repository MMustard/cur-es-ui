import torch.nn as nn
import torch
import torchvision
import torch.optim
import os
from torchvision import transforms
from .functions import compute_metric
import model
import numpy as np
from PIL import Image
import time
import gradio as gr
import cv2

def infer(net: nn.Module, input, metrics=None, baseline_metrics=None, args=None):
    if args is None:
        args = {"result_path": "./prediciton"}
    net.eval()
    w, h = input["img"].size
    data_lowlight = input["img"]
    data_lowlight = (np.asarray(data_lowlight) / 255.0)

    data_lowlight = torch.from_numpy(data_lowlight).float()
    data_lowlight = data_lowlight.permute(2, 0, 1)
    # data_lowlight = data_lowlight.cuda().unsqueeze(0)
    data_lowlight = data_lowlight.unsqueeze(0)

    start = time.time()
    _, enhanced_image, _ = net(data_lowlight)

    end_time = (time.time() - start)
    print(end_time)



    """返回我的模型的指标"""
    metric = metrics[str(input["id"])]

    """得到baseline的指标"""
    # global metrics
    metric_baseline = baseline_metrics[str(input["id"])]

    to_pil = transforms.ToPILImage()
    final = Image.fromarray(np.array(transforms.Resize((h, w))(to_pil(enhanced_image.squeeze(0)))))

    result = {"pre": final, "pre_metric": metric,
              "baseline_metric": metric_baseline}

    # result = {"pre": pre_pil, "pre_metric": metric,
    #           "baseline_metric": metric_baseline}

    return result
