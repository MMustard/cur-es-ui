import torch
import torch.nn as nn
import piq

from tqdm import tqdm
import os
import json

class DimNotMatch(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message

  
def compute_metric(pre):
    metric = {}
    """这里为了让他们 #类型# 统一故都将其转化为bool type"""
    metric["iou"] = compute_iou(pre).data.item()
    metric["pa"] = compute_pa(pre).data.item()
    metric["mae"] = compute_mae(pre).data.item()
    metric["ber"] = compute_ber(pre).data.item()
    return metric


def compute_iou(pre):

    brisque = piq.brisque(pre)
    print("iou")
    return brisque


def compute_mae(pre):
    brisque = piq.brisque(pre)
    print("iou")
    return brisque


def compute_ber(pre):
    brisque = piq.brisque(pre)
    print("iou")
    return brisque


def compute_pa(pre):
    brisque = piq.brisque(pre)
    print("iou")
    return brisque
