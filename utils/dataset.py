import numpy as np
import torch
from torch.utils.data import Dataset
import cv2
import os


class BasicDataset(Dataset):
    def __init__(self, imgs_dir, masks_dir):
        self.images = []
        self.masks  = []

        show_size = True

        for file in os.listdir(imgs_dir):
            img  = cv2.imread(imgs_dir  + '/' + file[:-4] + '.jpg')
            mask = cv2.imread(masks_dir + '/' + file[:-4] + '.png', cv2.IMREAD_GRAYSCALE)

            if (not np.any(mask)):
                continue
            
            img  = cv2.resize(img,  dsize = (300, 200), interpolation = cv2.INTER_AREA)
            mask = cv2.resize(mask, dsize = (300, 200), interpolation = cv2.INTER_AREA)

            self.images.append(img)
            self.masks.append(mask)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, i):
        img  = self.images[i].transpose((2, 0, 1))
        mask = self.masks[i]

        img  = torch.from_numpy(img).type(torch.FloatTensor)
        mask = torch.from_numpy(mask).type(torch.FloatTensor)

        return img, mask