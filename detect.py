import cv2
import torch
import easyocr

def video(video_path):
    capture = cv2.VideoCapture(video_path)

    model = torch.hub.load(
        'yolov5',
        'custom',
        path='weights/best.pt',
        force_reload=True,
        source='local'
    )

    reader = easyocr.Reader(
        ['ru'],
        model_storage_directory='custom_easyocr/model',
        user_network_directory='custom_easyocr/user_network',
        recog_network='custom_example'
    )

    while capture.isOpened():
        ret, image = capture.read()
        if image is None:
            break
        img = image.copy()
        result = model(image)
        cordinates = result.xyxyn[0][:, :-1]
        if cordinates.shape[0] != 0:
            width, height = image.shape[1], image.shape[0]

            for row in cordinates:
                x1, y1, x2, y2 = (int(row[0] * width), int(row[1] * height),
                                  int(row[2] * width), int(row[3] * height))

                img_gray = cv2.cvtColor(image[y1:y2, x1:x2], cv2.COLOR_BGR2GRAY)
                read = reader.readtext(
                    img_gray,
                    allowlist='0123456789АВЕКМНОРСТУХ'
                )

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y1 - 28), (x2, y1), (51, 51, 255), -1)

                if not read:
                    continue
                plate = ''
                for i in range(len(read)):
                    if i < 2 and read[i][-1] > 0.5:
                        plate += read[i][-2]
                    elif read[i][-1] > 0.8:
                        plate += read[i][-2]

                cv2.putText(img, ' ' + plate, (x1, y1 - 10), cv2.FONT_HERSHEY_COMPLEX,
                            0.55, (255, 255, 255), 2)

            cv2.imshow('video', img)
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    video('test/video.mp4')
