import numpy as np
import cv2 as cv
from fastseg import MobileV3Small
import torch
from fastai.data.transforms import get_image_files
from fastai.vision.data import SegmentationDataLoaders
from fastai.vision.all import Learner, load_learner
from fastai.metrics import DiceMulti


def label_func(img):
    return (
        f"/media/nevin/Trash Games1/selfdrive/train_label/{img.stem}_label{img.suffix}"
    )


if __name__ == "__main__":
    model_file = "/media/nevin/Trash Games1/selfdrive/model.pth"
    print("initializing dataset (fastai is dumb for needing this)")
    train_images = get_image_files("/media/nevin/Trash Games1/selfdrive/train")

    codes = ["nothing", "left", "right"]

    dls = SegmentationDataLoaders.from_label_func(
        path="/media/nevin/Trash Games1/selfdrive",
        bs=4,
        fnames=train_images,
        label_func=label_func,
        codes=codes,
    )

    print("initializing model")
    model = MobileV3Small(num_classes=3, use_aspp=True)
    learner = load_learner(model_file)
    print(dir(learner.model))

    # torch.save(learner.state_dict(), "/home/nevin/Desktop/model.pth")
    # print(learner.state_dict())
    print("done initializing model")

    cap = cv.VideoCapture("0.hevc")

    while True:
        ret, frame = cap.read()

        if ret != True:
            break

        value = learner.predict(frame)
        value = np.asarray(value[0].cpu())

        value = value.astype(np.uint8)

        value[value == 2] = 100
        value[value == 1] = 255

        cv.imshow("frame", value)

        key = cv.waitKey()

        if key == 113:
            break
