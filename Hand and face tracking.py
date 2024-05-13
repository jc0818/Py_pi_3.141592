import cv2
import mediapipe as mp

def main():
    # 미디어파이프 핸드 트래킹 모델 로드
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    # 미디어파이프 얼굴 트래킹 모델 로드
    mp_face_detection = mp.solutions.face_detection
    face_detection = mp_face_detection.FaceDetection()

    # OpenCV 비디오 캡처 설정
    cap = cv2.VideoCapture(0)

    # 초기 트래킹 모드 설정 (hand: 핸드 트래킹, face: 얼굴 트래킹)
    tracking_mode = 'hand'

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("비디오를 읽을 수 없습니다.")
            break

        # 키 입력 감지
        key = cv2.waitKey(1) & 0xFF

        if key == ord('f') and tracking_mode == 'hand':
            tracking_mode = 'face'
            print("얼굴 트래킹 모드로 전환")
        elif key == ord('f') and tracking_mode == 'face':
            tracking_mode = 'hand'
            print("핸드 트래킹 모드로 전환")

        # 프레임을 BGR에서 RGB로 변환
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if tracking_mode == 'hand':
            # 미디어파이프를 사용하여 핸드 감지
            results = hands.process(rgb_frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    for lm in hand_landmarks.landmark:
                        # 감지된 핸드의 각 랜드마크를 출력
                        h, w, c = frame.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)
                
                # 랜드마크에 이어지는 선 그리기
                mp_drawing = mp.solutions.drawing_utils
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        elif tracking_mode == 'face':
            # 미디어파이프를 사용하여 얼굴 감지
            results = face_detection.process(rgb_frame)

            if results.detections:
                for detection in results.detections:
                    bboxC = detection.location_data.relative_bounding_box
                    ih, iw, _ = frame.shape
                    x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 프레임 표시
        cv2.imshow('Tracking', frame)

        # 'q'를 누르면 종료
        if key == ord('q'):
            break

    # 작업 완료 후 해제
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
