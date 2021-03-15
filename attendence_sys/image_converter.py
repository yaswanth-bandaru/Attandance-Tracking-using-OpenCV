import cv2
import os
import shutil
from multiprocessing import Process

def vid_img_converter():
    os.chdir('Y:\\Masters_Content\\Software_development_for_AI\\Project 2\\Attendance Tracking 5\\static\\images\\Student_Images\\')
    sec = 0
    frameRate = 500
    count=1
    for dept in os.listdir():
        for year in os.listdir(os.path.join(os.getcwd(),dept)):
            for section in os.listdir(os.path.join(os.getcwd(),dept,year)):
                for name in os.listdir(os.path.join(os.getcwd(),dept,year,section)):
                    for vid in os.listdir(os.path.join(os.getcwd(),dept,year,section,name)):
                        if '.mp4' in vid:
                            vidcap = cv2.VideoCapture(os.path.join(os.path.join(os.getcwd(),dept,year,section,name),vid))
                            def getFrame(sec):
                                vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
                                hasFrames,image = vidcap.read()
                                if hasFrames:
                                    cv2.imwrite(os.path.join(os.path.join(os.getcwd(),dept,year,section,name),"image"+str(count)+".jpg"), image)
                                    if not os.path.exists(os.path.join("Y:\\Masters_Content\\Software_development_for_AI\\Project 2\\Attendance Tracking 5\\raw_images",name)):
                                        os.mkdir(os.path.join("Y:\\Masters_Content\\Software_development_for_AI\\Project 2\\Attendance Tracking 5\\raw_images",name))
                                    cv2.imwrite(os.path.join(os.path.join("Y:\\Masters_Content\\Software_development_for_AI\\Project 2\\Attendance Tracking 5\\raw_images",name),"image"+str(count)+".jpg"), image)
                                   # save frame as JPG file
                                return hasFrames
                            sec = 0
                            frameRate = 0.5 #//it will capture image in each 0.5 second
                            count=1
                            success = getFrame(sec)
                            while success:
                                count = count + 1
                                sec = sec + frameRate
                                sec = round(sec, 2)
                                success = getFrame(sec)
                            vidcap.release()
                            cv2.destroyAllWindows()
                            if not os.path.exists("Y:\\Masters_Content\\Software_development_for_AI\\Project 2\\Attendance Tracking 5\\Videos converted to jpg"):
                                os.mkdir("Y:\\Masters_Content\\Software_development_for_AI\\Project 2\\Attendance Tracking 5\\Videos converted to jpg")
                            original = os.path.join(os.path.join(os.getcwd(),dept,year,section,name),vid)
                            target = "Y:\\Masters_Content\\Software_development_for_AI\\Project 2\\Attendance Tracking 5\\Videos converted to jpg\\"+vid
                            shutil.move(original,target)
