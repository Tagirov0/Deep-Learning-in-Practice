# License plates detection with YOLOv5 and EasyOCR

### Install dependencies
```
pip install -r requirements.txt
```

### Usage
``` 
# clone repository:
git clone https://github.com/Tagirov0/Deep-Learning-in-Practice

cd Deep-Learning-in-Practice

# clone repository:
git clone https://github.com/ultralytics/yolov5

# download weights and test video:
python loader.py

# run pipeline
python detect.py
```

### Train YOLOv5
```
python train.py --img 640 --batch 16 --epochs 50 --data custom.yaml --weights yolov5x.pt --cache
```

### Experiments
#### YOLOv5:
Models  | Parameters                         | Precision |  Recall   |   mAP50   | mAP50-95
  ---   |             ---                    |   ---     |    ---    |     ---   |   ---
YOLOv5s | batch_size=32, fl_gamma=0             |   0.766   |   0.638   |   0.703   |  0.317
YOLOv5m | batch_size=32, fl_gamma=1              |   0.736  |    0.574  |    0.637  |    0.336
YOLOv5m | batch_size=32, fl_gamma=0            |   0.786   |   0.681   |   0.742   |  0.37
YOLOv5x | batch_size=16, fl_gamma=0              |   0.825   |   0.785   |   0.832   |  0.424

#### EasyOCR:
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

### Three
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
└── requirements.txt
```
