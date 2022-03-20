# import os
# import glob
# import pandas as pd
# import xml.etree.ElementTree as ET


# def xml_to_csv(path):
#     xml_list = []
#     for xml_file in glob.glob(path + '/*.xml'):
#         tree = ET.parse(xml_file)
#         root = tree.getroot()
#         for member in root.findall('object'):
#             value = (root.find('filename').text,
#                      int(root.find('size')[0].text),
#                      int(root.find('size')[1].text),
#                      member[0].text,
#                      int(member[4][0].text),
#                      int(member[4][1].text),
#                      int(member[4][2].text),
#                      int(member[4][3].text)
#                      )
#             xml_list.append(value)
#     column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
#     xml_df = pd.DataFrame(xml_list, columns=column_name)
#     return xml_df


# def main():
#     for folder in ['train','test']:
#         image_path = os.path.join(os.getcwd(), ('images/' + folder))
#         xml_df = xml_to_csv(image_path)
#         xml_df.to_csv(('images/' + folder + '_labels.csv'), index=None)
#         print('Successfully converted xml to csv.')


# main()

'''
Code obtained from
https://gist.github.com/Amir22010/a99f18ca19112bc7db0872a36a03a1ec
and
change according to the my requirements
'''

import glob
import os
import cv2
import pickle
import xml.etree.ElementTree as ET
from os import listdir, getcwd
from os.path import join


############ CONFIGURATION ############
''''
Make sure you have train, val and/or test subsets in the current directory
'''
dirs = ['Phase1'] # ['train', 'val', 'test']

'''
Name your classes exactly same as you have used in your annotation in Voc
Order is important for consistency so make sure to put in order as you want them
'''
classes = ['LAN', 'Micro-USB', 'USB', 'Audio', 'GPIO', 'ICSP', 'Crystal', 'IC', 'C', 'R', 'D', 'Switch', 'LED', 'Varistor', 'HeatSink']

'''
Image extension
'''
IMG_EXTENSION = 'jpg'

# get images from current dirctory
def getImagesInDir(dir_path):
    """Function to append all the image names in a image_list variable"""
    image_list = []
    for filename in glob.glob(dir_path + f'/*.{IMG_EXTENSION}'):
        image_list.append(filename)

    return image_list

# converstion into YOLO format
def convert(size, box):
    """size is the default image size --> defaulted to 640 x 640 other wise when size is 0 then division by 0 error was coming"""
    # if size[0] == 0:
    #     size = (640, 640)
    # if size[1] == 0:
    #     size = (640, 640)
    
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x, y, w, h)

def convert_annotation(dir_path, output_path, image_path):
    basename = os.path.basename(image_path)
    basename_no_ext = os.path.splitext(basename)[0]

    in_file = open(dir_path + '/' + basename_no_ext + '.xml')
    out_file = open(output_path + basename_no_ext + '.txt', 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    if (w == 0) or (h == 0):
        img = cv2.imread(image_path)
        w, h= img.shape[0], img.shape[1]
        # print(img.shape[:2])


    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

if __name__=='__main__':
    # current directory path
    cwd = getcwd()

    # start conversion for each subsets (train, val and test) or any other name you can give
    for dir_path in dirs:
        full_dir_path = cwd + '/' + dir_path
        output_path = full_dir_path +'/yolo_annotations/'

        # Creating a directory named yolo_annotations inside the subset directory
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Getting the image list
        image_paths = getImagesInDir(full_dir_path)
        list_file = open(full_dir_path + '.txt', 'w')

        # Looping on each image inside the list
        for image_path in image_paths:
            list_file.write(image_path + '\n')
            convert_annotation(full_dir_path, output_path, image_path)
            print(f"{image_path} Converted!")
        list_file.close()

        print(f"{dir_path} Subset Conversion Completed!")
