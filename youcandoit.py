# -*- codeing =utf-8 -*-
# @Time : 2021/7/6 11:04
# @Author : ArLin
# @File : Text2.py
# @Software: PyCharm
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from uGUI import Ui_MainWindow
import sys
import cv2
import numpy
import librosa
import numpy as np

import PoseModule as pm
class MyThread(QThread):
    sinOut = pyqtSignal(QImage)
    def __init__(self, imgname,imgType):
        super(MyThread, self).__init__()
        self._isPause = False
        self._value = 0
        self.cond = QWaitCondition()
        self.mutex = QMutex()
        self.imgname = imgname
        self.imgType = imgType
    def pause(self):
        #print("线程休眠")
        self._isPause = True
    def resume(self):
        #print("线程启动")
        self._isPause = False
        self.cond.wakeAll()
    def run(self):
        #print("进来啦")
        while 1:
            self.mutex.lock()
            # opencv打开一个视频
            cap = cv2.VideoCapture(self.imgname)
            # 读取视频图片帧
            success, img = cap.read()
            i = 0
            # 创建一个PoseDetector类的对象
            detector = pm.poseDetector()
            # 方向的变量
            #count = 0
            dir = 0
            while success:
                # print("self.flag",self.flag)
                #if self.restart():
                i = i + 1
                #调整视频中图像帧的大小
                img = cv2.resize(img, (1280, 720))
                # 检测视频图片帧中人体姿势
                img = detector.findPose(img, False)
                # 获取人体姿势列表数据
                lmList = detector.findPosition(img, False)
                # print(lmList)
                if len(lmList) != 0:
                    # Right Arm
                    #angle = detector.findAngle(img, 11, 13, 15)
                    # # Left Arm
                    # angle = detector.findAngle(img, 11, 13, 15,False)
                    angle = detector.findAngle(img, 24, 26, 28)
                    #以50到150度检测右手肘弯曲的程度
                    #per = np.interp(angle, (210, 310), (0, 100))
                    per = np.interp(angle, (120, 170), (0, 100))
                    # 进度条高度数据
                    #bar = np.interp(angle, (220, 310), (650, 100))
                    bar = np.interp(angle, (120, 170), (650, 100))
                    # print(angle, per)
                    # Check for the dumbbell curls
                    color = (255, 0, 255)
                    if per == 100:
                        color = (0, 255, 0)
                        if dir == 0:
                            #count += 0.5
                            dir = 1
                    if per == 0:
                        color = (0, 255, 0)
                        if dir == 1:
                            #count += 0.5
                            dir = 0
                    # 使用opencv画进度条和写右手肘弯曲的程度
                    cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
                    cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
                    cv2.putText(img, f'{int(per)} %', (1050, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                                color, 4)
                self.pro_image(img)
                if success:
                    #print('success', i)
                    success, img = cap.read()
                if self._isPause: self.cond.wait(self.mutex)

            self.msleep(1000)
            self.mutex.unlock()


    def pro_image(self, img):
        height, width, depth = img.shape
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        qtimg = QImage(img.data, width, height, width * depth, QImage.Format_RGB888)
        self.sinOut.emit(qtimg)
        # self.video.setPixmap(QPixmap(qtimg))
        cv2.waitKey(1)

class myMainWindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.btn_open.clicked.connect(self.openfile)
        self.btn_ext.clicked.connect(self.exit)
        self.btn_open_2.clicked.connect(self.openfile)
        # # self.btn_ext.clicked.connect(self.exit)
        # self.btn_stop.clicked.connect(self.t.pause)
        # self.btn_ok.clicked.connect(self.t.resume)

    def openfile(self):

        imgname, imgType = QFileDialog.getOpenFileName(self, "打开视频", "", "All Files(*)")

        self.t =  MyThread(imgname,imgType)
        self.btn_stop.clicked.connect(self.t.pause)
        self.btn_ok.clicked.connect(self.t.resume)
        self.t.sinOut.connect(self.updatalabel)
        self.t.start()

    def exit(self):
        self.close()

    def updatalabel(self, qtimg):
        self.video.setPixmap(QPixmap(qtimg))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vieo_gui = myMainWindow()
    vieo_gui.show()
    sys.exit(app.exec_())