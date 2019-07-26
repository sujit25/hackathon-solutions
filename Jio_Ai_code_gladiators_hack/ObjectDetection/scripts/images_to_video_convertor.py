import cv2
from glob import glob


def generate_video(img_fpaths,video_filename):

    img_arrs = [cv2.imread(img_fpath) for img_fpath in img_fpaths]
    height, width, layers = img_arrs[1].shape
    # video = cv2.VideoWriter('{}.avi'.format(video_filename), -1, 1, (width, height))
    video = cv2.VideoWriter('{}.avi'.format(video_filename), cv2.VideoWriter_fourcc(*'DIVX'), 2, (width, height))
    for img_arr in img_arrs:
        video.write(img_arr)
    video.release()


def get_imgs_for_camera(cam_mask_path):
    return [img for img in glob(cam_mask_path)]


if __name__ == '__main__':
    cam1_mask_path = "/home/anton/Workspace/Hackathons/jio_car_parking_challenge/data/dataset1/CNR-EXT_FULL_IMAGE_1000x750/FULL_IMAGE_1000x750/*/*/camera1/*.jpg"
    cam2_mask_path = "/home/anton/Workspace/Hackathons/jio_car_parking_challenge/data/dataset1/CNR-EXT_FULL_IMAGE_1000x750/FULL_IMAGE_1000x750/*/*/camera2/*.jpg"
    cam3_mask_path = "/home/anton/Workspace/Hackathons/jio_car_parking_challenge/data/dataset1/CNR-EXT_FULL_IMAGE_1000x750/FULL_IMAGE_1000x750/*/*/camera3/*.jpg"
    cam4_mask_path = "/home/anton/Workspace/Hackathons/jio_car_parking_challenge/data/dataset1/CNR-EXT_FULL_IMAGE_1000x750/FULL_IMAGE_1000x750/*/*/camera4/*.jpg"
    cam5_mask_path = "/home/anton/Workspace/Hackathons/jio_car_parking_challenge/data/dataset1/CNR-EXT_FULL_IMAGE_1000x750/FULL_IMAGE_1000x750/*/*/camera5/*.jpg"
    cam6_mask_path = "/home/anton/Workspace/Hackathons/jio_car_parking_challenge/data/dataset1/CNR-EXT_FULL_IMAGE_1000x750/FULL_IMAGE_1000x750/*/*/camera6/*.jpg"
    cam7_mask_path = "/home/anton/Workspace/Hackathons/jio_car_parking_challenge/data/dataset1/CNR-EXT_FULL_IMAGE_1000x750/FULL_IMAGE_1000x750/*/*/camera7/*.jpg"
    cam8_mask_path = "/home/anton/Workspace/Hackathons/jio_car_parking_challenge/data/dataset1/CNR-EXT_FULL_IMAGE_1000x750/FULL_IMAGE_1000x750/*/*/camera8/*.jpg"
    cam9_mask_path = "/home/anton/Workspace/Hackathons/jio_car_parking_challenge/data/dataset1/CNR-EXT_FULL_IMAGE_1000x750/FULL_IMAGE_1000x750/*/*/camera9/*.jpg"

    cam1_imgs = get_imgs_for_camera(cam1_mask_path)
    cam2_imgs = get_imgs_for_camera(cam2_mask_path)
    cam3_imgs = get_imgs_for_camera(cam3_mask_path)
    cam4_imgs = get_imgs_for_camera(cam4_mask_path)
    cam5_imgs = get_imgs_for_camera(cam5_mask_path)
    cam6_imgs = get_imgs_for_camera(cam6_mask_path)
    cam7_imgs = get_imgs_for_camera(cam7_mask_path)
    cam8_imgs = get_imgs_for_camera(cam8_mask_path)
    cam9_imgs = get_imgs_for_camera(cam9_mask_path)

    sorted_cam1_imgs = sorted(cam1_imgs)
    sorted_cam2_imgs = sorted(cam2_imgs)
    sorted_cam3_imgs = sorted(cam3_imgs)
    sorted_cam4_imgs = sorted(cam4_imgs)
    sorted_cam5_imgs = sorted(cam5_imgs)
    sorted_cam6_imgs = sorted(cam6_imgs)
    sorted_cam7_imgs = sorted(cam7_imgs)
    sorted_cam8_imgs = sorted(cam8_imgs)
    sorted_cam9_imgs = sorted(cam9_imgs)

    generate_video(cam1_imgs, "camera1")
    generate_video(cam2_imgs, "camera2")
    generate_video(cam3_imgs, "camera3")
    generate_video(cam4_imgs, "camera4")
    generate_video(cam5_imgs, "camera5")
    generate_video(cam6_imgs, "camera6")
    generate_video(cam7_imgs, "camera7")
    generate_video(cam8_imgs, "camera8")
    generate_video(cam9_imgs, "camera9")


