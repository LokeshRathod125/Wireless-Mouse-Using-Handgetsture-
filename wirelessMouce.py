import cv2
import mediapipe as mp
import pyautogui
import numpy as np

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size()
click_down = False  # To prevent multiple clicks

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            if len(lm_list) >= 9:
                # Move mouse with index finger
                x, y = lm_list[8]  # Index finger tip
                screen_x = int(np.interp(x, [0, w], [0, screen_w]))
                screen_y = int(np.interp(y, [0, h], [0, screen_h]))
                pyautogui.moveTo(screen_x, screen_y)

                # Detect click: distance between index finger tip (8) and thumb tip (4)
                x1, y1 = lm_list[4]  # Thumb tip
                x2, y2 = lm_list[8]  # Index finger tip
                distance = np.hypot(x2 - x1, y2 - y1)
                if distance < 30 and not click_down:
                    pyautogui.click()
                    click_down = True
                elif distance >= 30:
                    click_down = False

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Wireless Mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()