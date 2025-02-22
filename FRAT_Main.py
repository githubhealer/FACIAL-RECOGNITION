import cv2
from deepface import DeepFace
import os
from datetime import datetime
from FRAT_importImages import getImages
from FRAT_CaptureImage import captureImage
from FRAT_AccessExcel import createTodaysFile, updateAtt

face_matched = False

def verify_faces(cap_img, images):
    global face_matched
    print("********Entering verification phase**************")
    cv2.imshow("REFERENCE", cap_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    for index, img in enumerate(images):
        print("Stored image:", index)
        cv2.imshow("Stored Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        result = DeepFace.verify(cap_img, img)

        print("Verification result:", result)
        if result['verified']:
            face_matched = True
            print("**********Image verified successfully*********")
            return index

    return -1

cap_img = captureImage()
cv2.imshow("MAIN FRAME", cap_img)
cv2.waitKey(0)
cv2.destroyAllWindows() 

ref_img = cv2.resize(cap_img, (300, 300))
images, names = getImages()
for i in names:
    print("Names of stored images: ", i)

matched_index = verify_faces(ref_img, images)

if face_matched:
    print("Matched")
    txt = names[matched_index]

    cv2.putText(ref_img, txt, (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 1)

    at_time = datetime.now()
    current_date = at_time.strftime('%d%m%y')
    fname = current_date + "Attendance.xlsx"
    print("Filename:", fname)

    if os.path.isfile(fname):
        updateAtt(fname, txt)
    else:
        createTodaysFile(fname, txt)
else:
    print("Not matched")
    cv2.putText(ref_img, "MATCH NOT FOUND", (20, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 3)

cv2.imshow("Result Image", ref_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
