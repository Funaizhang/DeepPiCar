import logging
import cv2
import matplotlib.pyplot as plt

from lane_follower import HandCodedLaneFollower


class Test:
    def test_photo(self, file):
        land_follower = HandCodedLaneFollower()
        frame = cv2.imread(file)
        combo_image = land_follower.follow_lane(frame)
        imgplot = plt.imshow(combo_image)
        plt.show()
        # cv2.imshow('final', combo_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def test_video(self, video_file):
        lane_follower = HandCodedLaneFollower()
        cap = cv2.VideoCapture(video_file + '.avi')

        # skip first second of video.
        for i in range(3):
            _, frame = cap.read()

        video_type = cv2.VideoWriter_fourcc(*'XVID')
        video_overlay = cv2.VideoWriter("%s_overlay.avi" % (video_file), video_type, 20.0, (320, 240))
        try:
            i = 0
            while cap.isOpened():
                _, frame = cap.read()
                print('frame %s' % i)
                combo_image = lane_follower.follow_lane(frame)

                cv2.imwrite("%s_%03d_%03d.png" % (video_file, i, lane_follower.curr_steering_angle), frame)

                cv2.imwrite("%s_overlay_%03d.png" % (video_file, i), combo_image)
                video_overlay.write(combo_image)
                cv2.imshow("Road with Lane line", combo_image)

                i += 1
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            cap.release()
            video_overlay.release()
            cv2.destroyAllWindows()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    input_path = 'images/10.jpg'
    output_path = ''
    myTest = Test()
    myTest.test_photo(input_path)
