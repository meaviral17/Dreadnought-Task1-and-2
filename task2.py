import cv2

video_capture = cv2.VideoCapture('path/to/video/file.mp4')


total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
frames_to_skip = int(total_frames * 0.75)

for i in range(total_frames):

    if i % frames_to_skip == 0:
        ret, frame = video_capture.read()
        if ret:
            cv2.imshow('Video', frame)
            cv2.waitKey(1)
        else:
            break

video_capture.release()
cv2.destroyAllWindows()
