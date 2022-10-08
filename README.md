# License plates detection with YOLOv5 and EasyOCR

### Установка зависимостей
```
pip install -r requirements.txt
```

### Запуск пайплайна
*   Клонируйте репозиторий ``` git clone https://github.com/ultralytics/yolov5 ```
*   Загрузите [веса модели](https://drive.google.com/drive/folders/1vwSxXGE69TGpm8ONGjzn9BTuJde8DhN9)
*   Запустите detect.py, передав на вход фунции путь к видеофайлу

### Обучение модели YOLOv5
```
python train.py --img 640 --batch 16 --epochs 50 --data custom.yaml --weights yolov5x.pt --cache
```

### Эксперименты
Models  | Precision | Recall   | mAP50     | mAP50-95
  ---   |    ---    |   ---    |    ---    |   ---
YOLOv5s |   0.766   |  0.638   |   0.703   |  0.317
YOLOv5m |   0.786   |  0.681   |   0.742   |  0.37
YOLOv5x |   0.825   |  0.785   |   0.832   |  0.424

