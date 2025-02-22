import cv2
from deepface import DeepFace

def captureImage():
    #Creating a video capture object
    cap_obj=cv2.VideoCapture(0)
    print("captured:", type(cap_obj))

    #checking if camera is opened successfully
    if not cap_obj.isOpened():
        print("camera failure")
        exit()

    #capturing a frame from the object
    ret, frame=cap_obj.read()

    #display frame
    if ret:
        cv2.imshow ('captured frame', frame)
    else:
        print("frame capture failed")
        cap_obj.release()
        exit()

    #releasing the camera
    cap_obj.release()
    cv2.waitKey (0)
    cv2.destroyAllWindows()

    return frame
    
