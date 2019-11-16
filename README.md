# Smart mirror

Smart mirror project running on Raspberry Pi with opencv.

## Installation
```
sudo apt-get install -y libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test
sudo pip3 install Flask
sudo pip3 install opencv-python
wget "https://raw.githubusercontent.com/Mjrovai/OpenCV-Face-Recognition/master/FaceDetection/Cascades/haarcascade_frontalface_default.xml"
```

## Running
```
git clone https://gitlab.com/RaspberryPiJam/nokia-pi-jam---smart-mirror.git
cd nokia-pi-jam---smart-mirror
echo 'export LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0' >> ~/.bashrc
source ~/.bashrc
export FLASK_APP=server.py
flask run
python3 validate_face_detection.py //validate if your face is detected
python3 gather_data.py //gather your face images
python3 trainer.py //train model on your data
python3 face_recognition.py
```

## Useful commands
```
ls /dev/ | grep video
lsusb
```

## Solving problems
```
VIDEOIO ERROR: V4L2: Pixel format of incoming image is unsupported by OpenCV
Unable to stop the stream: Device or resource busy
```
`cv2.VideoCapture` is running in loop without releasing
<br/><br/>

```
Captured video is blank
```
Lack of `cv2.waitKey` method or wrong value
<br/><br/>

```
cv2.error: OpenCV(3.4.3) /home/pi/opencv-python/opencv/modules/objdetect/src/cascadedetect.cpp:1698: error: (-215:Assertion failed) !empty() in function 'detectMultiScale'
```
Xml with face recognition set is provided incorrectly
<br/><br/>

```
cv2.error: OpenCV(3.4.3) /home/pi/opencv-python/opencv/modules/core/src/persistence_c.cpp:388: error: (-49:Unknown error code -49) Input file is empty in function 'cvOpenFileStorage'
```
Content of xml file is invalid
<br/><br/>

```
AttributeError: module 'cv2.cv2' has no attribute 'face'
```
Run `python3 -m pip install opencv-contrib-python --upgrade`
