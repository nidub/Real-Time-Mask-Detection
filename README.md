# Real-Time-Mask-Detection
In this project firstly it will display html page which consist of button that will redirect to second html page that has user currently captured video stream and a stop button.
While redirecting it will start to capture the face of a user, whose output will be given by voice assistant after the prediction of user is masked or unmasked.
If you want to stop the application click on the stop button.
We have used Opencv to capture the images from the webcam, Tensorflow, Keras, Techable Machine of google to train the model, flask with html for GUI and gtts for voce assistant
Firstly the images is been trained in google techable machine and than it is exported only after it will be accurately predict the output.
With the help of gTTs voice is been recorded and in the code with the help of os package the recorded voice is been played.
Rest is the flask as backend with two GUI page which is written in html, css, and bootstrap. 
