import cv2
from deepface import DeepFace



# Function for face verification
def verify_faces(cap_img, images):
    print("entering verification")
    cv2.imshow("reference",cap_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    for img in images:
        print("here are your stored images: ")
        cv2.imshow("ref_img", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if DeepFace.verify(cap_img, img)['verified']:
            face_matched = True
            print("face matched in verify  function")
            break
        else:
            face_matched = False
            print("face not matched")
    print("returning value into verify function",face_matched)
    return face_matched
