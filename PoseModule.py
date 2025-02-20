# -*- codeing =utf-8 -*-
# @Time : 2021/7/3 15:24
# @Author : ArLin
# @File : PoseModule.py
# @Software: PyCharm
import cv2
import mediapipe as mp
import math
import numpy as np

class poseDetector():
    def __init__(self,mode=False,upBody=False,smooth=True,
                 detectionCon=0.5,trackCon=0.5):
        '''
        初始化
        :param static_image_mode: 是否是静态图片，默认为否
        :param upper_body_only: 是否是上半身，默认为否
         :param smooth_landmarks: 设置为True减少抖动
        :param min_detection_confidence:人员检测模型的最小置信度值，默认为0.5
        :param min_tracking_confidence:姿势可信标记的最小置信度值，默认为0.5
         '''

        self.mode=mode
        self.upBody=upBody
        self.smooth=smooth
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        # 创建一个Pose对象用于检测人体姿势
        self.pose = self.mpPose.Pose(self.mode,self.upBody,self.smooth,
                                     self.detectionCon,self.trackCon)

    def findPose(self,img,draw=True):
        '''
            检测姿势方法
            :param img: 一帧图像
            :param draw: 是否画出人体姿势节点和连接图
            :return: 处理过的图像
        '''
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)#会识别这帧图片中的人体姿势数据，
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                            self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self,img,draw=True):
        '''
             获取人体姿势数据
             :param img: 一帧图像
             :param draw: 是否画出人体姿势节点和连接图
             :return: 人体姿势数据列表
             '''
        # 人体姿势数据列表，每个成员由3个数字组成：id, x, y
        # id代表人体的某个关节点，x和y代表坐标位置数据
        self.lmList=[]
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                #print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList

    def findAngle(self,img,p1,p2,p3,draw=True):
        '''
        获取人体姿势中3个点p1-p2-p3的角度
        :param img: 一帧图像
        :param p1: 第1个点
        :param p2: 第2个点
        :param p3: 第3个点
        :param draw: 是否画出3个点的连接图
        :return: 角度
        '''


        #Get the landmarks
        x1,y1=self.lmList[p1][1:]
        x2,y2=self.lmList[p2][1:]
        x3,y3=self.lmList[p3][1:]


        #Calculate the Angle
        # 使用三角函数公式获取3个点p1-p2-p3，以p2为角的角度值，0-180度之间
        angle=math.degrees(math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2))
        print(angle)
        if angle<0:
            angle+=360

        #Draw
        if draw:
            cv2.line(img,(x1,y1),(x2,y2),(255,255,255),3)
            cv2.line(img,(x3,y3),(x2, y2),(255,255,255),3)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
            # cv2.putText(img,str(int(angle)),(x2-50,y2+50),
            #             cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
        return angle

def main():
    cap = cv2.VideoCapture('../PoseVideos/5.mp4')
    success, img = cap.read()
    #img = cv2.resize(img, (1280, 520))
    i = 0
    detector = poseDetector()
    count = 0
    dir = 0

    while success:
        i = i + 1
        img = cv2.resize(img, (1000, 720))
        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)
        # print(lmList)
        if len(lmList) != 0:
            # 右手
            #angle = detector.findAngle(img, 12, 14, 16)
            # # Left Arm
            # angle = detector.findAngle(img, 11, 13, 15,False)
          #这里就是改一下健身的部位就行
            #右腿
            angle = detector.findAngle(img, 23, 25, 27)
            per = np.interp(angle, (210, 310), (0, 100))
            bar = np.interp(angle, (220, 310), (650, 100))
            # print(angle, per)

            # Check for the dumbbell curls
            color = (255, 0, 255)
            if per == 100:
                color = (0, 255, 0)
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                color = (0, 255, 0)
                if dir == 1:
                    count += 0.5
                    dir = 0



            cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
            cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                        color, 4)

            # cv2.rectangle(img, (920, 100), (975, 550), color, 3)
            # cv2.rectangle(img, (920, int(bar)), (975, 550), color, cv2.FILLED)
            # cv2.putText(img, f'{int(per)} %', (920, 50), cv2.FONT_HERSHEY_PLAIN, 4,
            #             color, 4)

            # Draw Curl Count
            # cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
            # cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
            #             (255, 0, 0), 25)
        pro_image(img)
        if success:
            print('success', i)
            success, img = cap.read()

def pro_image(img):
    cv2.namedWindow('Image', 0)
    cv2.imshow("Image", img)
    cv2.waitKey(1)



if __name__ == '__main__':
    main()
