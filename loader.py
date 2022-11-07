import os
import gdown

# download YOLOv5 weights:
os.mkdir('weights')
url = 'https://drive.google.com/file/d/1wGdTdIu0INb7S5VBht49mNDnxj0_HIBE/view?usp=share_link'
output = 'weights/best.pt'
gdown.download(url=url, output=output, quiet=False, fuzzy=True)

# download custom easyocr weights:
os.mkdir('custom_easyocr/model')
url = 'https://drive.google.com/file/d/1I03JdYkM3d06U--Rsm0mM6cZ3WXY-qmU/view?usp=share_link'
output = 'custom_easyocr/model/custom_example.pth'
gdown.download(url=url, output=output, quiet=False, fuzzy=True)

# download test video:
url = 'https://drive.google.com/file/d/1Y0H5TJ4O77YNC_l3boIxNFKPFhKUIsZY/view?usp=share_link'
output = 'test/video.mp4'
gdown.download(url=url, output=output, quiet=False, fuzzy=True)