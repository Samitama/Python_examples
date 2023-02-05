import cv2
import numpy as np



def thresholding(img):
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerwhite = np.array([80,0,0])
    upperwhite = np.array([255,160,255])
    maskWhite = cv2.inRange(imgHsv,lowerwhite,upperwhite)
    return maskWhite
def warpimg(img,points,w,h,inv=False):
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    if inv:
        matrix = cv2.getPerspectiveTransform(pts2,pts1)
    else : 
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgWrap = cv2.warpPerspective(img,matrix,(w,h))
    return imgWrap
def nothing(a):
    pass
def initializeTrackbars(intialTracbarVals,wT=480, hT=240):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top", "Trackbars", intialTracbarVals[0],wT//2, nothing)
    cv2.createTrackbar("Height Top", "Trackbars", intialTracbarVals[1], hT, nothing)
    cv2.createTrackbar("Width Bottom", "Trackbars", intialTracbarVals[2],wT//2, nothing)
    cv2.createTrackbar("Height Bottom", "Trackbars", intialTracbarVals[3], hT, nothing)

def valTrackbars(wT=480, hT=240):
    widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
    heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
    widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
    heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
    points = np.float32([(widthTop, heightTop), (wT-widthTop, heightTop),
                      (widthBottom , heightBottom ), (wT-widthBottom, heightBottom)])
    return points

def drawPoints(img,points):
    for i in range(4):
        cv2.circle(img,(int(points[i][0]),int(points[i][1])),15,(0,0,255),cv2.FILLED)
    return img


def getHistogram(img,minPer=0.1,display=False,minval=0.1,region=1):
    if region==1:
        histvalues = np.sum(img,axis=0)
    else :
        histvalues = np.sum(img[img.shape[0]//region:,:],axis=0)
    maxvalue = np.max(histvalues)
    minvalue = minPer*maxvalue
    indexarray = np.where(histvalues >= minvalue)
    basepoint = int(np.average(indexarray))
    if display:
        imgHist = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
        for i ,intensity in enumerate(histvalues):
            cv2.line(imgHist,(i,img.shape[0]),(i,img.shape[0]-(intensity//255//region)),(255,0,255),1)
            cv2.circle(imgHist,(basepoint,img.shape[0]),20,(0,255,255),cv2.FILLED)
        return basepoint,imgHist
    return basepoint