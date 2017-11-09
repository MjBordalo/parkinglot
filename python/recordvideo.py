# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


#blabla22323423wewrwr1231231231weqweqweqw

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
camera.hflip = True
camera.vflip = True
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 32, (640,480))

# capture frames from the camera
last_time=0
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
	now_time =int(time.time())
	# if (now_time % 1==0 & last_time != now_time ):
	# 	last_time = now_time
	time.sleep(1)
	print "frame plote "+ str(now_time)
	out.write(image)

	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break


out.release()

cv2.destroyAllWindows()
