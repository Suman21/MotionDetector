import cv2,numpy,time,os,fnmatch
from pygame import mixer
import playsound
#################--Delete Past Images--#############
listOfFiles = os.listdir('./capturedImages')       #
pattern = "*"                                      #
files=[]                                           #
mixer.init()                                       #
for entry in listOfFiles:                          #
    if fnmatch.fnmatch(entry, pattern):            #
            os.remove('./capturedImages/'+entry)   #
####################################################

mixer.init() #Load mixer for play music

video=cv2.VideoCapture(0)
check1, frame1=video.read()
threshold=830000 
c=0
while True:
    check2, frame2=video.read()
    numberOfNonzeros=numpy.count_nonzero(cv2.absdiff(frame1,frame2))
    frame1=frame2
    if(threshold<numberOfNonzeros):
        print("Detected:"+str(c))
        millis = int(round(time.time() * 1000))
        cv2.imwrite('./capturedImages/'+str(millis)+'.jpg', frame1)
        mixer.music.load('./alarmTone/toneOne.mp3')
        mixer.music.play(start=1.56)
        c=c+1
    
video.release()
