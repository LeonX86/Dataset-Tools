import glob
import random
import os
import shutil
#可以改写一下生成路径
# Get all paths to your images files and text files
PATH = 'C:\Fake\E\Code\Python\GameHelper\yolov5\data\myData/'#多写一层
img_paths = glob.glob(r"C:\Fake\E\Code\Python\GameHelper\yolov5\data\myData\images\*.png")
txt_paths = glob.glob(r"C:\Fake\E\Code\Python\GameHelper\yolov5\data\myData\labels\*.txt")

# Calculate number of files for training, validation
data_size = len(img_paths)
r = 0.8
train_size = int(data_size * 0.8)

# Shuffle two list
img_txt = list(zip(img_paths, txt_paths))
random.seed(43)
random.shuffle(img_txt)
img_paths, txt_paths = zip(*img_txt)

# Now split them
train_img_paths = img_paths[:train_size]
train_txt_paths = txt_paths[:train_size]

valid_img_paths = img_paths[train_size:]
valid_txt_paths = txt_paths[train_size:]

# Move them to train, valid folders
train_folder = PATH+'train/'
valid_folder = PATH+'valid/'
os.mkdir(train_folder)
os.mkdir(valid_folder)

def move(paths, folder):
    for p in paths:
        shutil.move(p, folder)

move(train_img_paths, train_folder)
move(train_txt_paths, train_folder)
move(valid_img_paths, valid_folder)
move(valid_txt_paths, valid_folder)
