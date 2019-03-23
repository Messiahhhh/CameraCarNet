import cv2
class VideoCamera(object):
    def __init__(self):
        # 通过opencv获取实时视频流
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        # cv2.imshow("image",image)
        # cv2.waitKey (10000000)
        ret, jpeg = cv2.imencode('.jpg', image)
        # cv2.imshow(jpeg)
        return jpeg.tobytes()
        # return jpeg