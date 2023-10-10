

import cv2
import os
from pathlib import Path


def fanzhuan(image_path,save_path):
    imagelist = os.listdir(image_path)
    print(imagelist)
    imagelist2 = []
    for i in imagelist:
        if(Path(i).suffix =='.png'):
            imagelist2.append(i)
    #print(len(imagelist2))
    for i in imagelist2:
        img = cv2.imread(image_path+i)
        img2 = 255-img
        cv2.imwrite(save_path+i,img2)










if __name__ == '__main__':
    image_path = ''
    save_path = ''
    fanzhuan(image_path,save_path)



