#Advanced Computer Vision with Python - Full Course 컴퓨터 비전 실습 공부 
import cv2
import mediapipe as mp
import time
import os

#Video Check 
cap = cv2.VideoCapture(0)# 0 -> 연결되어 있는 웹캡 중 0 번째

#
mpHands = mp.solutions.hands# Mediapipe의 Hands 모듈
hands = mpHands.Hands()# Hands 모델 인스턴스 생성
mpDraw = mp.solutions.drawing_utils # 랜드마크를 영상에 그려주는 유틸

#프레임 속도 조절 
pTime = 0
cTime = 0


while True:
    success, img = cap.read()
       # b. RGB로 변환 (Mediapipe는 RGB 영상을 입력으로 받음)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
     # c. Mediapipe로 영상에서 Hands 인지
    results = hands.process(imgRGB)    
    #print(results.multi_hand_landmarks) # 감지된 hand마다 21개의 랜드마크 정보가 있음
    
    
    # e. 감지된 한 개 한 개의 hand마다 랜드마크 연결선을 영상에 표시
    if results.multi_hand_landmarks:
        # 한 개의 hand마다 반복
        for handLms in results.multi_hand_landmarks: #single Hands
            for id, lm in enumerate(handLms.landmark):
                      
                #n+1 x: 0.143865407
                #y: 0.0738212
                #z: 3.75614974e-007
                #  print(id,lm) 
                
                #pixel 값으로 변환.
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(f"================\nHand LandMarks : {id}\nX좌표 : {cx}\nY좌표 : {cy}\n\n") #pixel 좌표값으로 나옴 
                if id == 0:
                    cv2.circle(img, (cx,cy),25, (1,1,255), cv2.FILLED)
                   
            # draw_landmarks로 영상(img)에 랜드마크 연결선과 점을 표시함
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    #프레임 계산 식        
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    #FPS 출력    
    cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(235,54,211),3)    
    
    cv2.imshow("Image", img) # "Image"이라는 이름의 화면창에 영상 출력
    if cv2.waitKey(1) == ord("q"): # 1ms마다 키 입력 확인, q키가 눌리면 반복 탈출
        break
    
    
cap.release()
cv2.destroyAllWindows()
