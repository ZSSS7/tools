import cv2
import os
import numpy as np



def chazhi(gt_path,img_path,save_path):
    gt_list = os.listdir(gt_path)
    img_list = os.listdir(img_path)

    for i in gt_list:
        gt = cv2.imread(gt_path+'/'+i,cv2.IMREAD_GRAYSCALE).astype(np.int32)
        img = cv2.imread(img_path+'/'+i,cv2.IMREAD_GRAYSCALE).astype(np.int32)
        chazhi  = abs(img-gt)
        cv2.imwrite(save_path+'/'+i,chazhi)





if __name__ =='__main__':
    gt_path = ''
    img_path = ''
    save_path = ''
    chazhi(gt_path,img_path,save_path)


#def chazhi(gt_path,img_path,save_path):





