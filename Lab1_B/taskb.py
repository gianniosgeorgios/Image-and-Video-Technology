import cv2 
import numpy as np
from matplotlib import pyplot as plt
from skimage.util import random_noise
from skimage import filters
from skimage.morphology import disk

# ----------------------Ομάδα F10 ---------------------------------------------------------
#----  Γιώργιος Γιαννιός 03116156 --- Μαρία Τσαμπάζη 03115716  ----------------------------
#------------------------------------------------------------------------------------------


#----------Ερώτημα 1------------------------------------------------------

def ResizeVideoResolution(original_video, resized_video):
    cap = cv2.VideoCapture(original_video)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    scale_percent = 50 # percent of original size
    new_width = int(width * scale_percent / 100)
    new_height = int(height * scale_percent / 100)
    dim = (new_width, new_height)
    final_cap = cv2.VideoWriter(resized_video, cv2.VideoWriter_fourcc(*'mp4v'), cap.get(cv2.CAP_PROP_FPS), dim)

    while (cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        final_cap.write(cv2.resize(frame, dim, interpolation = cv2.INTER_AREA))

    cap.release()

ResizeVideoResolution("VIRAT_S_010001_04_000583_000646.mp4", "resized_video.mp4")

#---------Ερώτημα 2----------------------------------------------------------
cap = cv2.VideoCapture("resized_video.mp4")
ret, first_frame = cap.read()
#color isn't essential for corner detection
first_frame_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY) #converts video's 1st frame to grayscale

#---------Ερώτημα 3----------------------------------------------------------

def CornerDetector(which_detector):
    plot, axs = plt.subplots(3, 3)
    i = 0
    for maxcorners in [200]:
        for quality in [0.1, 0.2, 0.3]:
            j = 0
            for mindistance in [2, 6, 8]:
                for blocksize in [4]:
                    gray_copy = first_frame_gray.copy()
                    if which_detector=="Harris":
                        harris_params = dict(maxCorners = maxcorners, qualityLevel = quality, minDistance = mindistance, blockSize = blocksize, useHarrisDetector = True)
                        first_corners = cv2.goodFeaturesToTrack(first_frame_gray, **harris_params)
                    else:
                        shitomasi_params = dict(maxCorners = maxcorners, qualityLevel = quality, minDistance = mindistance, blockSize = blocksize)
                        first_corners = cv2.goodFeaturesToTrack(first_frame_gray, **shitomasi_params)
                    for corner in first_corners:
                        x, y = corner.ravel()
                        cv2.circle(gray_copy, (x, y), 3, 255, -1)
                    axs[i][j].set_title("maxcorners:{}, quality:{}, mindistance:{}, blocksize:{}".format(maxcorners, quality, mindistance, blocksize))
                    axs[i][j].imshow(gray_copy, cmap = "gray")
                    axs[i][j].axis("off")
                    j += 1
            i += 1
                    
    if which_detector=="Harris":  
        plot.suptitle("Harris Corner Detector")
        plt.show()
    else:
        plot.suptitle("Shi-Tomasi")
        plt.show()

CornerDetector('Harris')
CornerDetector('Shi-Tomasi')


#Best result - Harris Corner Detector
harris_params = dict(maxCorners = 400, qualityLevel = 0.2, minDistance = 8, blockSize = 4, useHarrisDetector = True)
harris_corners = cv2.goodFeaturesToTrack(first_frame_gray, **harris_params)
#Best result - Shi Tomasi Corner Detector
shitomasi_params = dict(maxCorners = 200, qualityLevel = 0.3, minDistance = 8, blockSize = 4)
shitomasi_corners = cv2.goodFeaturesToTrack(first_frame_gray, **shitomasi_params)

#---------Ερώτημα 4----------------------------------------------------------

def LucasKanadeForOpticalFlow(winSize, maxLevel, criteria, cap, first_frame, prev):
    cap = cv2.VideoCapture("resized_video.mp4")
    ret, first_frame = cap.read()
    first_frame_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    color = (0, 255, 0) #green
    lk_params = dict(winSize = winSize, maxLevel = maxLevel, criteria = criteria) #Lucas-Kanade optical flow
    first_frame_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY) #for the 1st frame
    mask = np.zeros_like(first_frame)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #color is not essential for movement detection
        next, status, error = cv2.calcOpticalFlowPyrLK(first_frame_gray, gray, prev, None, **lk_params) #Lucas-Kanade sparse optical flow
        good_old = prev[status == 1] #good features prev position
        good_new = next[status == 1] #good features next position
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel() #coordinates of the new point
            c, d = old.ravel() #coordinates of the old point
            mask = cv2.line(mask, (a, b), (c, d), color, 2) #line between old and new position
            frame = cv2.circle(frame, (a, b), 3, color, -1)  #spot at the new position
        output = cv2.add(frame, mask)
        first_frame_gray = gray.copy()  # Updates previous frame
        prev = good_new.reshape(-1, 1, 2)
        cv2.imshow("sparse optical flow", output)
        #if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'): #interval between frames, user can stop the video play 
        #break
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()

#Lucas Kanade Method's best results for Harris Corner Detector
LucasKanadeForOpticalFlow((15, 15), 0, (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03), cap, first_frame, harris_corners)
#Lucas Kanade Method's best results for Shi-Tomasi Detector
LucasKanadeForOpticalFlow((15, 15), 0, (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 10, 0.03), cap, first_frame, shitomasi_corners)


#---------Ερώτημα 5----------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
#----κορμός κώδικα για ερωτήματα 5, 6, 7-------------------------------------------------------
#----τροποιούνται τα αποτελέσματα κατάλληλα, ανάλογα με το input των κλήσεων των συναρτήσεων---
#----------------------------------------------------------------------------------------------
source_input = "VIRAT_S_010001_04_000583_000646.mp4"
displacement = 0.3
frame_update = 30

def PreciseCornerDetector(first_frame_gray, harris):
    if harris:
        params = dict(maxCorners = 400, qualityLevel = 0.2, minDistance = 8, blockSize = 4, useHarrisDetector = True)
    else:
        params = dict(maxCorners = 200, qualityLevel = 0.3, minDistance = 8, blockSize = 4)
    corners = cv2.goodFeaturesToTrack(first_frame_gray, **params) #Finds the strongest corners
    return corners

def PreciseLucasKanade(video_name, harris = True, snp=False, denoise=False):
    global displacement, frame_update
    color = (0, 0, 255)
    frames = 0
    cap = cv2.VideoCapture("resized_video.mp4")
    ret, first_frame = cap.read()
    if snp==True:
     #Converting first frame to gray scale and adding noise
        first_frame_gray = (random_noise(cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY), mode = 's&p', seed = 6, amount = snpAmount(5)) * 255).astype(np.uint8)
    else:
        first_frame_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    if denoise==True:
        #Denoising with median filter
        first_frame_gray = filters.rank.median(first_frame_gray, disk(radius = 3))
    mask = np.zeros_like(first_frame)
    prev = PreciseCornerDetector(first_frame_gray, harris)
    lk_params = dict(winSize = (15, 15), maxLevel = 3, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 20, 0.03))
    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        frames += 1
        if snp==False:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            #Converting to gray scale and adding noise
            gray = (random_noise(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), mode = 's&p', seed = 6, amount = snpAmount(5)) * 255).astype(np.uint8)
        if denoise==True:
            #Denoising with median filter
            gray = filters.rank.median(gray, disk(radius = 3))
        next, status, error = cv2.calcOpticalFlowPyrLK(first_frame_gray, gray, prev, None, **lk_params)
        good_old = prev[status == 1]
        good_new = next[status == 1]
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()

            #you can also use Quasi Eucliadian Distance to measure distance between pixels
            #https://shodhganga.inflibnet.ac.in/bitstream/10603/33597/12/12_chapter4.pdf
            if np.sqrt((b - d) ** 2 + (a - c) ** 2) >= displacement: #euclidean distance
                mask = cv2.line(mask, (a, b), (c, d), color, 2)
                frame = cv2.circle(frame, (a, b), 3, color, -1)

        output = cv2.add(frame, mask)
        first_frame_gray = gray.copy()
        prev = good_new.reshape(-1, 1, 2)
        cv2.imshow("sparse optical flow", output)

        #New corners detection
        if frames == frame_update:
            frames = 0
            prev = PreciseCornerDetector(gray, harris)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()

PreciseLucasKanade("source_input", True, False, False) #Harris, no snp
PreciseLucasKanade("source_input", False, False, False) #Shi-Tomasi, no snp

#---------Ερώτημα 6----------------------------------------------------------

def snpAmount(x):
    return x/90.0 + 0.3

source_input = "VIRAT_S_010001_04_000583_000646.mp4"
PreciseLucasKanade("source_input", True, True, False) #with snp, no denoise
PreciseLucasKanade("source_input", False, True, False) #with snp, no denoise

#---------Ερώτημα 7----------------------------------------------------------

source_input = "VIRAT_S_010001_04_000583_000646.mp4"
PreciseLucasKanade("source_input", True, True, True) #with snp, denoise
PreciseLucasKanade("source_input", False, True, True) #with snp, denoise




"""
"""