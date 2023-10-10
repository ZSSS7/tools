import cv2
import os

def create_video(image_folder1, image_folder2, image_folder3, output_video):
    # 获取图片文件夹中的所有图片文件
    images1 = sorted(os.listdir(image_folder1))
    images2 = sorted(os.listdir(image_folder2))
    images3 = sorted(os.listdir(image_folder3))

    # 获取图片尺寸
    image1 = cv2.imread(os.path.join(image_folder1, images1[0]))
    image2 = cv2.imread(os.path.join(image_folder2, images2[0]))
    image3 = cv2.imread(os.path.join(image_folder3, images3[0]))
    height, width, _ = image1.shape

    # 设置视频编码器和输出视频对象
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter(output_video, fourcc, 30.0, (3 * width, height))

    # 逐帧将图片写入视频
    for i in range(len(images1)):
        frame1 = cv2.imread(os.path.join(image_folder1, images1[i]))
        frame2 = cv2.imread(os.path.join(image_folder2, images2[i]))
        frame3 = cv2.imread(os.path.join(image_folder3, images3[i]))
        combined_frame = cv2.hconcat([frame1, frame2, frame3])
        video.write(combined_frame)

    # 释放视频对象
    video.release()

    print("视频制作完成！")

# 输入图片文件夹路径和输出视频路径
image_folder1 = '/home/shuaizhang/gaussian-splatting-main2/output/30/test/ours_30000/gt'
image_folder2 = '/home/shuaizhang/gaussian-splatting-main2/output/30/test/ours_30000/renders'
image_folder3 = '/home/shuaizhang/gaussian-splatting-main2/chazhitu2'
output_video = "output.mp4"

# 调用函数创建视频
create_video(image_folder1, image_folder2, image_folder3, output_video)