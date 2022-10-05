import cv2
import torch
import easyocr

def video(path=None):
    capture = cv2.VideoCapture(path)

    model = torch.hub.load('..yolov5', 'custom', path='best.pt', force_reload=True, source='local')

    reader = easyocr.Reader(['ru'])

    while capture.isOpened():
        ret, image = capture.read()
        if image is None:
            break
        result = model(image)
        cordinates = result.xyxyn[0][:, :-1]
        if len(cordinates) == 0:
            continue

        width, height = image.shape[1], image.shape[0]

        for row in cordinates:
            x1, y1, x2, y2 = int(row[0] * width), int(row[1] * height), int(row[2] * width), int(row[3] * height)

            img_gray = cv2.cvtColor(image[y1:y2, x1:x2], cv2.COLOR_BGR2GRAY)

            read = reader.readtext(img_gray)
            try:
                if len(read) != 0:
                    plate = read[0][-2].upper().replace(';', '')
                else:
                    plate = "не опознал"
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(image, (x1, y1 - 28), (x2, y1), (51, 51, 255), -1)
                if len(read) != 0:
                    cv2.putText(image, ' ' + plate, (x1, y1 - 10), cv2.FONT_HERSHEY_COMPLEX,
                                0.55, (255, 255, 255), 2)
            except:
                print(read)

        cv2.imshow("video", image)
        cv2.waitKey(1)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    video('spb.mp4')