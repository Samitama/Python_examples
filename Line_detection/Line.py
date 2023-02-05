import cv2
import numpy as np
import utlis 

curvelist = []
avgval = 10
def getLaneCurve(img):
    imgcopy = img.copy()
    imgThres = utlis.thresholding(img)
    h,w,c= img.shape
    points = utlis.valTrackbars()
    imgWarp = utlis.warpimg(imgThres,points,w,h)
    imgWarpPoints = utlis.drawPoints(imgcopy,points)
    midPoint,imgHist = utlis.getHistogram(imgWarp,display=True,minPer=0.5,region=4)
    curvePoint,imgHist = utlis.getHistogram(imgWarp,display=True,minPer=0.9)
    curveraw = curvePoint - midPoint
    curvelist.append(curveraw)
    if len(curvelist)>avgval:
        curvelist.pop(0)
    curve = int(sum(curvelist)//len(curvelist))
    cv2.imshow('sami2',imgThres)
    cv2.imshow('sami3',imgWarp)
    cv2.imshow('sami4',imgWarpPoints)
    cv2.imshow('sami5',imgHist)
    return None



if __name__ == '__main__':
    cap = cv2.VideoCapture('Line_detection/vid1.mp4')
    Value = [102,80,20,214]
    utlis.initializeTrackbars(Value)
    frameCounter = 0

    while True:
        frameCounter +=1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT)==frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES,0)
            frameCounter = 0
        success, img = cap.read()
        img = cv2.resize(img,dsize=(480,240))
        getLaneCurve(img)
        cv2.imshow('sami',img)
        if cv2.waitKey(10) & 0xFF == 27:
            break