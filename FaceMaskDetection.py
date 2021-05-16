import tensorflow.keras
import cv2
import numpy as np
import os
import time
from gtts import gTTS

def faceMaskDetection(stopThead):
	cap= cv2.VideoCapture(0)

	cap.set(cv2.CAP_PROP_FRAME_WIDTH,244)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT,244)


	np.set_printoptions(suppress=True)

	data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

	shape = (224, 224)

	# Load the model
	model = tensorflow.keras.models.load_model('keras_model.h5')


	while stopThead[0]:
		time.sleep(0.5)
		
		_, frame=cap.read()
		frame=cv2.resize(frame,shape)

		normalized_frame=(frame.astype(np.float32) / 127.0) - 1

		data[0] = normalized_frame

		prediction = model.predict(data)

		if prediction[0][0]>prediction[0][1]:
			print("Mask")
		else:
			os.system("afplay ./noMask.mp3")


if __name__ == '__main__':
	faceMaskDetection([True])


