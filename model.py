from gdapi import *
from PIL import Image

def inference(id, img, gt, metrics , base_metrics):
    input = {
        "id": id,
        "img": img,
        "mask": gt,
    }
    output = infer(net, input, metrics=metrics, baseline_metrics=base_metrics, args=None)
    return output['pre'], output['pre_metric'], output['baseline_metric']

