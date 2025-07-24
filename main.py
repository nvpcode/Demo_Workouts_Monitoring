import cv2
from ultralytics import solutions

cap = cv2.VideoCapture("input2.MOV")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Init AIGym
gym = solutions.AIGym(
    show=False,  # display the frame
    kpts=[6,8,10],  # keypoints for monitoring specific exercise, by default it's for pushup
    model="yolo11m-pose.pt",  # path to the YOLO11 pose estimation model file
    conf = 0.5, # Đặt ngưỡng tin cậy cho việc phát hiện; giá trị thấp hơn cho phép theo dõi nhiều đối tượng hơn nhưng có thể bao gồm các kết quả dương tính giả.
    down_angle = 80,
    device=0,  # use GPU if available
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = gym(im0)

    # Hiển thị số lần push-up và trạng thái (up/down)
    count = results.workout_count[0]
    stage = results.workout_stage[0]

    # Tạo văn bản
    text1 = f"Push-ups: {count}"
    text2 = f"Stage: {stage.capitalize()}"

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2.0
    font_thickness = 4
    color1 = (0, 255, 255)  # vàng
    color2 = (0, 128, 255)  # cam

    # Tính toán vị trí hiển thị giữa màn hình
    (text1_width, text1_height), _ = cv2.getTextSize(text1, font, font_scale, font_thickness)
    (text2_width, text2_height), _ = cv2.getTextSize(text2, font, font_scale, font_thickness)

    center_x = int(im0.shape[1] / 2)

    # Vị trí hiển thị
    x1 = center_x - int(text1_width / 2)
    y1 = int(im0.shape[0] / 2) - 30

    x2 = center_x - int(text2_width / 2)
    y2 = y1 + 60

    # Hiển thị text lên ảnh
    cv2.putText(results.plot_im, text1, (x1, y1), font, font_scale, color1, font_thickness)
    cv2.putText(results.plot_im, text2, (x2, y2), font, font_scale, color2, font_thickness)

    video_writer.write(results.plot_im)  # write the processed frame

cap.release()
video_writer.release()
cv2.destroyAllWindows()