import copy
import numpy as np
import cv2 as cv
from fastseg import MobileV3Small
from fastseg.image import colorize
import torch
from fastai.data.transforms import get_image_files
from fastai.vision.data import SegmentationDataLoaders
from fastai.vision.all import Learner, load_learner
from fastai.metrics import DiceMulti

# https://www.kaggle.com/code/thomasfermi/fastai-sample-solution


def ld_detection_overlay(image, left_mask, right_mask):
    res = copy.copy(image)
    res[left_mask > 0.3, :] = [0, 0, 255]
    res[right_mask > 0.3, :] = [255, 0, 0]
    return res


def get_pred_for_mobilenet(model, img):
    with torch.no_grad():
        image_tensor = img.transpose(2, 0, 1).astype("float32") / 255
        x_tensor = torch.from_numpy(image_tensor).to("cuda").unsqueeze(0)
        model_output = (
            torch.nn.functional.softmax(model.forward(x_tensor), dim=1).cpu().numpy()
        )
        return model_output


def label_func(img):
    return (
        f"/media/nevin/Trash Games1/selfdrive/train_label/{img.stem}_label{img.suffix}"
    )


if __name__ == "__main__":
    model_file = "/media/nevin/Trash Games1/selfdrive/model.pth"
    # print("initializing dataset (fastai is dumb for needing this)")
    # train_images = get_image_files("/media/nevin/Trash Games1/selfdrive/train")

    # codes = ["nothing", "left", "right"]

    # dls = SegmentationDataLoaders.from_label_func(
    #     path="/media/nevin/Trash Games1/selfdrive",
    #     bs=4,
    #     fnames=train_images,
    #     label_func=label_func,
    #     codes=codes,
    # )

    print("initializing model")
    # model = MobileV3Small(num_classes=3, use_aspp=True)
    learner = load_learner(model_file)
    learner.cuda()
    print(learner)

    torch.save(learner.model, "/home/nevin/Desktop/model.pt")
    learner.model.eval()
    # print(learner.state_dict())
    print("done initializing model")

    cap = cv.VideoCapture("0.hevc")

    while True:
        ret, frame = cap.read()

        if ret != True:
            break

        # value = learner.predict_one(frame)
        # print(value.shape)
        back, left, right = get_pred_for_mobilenet(learner.model, np.asarray(frame))[0]
        value = ld_detection_overlay(frame, left, right)
        # print(value[0].shape)
        # value = learner.predict(frame)
        # value = np.asarray(value[0].cpu())

        # value = value.astype(np.uint8)

        # value[value == 2] = 100
        # value[value == 1] = 255

        cv.imshow("frame", np.asarray(value))

        key = cv.waitKey()

        if key == 113:
            break
