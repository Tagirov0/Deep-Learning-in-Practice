# License plates detection with YOLOv5 and EasyOCR

### Install dependencies
```
pip install -r requirements.txt
```

### Usage
``` 
# clone repository:
git clone https://github.com/ultralytics/yolov5

# download YOLOv5 weights:
gdown "1wGdTdIu0INb7S5VBht49mNDnxj0_HIBE"

# download custom easyocr weights:
gdown ""

# download test video:
gdown "1Y0H5TJ4O77YNC_l3boIxNFKPFhKUIsZY"

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
```
WER=\frac{S + D + I}{N}
```
`S` is the number of substitutions, `D` is the number of deletions, `I` is the number of insertions, `C` is the number of correct words, `N` is the number of words in the reference (N=S+D+C). This value indicates the average number of errors per reference word. 

#### Character error rate (CER) - similar to Word Error Rate (WER), but operates on character instead of word.

**The lower the value of WER and CER, the better the performance of the OCR system with a WER and CER of 0 being a perfect score.**

```
.
├── custom easyocr                  
├── test                   
├── Detection.ipynb 
├── README.md
├── detect.py           
└── requirements.txt
```
