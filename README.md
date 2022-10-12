# License plates detection with YOLOv5 and EasyOCR

### Установка зависимостей
```
pip install -r requirements.txt
```

### Запуск пайплайна
*   Клонируйте репозиторий ``` git clone https://github.com/ultralytics/yolov5 ```
*   Загрузите [веса модели](https://drive.google.com/file/d/1wGdTdIu0INb7S5VBht49mNDnxj0_HIBE/view?usp=sharing)
*   Запустите detect.py, передав на вход фунции путь к видеофайлу

### Обучение модели YOLOv5
```
python train.py --img 640 --batch 16 --epochs 50 --data custom.yaml --weights yolov5x.pt --cache
```

### Эксперименты
Models  | Parameters                         | Precision |  Recall   |   mAP50   | mAP50-95
  ---   |             ---                    |   ---     |    ---    |     ---   |   ---
YOLOv5s | batch_size=32, fl_gamma=0             |   0.766   |   0.638   |   0.703   |  0.317
YOLOv5m | batch_size=32, fl_gamma=1              |   0.736  |    0.574  |    0.637  |    0.336
YOLOv5m | batch_size=32, fl_gamma=0            |   0.786   |   0.681   |   0.742   |  0.37
YOLOv5x | batch_size=16, fl_gamma=0              |   0.825   |   0.785   |   0.832   |  0.424

