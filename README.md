# AI健身动作分析系统 / AI Fitness Action Analysis System
![image](https://github.com/22xxlin/VisualPosture/blob/master/image/i1.gif)
![image](https://github.com/22xxlin/VisualPosture/blob/master/image/i2.gif)

[![](https://github.com/22xxlin/VisualPosture/blob/master/image/i2.gif)](https://player.bilibili.com/player.html?isOutside=true&aid=206511048&bvid=BV1Xh411h7YW&cid=367161141&p=1)

## 项目概述 / Overview
**中文**  
基于PyQt5和MediaPipe BlazePose实现的实时健身动作分析系统，具备：
- 33个人体关键点实时追踪
- 右膝关节动作完成度可视化
- 视频/摄像头多源输入支持
- 多线程同步控制架构

**English**  
Real-time fitness action analysis system based on PyQt5 and MediaPipe BlazePose, featuring:
- Real-time tracking of 33 body keypoints
- Visualized completion rate for right knee joint
- Multi-source input (video/camera)
- Multithreading synchronization architecture

## 核心功能 / Core Features
### 动作分析 / Action Analysis
| 中文描述 | English Description |
|---------|---------------------|
| 24-26-28关键点角度计算 | Angle calculation for keypoints 24(hip)-26(knee)-28(ankle) |
| 120°→170°弯曲映射为0-100%进度条 | 120°→170° bending mapped to 0-100% progress bar |
| 动态颜色反馈（洋红→绿） | Dynamic color feedback (magenta→green) |

### 交互功能 / UI Controls
| 按钮 | Button | 功能 | Function |
|-----|--------|-----|----------|
| 打开文件 | Open File | 选择视频文件 | Select video file |
| 暂停/继续 | Pause/Resume | 控制分析流程 | Control analysis process |
| 退出 | Exit | 关闭应用 | Close application |

## 环境配置 / Environment Setup
### 依赖要求 / Requirements
```bash
# 中文版本
Python == 3.7+          # 解释器
opencv-python == 4.5.2  # 图像处理
mediapipe == 0.8.3      # 姿态检测
PyQt5 == 5.15.4         # 图形界面
numpy == 1.21.6         # 数值计算
```
```bash
# English Version
Python == 3.7+          # Interpreter
opencv-python == 4.5.2  # Image processing
mediapipe == 0.8.3      # Pose detection
PyQt5 == 5.15.4         # GUI framework
numpy == 1.21.6         # Numerical computing
```

## 使用指南 / Quick Start
# 启动命令 / Launch
```bash
python youcandoit.py
```


## 操作流程 / Workflow
```bash
1点击"打开视频"选择训练录像
1Click "Open File" to select workout video
2观察右侧膝关节进度条变化
2Monitor right knee progress bar (right-side vertical bar)
3使用暂停按钮进行动作分析
3Use pause button for detailed motion analysis
```

## 📜 References
- Blog Post: [基于BlazePose的AI健身教练系统](https://blog.csdn.net/qq_43741419/article/details/123139987)
- Video Example:[BlazePose+Pyqt5+OpenCV=>基于人体姿态识别的AI健身系统](https://www.bilibili.com/video/BV1Xh411h7YW/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=6c9f912933a452f98bb4716328eb36da)
- MediaPipe Documentation: [BlazePose Overview](https://google.github.io/mediapipe/solutions/pose)
- PyQt5 Framework: [Official Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)



