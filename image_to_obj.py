import sys

import cv2 as cv
import mediapipe as mp
import numpy as np


# conveting image to .obj file
def image_to_obj(image: np.mat, obj_path: str) -> None:
    # mediapipe config
    mp_pose = mp.solutions.pose
    with mp_pose.Pose(
            static_image_mode=True,
            model_complexity=2,
            enable_segmentation=True,
            min_detection_confidence=0.8) as pose:

        # conveting the image to RGB before processing
        results = pose.process(cv.cvtColor(image, cv.COLOR_BGR2RGB))

        if results.pose_landmarks:
            lndmrk = results.pose_landmarks.landmark
            # translating and rotating points to bring the subject to origin
            nose = (lndmrk[mp_pose.PoseLandmark.NOSE].x,
                    lndmrk[mp_pose.PoseLandmark.NOSE].y,
                    lndmrk[mp_pose.PoseLandmark.NOSE].z)
            left_foot_index = (lndmrk[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].x,
                               lndmrk[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].y,
                               lndmrk[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].z)
            right_foot_index = (lndmrk[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].x,
                                lndmrk[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].y,
                                lndmrk[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].z)

            lowest_point = left_foot_index if left_foot_index[1] > right_foot_index[1] else right_foot_index

            vertices = {}
            _ = 1
            # writing vertices
            with open(obj_path, 'w') as export:
                export.write('o face\nmtllib face.mtl\n\n# Vertices\n')
                for id, lm in enumerate(lndmrk):
                    x, y, z = (lm.x - nose[0]) * 100, (-lm.y + lowest_point[1]) * 100, (-lm.z + lowest_point[2]) * 100*0.3

                    # saving vertices for future
                    vertices[_] = (x, y, z)
                    _ = _ + 1
                    export.writelines('v ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n')

                # writing uv
                export.write('\n\n#UV\n')
                for vertex in vertices.values():
                    export.writelines('vt ' + str(vertex[0]) + ' ' + str(vertex[1]) + '\n')

                # writing faces
                export.write('\n\n#Faces\n')
                for conn in mp_pose.POSE_CONNECTIONS:
                    export.writelines('f ' + str(conn[0] + 1) + ' ' + str(conn[1] + 1) + '\n')


# driver code
if __name__ == "__main__":
    img_path, obj_path = sys.argv[1], sys.argv[2]
    img = cv.imread(img_path)

    image_to_obj(img, obj_path)
