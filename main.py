import cv2;
import mediapipe as md;

md_drawing=md.solutions.drawing_utils;
md_drawing_styles=md.solutions.drawing_styles;
md_pose=md.solutions.pose;

pushupCount=0;

position =None;
cap=cv2.VideoCapture(0);
with md_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        sucess,image=cap.read();
        if not sucess:
            print("NULL");
            break;
        image=cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB);
        res=pose.process(image);

        reslist=[];  

        if res.pose_landmarks : 
            md_drawing.draw_landmarks(
                image,res.pose_landmarks,md_pose.POSE_CONNECTIONS
            )
            for id,im in enumerate(res.pose_landmarks.landmark) :
                h,w,_=image.shape
                X,Y=int(im.x * w),int(im.y*h);
                reslist.append([id,X,Y]);
                
        if len(reslist)!=0: 
            if ((lmList[12][2] - lmList[14][2])>=15 and (lmList[11][2] - lmList[13][2])>=15):
                position = "down"
            if ((lmList[12][2] - lmList[14][2])<=5 and (lmList[11][2] - lmList[13][2])<=5) and position == "down":
                position = "up"
                count +=1 
                print(count)
            
        cv2.imshow("Counter",cv2.flip(image,1));
        key=cv2.waitKey(1);
        if key==ord('q'):
            break;
cap.release();
