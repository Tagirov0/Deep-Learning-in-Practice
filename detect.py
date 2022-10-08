import re
import cv2
import torch
import easyocr

def video(video_path):
    capture = cv2.VideoCapture(video_path)

    model = torch.hub.load('yolov5', 'custom',
                           path='best.pt', force_reload=True,
                           source='local')

    reader = easyocr.Reader(['ru'])

    while capture.isOpened():
        ret, image = capture.read()
        img = image.copy()
        if image is None:
            break
        result = model(image)
        cordinates = result.xyxyn[0][:, :-1]
        if cordinates.shape[0] == 0:
            continue

        width, height = image.shape[1], image.shape[0]

        for row in cordinates:
            x1, y1, x2, y2 = (int(row[0] * width), int(row[1] * height),
                              int(row[2] * width), int(row[3] * height))

            img_gray = cv2.cvtColor(image[y1:y2, x1:x2], cv2.COLOR_BGR2GRAY)
            read = reader.readtext(img_gray)

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y1 - 28), (x2, y1), (51, 51, 255), -1)
            if read:
                plate = ''.join(re.findall(r'[А-Я-0-9]', read[0][-2].upper()))
                cv2.putText(img, ' ' + plate, (x1, y1 - 10), cv2.FONT_HERSHEY_COMPLEX,
                            0.55, (255, 255, 255), 2)

        cv2.imshow('video', img)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    video('ru2.mp4')