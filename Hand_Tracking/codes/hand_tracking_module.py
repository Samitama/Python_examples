import cv2
import mediapipe as mp
import time


class handDetector:
    def __init__(self,mode = False, maxHands = 2, detectionCon = 0.5,trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,
                                        self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils    
    def findHands(self,img,draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks :
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmark(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return img

     #for id,lm in enumerate(handLms.landmark):
      #              h, w, c = img.shape
       #             cx, cy = int(lm.x*w), int(lm.y*h)
        #            #print(id, cx, cy)
         #           #if id == 4:
          #          cv2.circle(img,(cx, cy), 15, (255, 0, 255), cv2.FILLED)
def main():
        ptime = 0
        ctime = 0
        cap = cv2.VideoCapture(0)
        Detector = handDetector()
        while True:
            success, img = cap.read()
            img = Detector.findHands(img)
            ctime = time.time()
            fps = 1/(ctime-ptime)
            ptime = ctime
            cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
            cv2.imshow('sami',img)
            if cv2.waitKey(30) & 0xFF == ord('esc'):
                break
if __name__ == "__main__":
    main()