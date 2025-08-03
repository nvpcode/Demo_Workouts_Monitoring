# README.md

## Count Push-Ups

A video-based workout monitoring system using YOLO pose estimation to count push-ups and display exercise stage.

---

### Demo
▶️ [Watch the demo video](https://drive.google.com/file/d/1Eu-Br9U-Nc4YbIWeoquwa_u47q29-rC2/view?usp=drive_link)

---

### Requirements

- Python 3.8+
- OpenCV (`cv2`)
- Ultralytics (`ultralytics`)
- YOLO pose model file (`yolo11m-pose.pt`)
- Input video named `input2.MOV`

---

### Installation

```sh
pip install opencv-python ultralytics
```

---

### Usage

1. Place your workout video in the project folder as `input2.MOV`.
2. Make sure the pose model file `yolo11m-pose.pt` is available in the project directory.
3. Run the program:

```sh
python main.py
```

4. The processed video will be saved as `output.avi`, showing the push-up count and current stage (up/down) on each frame.

---

### Source Code Explanation

- [main.py](d:\Projects_COMPUTER_VISION\venv\Project_Workouts_Monitoring\main.py): 
  - Reads the input video.
  - Uses YOLO pose estimation to detect keypoints and monitor push-ups.
  - Displays the number of push-ups and exercise stage on the video.
  - Saves the processed video to `output.avi`.

---

### Contact

For questions, please contact via email: nguyenphuongv07@gmail.com.
