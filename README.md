## 환경설정
requirements.txt 참고
conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cudatoolkit=11.0 -c pytorch
추가로 mish-cuda 설치 필요
cd mish-cuda
python setup.py build install

## 사용법

### 1. 데이터 셋 준비
our_data 폴더안에 train 폴더를 만들고, 그 안에 images 폴더와 labels 폴더를 만들자.
예시에는 VOTT로 annotation을 만들고 preprocessing.py로 yolov4 포맷으로 변경했음. 
labels 폴더내의 txt형식으로 만들어주면 될것으로 예상됨.

### 2. 여러 파라미터 수정
(1) data 폴더 내 coco.names의 class 이름, coco.yaml에서 데이터셋 경로 및 class 개수 및 이름 수정

(2) models 롣어 내 yolov4-csp.cfg 파일을 수정해주어야 함. (filters를 (class수 + 5)*3 로 변경 및 제일 아래 class 수를 변경)

### 3. 명령어 정리
(1) train
python train.py --device 0 --batch-size 8 --data data/coco.yaml  --cfg models/yolov4-csp.cfg --weights ''

(2) test
python test.py --img 640 --conf 0.45 --iou 0.4 --batch 1 --device 0 --data data/coco.yaml --cfg models/yolov4-csp.cfg --weights /home/jongwook95.lee/vision/Slive/ScaledYOLOv4-yolov4-csp/runs/exp7/weights/best.pt

(3) detect (영상)
python detect.py --conf-thres 0.4 --device 0 --weights /home/jongwook95.lee/vision/Slive/ScaledYOLOv4-yolov4-csp/runs/exp7/weights/best.pt --source /home/jongwook95.lee/vision/Slive/ScaledYOLOv4-yolov4-csp/our_data/closeshot_3.MOV --img-size 896 --cfg models/yolov4-csp.cfg