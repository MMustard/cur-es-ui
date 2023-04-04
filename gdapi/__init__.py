from .model import enhance_net_nopool
from .gdApi import infer
import torch
import json
import os

dir = os.getcwd() + "/snapshots/Epoch99.pth"

# net = DecoupleNet("4d", loadpretrain=False).cuda()
net = enhance_net_nopool()
net.eval()

with open('./gdapi/metrics.json', 'r', encoding='utf8')as fp:
    metrics = json.load(fp)

with open('./gdapi/baseline_metrics.json', 'r', encoding='utf8')as fp:
    base_metrics = json.load(fp)

state = torch.load(dir, map_location=torch.device('cpu'))
net.load_state_dict({k.replace('module.', ''): v for k, v in state.items()})
# net.load_state_dict(torch.load(dir, map_location={
#                     'cuda:7': 'cuda:0'}), strict=True)
