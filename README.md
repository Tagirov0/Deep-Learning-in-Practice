# License plates detection with YOLOv5 and EasyOCR

## Usage
``` 
# clone repository:
git clone https://github.com/Tagirov0/license-plates-detection

cd license-plates-detection

# install dependencies
pip install -r requirements.txt

# clone repository:
git clone https://github.com/ultralytics/yolov5

# download weights and test video:
python loader.py

# run pipeline
python detect.py
```

## Example
<img src="https://github.com/Tagirov0/license-plates-detection/blob/main/test/inference.jpg" width=50% height=50%>

## Train YOLOv5
```
python train.py --img 640 --batch 16 --epochs 50 --data custom.yaml --weights yolov5x.pt --cache
```

## Experiments
### YOLOv5:
* image size=640x640

Models  | Parameters                         | Precision |  Recall   |   mAP50   | mAP50-95
  ---   |             ---                    |   ---     |    ---    |     ---   |   ---
YOLOv5s | batch_size=32, fl_gamma=0             |   0.766   |   0.638   |   0.703   |  0.317
YOLOv5s | batch_size=64, fl_gamma=0             |   0.740    |   0.752    |  0.756    |  0.349
YOLOv5m | batch_size=32, fl_gamma=1              |   0.736  |    0.574  |    0.637  |    0.336
YOLOv5m | batch_size=32, fl_gamma=0            |   0.786   |   0.681   |   0.742   |  0.370
YOLOv5x | batch_size=16, fl_gamma=0              |   0.825   |   0.785   |   0.832   |  0.424
#### Metrics:
* Precision measures how accurate is your predictions. i.e. the percentage of your predictions are correct.
* Recall measures how good you find all the positives. For example, we can find 80% of the possible positive cases in our top K predictions.
* IoU measures the overlap between 2 boundaries. We use that to measure how much our predicted boundary overlaps with the ground truth (the real object boundary).
* AP is the average over multiple IoU (the minimum IoU to consider a positive match). AP@[.5:.95] corresponds to the average AP for IoU from 0.5 to 0.95 with a step size of 0.05. mAP (mean average precision) is the average of AP.

### EasyOCR:
Models         | Accuracy  | CER   |  WER
---            |   ---     | ---   |  ---   
EasyOCR        |  0.1      | 0.57  |  0.90
Custom EasyOCR |  0.57     | 0.28  |  0.42
#### Word error rate (WER):
```math
WER=\frac{S + D + I}{N}
```
`S` is the number of substitutions, `D` is the number of deletions, `I` is the number of insertions, `C` is the number of correct words, `N` is the number of words in the reference (N=S+D+C). This value indicates the average number of errors per reference word. 

#### Character error rate (CER) - similar to Word Error Rate (WER), but operates on character instead of word.

**The lower the value of WER and CER, the better the performance of the OCR system with a WER and CER of 0 being a perfect score.**

## Perfomance
Algorithm processes up to 15 images (640x640) per second on gpu NVIDIA GeForce RTX 2060 6GB

## Scalability
It is possible to scale the system to two or more cameras while reducing the number of frames processed per second.

## Tree
```
.
├── custom_easyocr
│   ├── model       
│   │   └── custom_example.pth  
│   └── user_network    
│       ├── custom_example.py           
│       └── custom_example.yaml            
├── notebooks
│       ├── train_yolov5.ipynb
│       └── train_custom_easyocr.ipynb  
├── test
│       ├── 1.txt  
│       ├── 2.txt  
│       ├── 3.txt
│       ├── 4.txt
│       └── 5.txt  
├── README.md
├── detect.py
├── loader.py
└── requirements.txt
```
