import torch
import torchvision
import torch.optim
import os
import model
import numpy as np
from PIL import Image
import time
import gradio as gr
import cv2
 
def lowlight(_file, image):
	os.environ['CUDA_VISIBLE_DEVICES']='0'
	print(_file)
	im = Image.fromarray(image)
	image_path = 'test/1002.jpg'
	im.save(image_path)
	data_lowlight = Image.open(image_path)
	data_lowlight = (np.asarray(data_lowlight)/255.0)
	"""R, G, B = data_lowlight[:, :, 0], data_lowlight[:, :, 1], data_lowlight[:, :, 2]
	data_lowlight[:, :, 0] = B
	data_lowlight[:, :, 1] = G
	data_lowlight[:, :, 2] = R"""

	data_lowlight = torch.from_numpy(data_lowlight).float()
	data_lowlight = data_lowlight.permute(2,0,1)
	data_lowlight = data_lowlight.cuda().unsqueeze(0)

	DCE_net = model.enhance_net_nopool().cuda()
	# DCE_net.load_state_dict(torch.load(_file))
	DCE_net.load_state_dict(torch.load(_file.name))
	start = time.time()
	_,enhanced_image,_ = DCE_net(data_lowlight)

	end_time = (time.time() - start)
	print(end_time)
	result_path = './test_result/1.jpg'
	torchvision.utils.save_image(enhanced_image, result_path)
	img = cv2.imread(result_path)
	return img

if __name__ == '__main__':
# test_images
	with torch.no_grad():
		input = [gr.inputs.File(file_count="single", type="file", label="zero dce weight", optional=False),
				 gr.Image(label="Target picture", shape=(1101, 800))]
		output = [gr.Image(label="Result picture")]
	interface = gr.Interface(fn=lowlight, inputs=input, outputs=output, )
	interface.launch()

		

