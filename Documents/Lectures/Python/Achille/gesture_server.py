import cv2
import mediapipe as mp
import asyncio
import websockets
import json

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

async def gesture_stream(websocket):
    prev_x = None
    prev_y = None

    while True:
        success, frame = cap.read()
        if not success:
            continue

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        data = {"dx": 0, "dy": 0, "zoom": 0, "rotate": 0}

        if result.multi_hand_landmarks:
            lm = result.multi_hand_landmarks[0].landmark
            x = lm[8].x
            y = lm[8].y

            if prev_x is not None:
                data["dx"] = (x - prev_x) * 5
                data["dy"] = (y - prev_y) * 5

            prev_x, prev_y = x, y

            # Zoom (thumb-index distance)
            dist = abs(lm[4].x - lm[8].x)
            data["zoom"] = (0.2 - dist) * 10

            # Rotation (wrist movement)
            data["rotate"] = (lm[0].x - 0.5) * 2

        await websocket.send(json.dumps(data))
        await asyncio.sleep(0.03)

async def main():
    async with websockets.serve(gesture_stream, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())
