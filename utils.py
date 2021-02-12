import logging
import os
import time
from typing import List
import cv2


class VideoProc:
    def __init__(self, input_path: str, output_path: str):
        self.video_file = input_path
        self.output_path = output_path
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    def extract_frame(self, times: List[int]) -> None:
        cap = cv2.VideoCapture(self.video_file)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        times.sort()
        count = 0
        time_idx = 0
        success = True

        while success:
            success, frame = cap.read()

            # Save the wanted frames
            if time_idx < len(times) and count == times[time_idx] * fps:
                print(os.path.join(self.output_path, f'{count}.jpg'))
                cv2.imwrite(os.path.join(self.output_path, f'{count}.jpg'), frame)
                print(f'Successfully written frame at {times[time_idx]}s')
                time_idx += 1
            count += 1

            # Check end of video
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    input_path = 'car_video_objs201128_170702.avi'
    output_path = 'images'
    times = [0.5, 1, 1.5, 2, 2.5, 3]
    myVideoProc = VideoProc(input_path, output_path)
    myVideoProc.extract_frame(times)
