import xml.etree.ElementTree as ET
from glob import glob
import shutil
import csv
from os.path import basename, splitext, join
# from PIL import Image, ImageFont, ImageDraw, ImageEnhance


def read_bboxes_from_xml(xml_fpath):
    '''
    reads bbox information from xml file
    :return: bbox info.
    '''

    root = ET.parse(xml_fpath).getroot()
    rows = []
    img_name = splitext(basename(xml_fpath))[0] + ".jpg"
    for object_node in root.findall('object'):
        label = "busy" if object_node.find('name').text == "car" else "free"
        xmin = int(object_node.find('bndbox/xmin').text)
        ymin = int(object_node.find('bndbox/ymin').text)
        xmax = int(object_node.find('bndbox/xmax').text)
        ymax = int(object_node.find('bndbox/ymax').text)
        rows.append([img_name, xmin, ymin, xmax, ymax, label])
    return rows


def save_imgs_and_write_data_to_csv(all_imgs_locs):
    with open('../data.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(['image_id', 'xmin', 'ymin', 'xmax', 'ymax', 'label'])
        for row in all_imgs_locs:
            csv_writer.writerow(row)


def generate_csv():
    xml_files = glob("/home/anton/Workspace/Hackathons/jio_parking_challenge_a3/All_dataset/Annotated/*.xml")
    #img_files = glob("/home/anton/Workspace/Hackathons/jio_parking_challenge_a3/All_dataset/Annotated/*.jpg")
    base_dir_path = "/home/anton/Workspace/Hackathons/jio_parking_challenge_a3/All_dataset/Annotated"

    all_parking_locs=[]
    for xml_file in xml_files:
        img_name = splitext(basename(xml_file))[0] + ".jpg"
        img_fpath = join(base_dir_path, img_name)
        img_parking_locs = read_bboxes_from_xml(xml_file)
        if len(img_parking_locs) != 0:
            all_parking_locs.extend(img_parking_locs)
            dest_path = join("../images", img_name)
            shutil.copy(img_fpath, dest_path)

    save_imgs_and_write_data_to_csv(all_parking_locs)

    # xml_fpath = "/home/anton/Workspace/Hackathons/jio_parking_challenge_a3/Annotated/dataset_6_image_9.xml"
    # read_bboxes_from_xml(xml_fpath)


def main():
    generate_csv()


if __name__ == "__main__":
    generate_csv()
