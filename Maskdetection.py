from flask import Flask, render_template, request, json, redirect
# from DinoGame import rundino
# import cv2
# import pyautogui
from FaceMaskDetection import *
import numpy as np
from threading import Thread

threadToPython=None
stopThread=[True]
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def entry_point():

	return render_template('Index.html')

@app.route('/face_MaskDetection')
def face_MaskDetection():
	global threadToPython
	threadToPython=Thread(target=faceMaskDetection,args=(stopThread,))
	threadToPython.start()
	url='Index2.html'
	return render_template(url)

@app.route('/thank_you')
def thank_you():
	# global threadToPython
	# threadToPython.deamon()
	stopThread[0]=False
	url='Thanks.html'
	return render_template(url)
if __name__ == '__main__':
	app.run(debug=True, port=8000)
