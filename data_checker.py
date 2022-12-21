import os

img_dir = os.path.join(os.getcwd(), 'dataset', 'img', 'train')
annot_dir = os.path.join(os.getcwd(), 'dataset', 'annot', 'train')


for file in os.listdir(img_dir):
    count = 0
    for annot_file in os.listdir(annot_dir):
        if annot_file.split('.')[0]==file.split('.')[0]:
            count=1

    if count==0:
        print(file)