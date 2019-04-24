# CatTransformer findet Augen / Ohren Landmarks in Katzenbildern
# und platziert eine Sonnenbrille darüber

from catutils import back_transform, mean_point, angle_between, dist_points, get_image_center
from fastai.vision import load_learner
from PIL import Image
import numpy as np

SCALING_FACTOR_GLASSES = 0.95
SCALING_FACTOR_MUSTACHE = 2


class CatTransformer:
    def __init__(self, glasses_filename, landmark_model_filename):
        self.glasses_pic = self._load_image(glasses_filename)
        self.landmark_model = load_learner(landmark_model_filename)

    def put_on_glasses(self, img: Image, orig_img: Image) -> (Image, list):
        landmarks = self._get_facial_landmarks(img)
        eye_left, eye_right = self._get_eyes(landmarks)
        ear_left, ear_right = self._get_ears(landmarks)

        glasses_pic = self.glasses_pic.copy()
        scaled_glasses = self._scale_object(ear_left, ear_right, glasses_pic, SCALING_FACTOR_GLASSES)
        shift = self._get_shift(eye_left, eye_right, scaled_glasses)
        rotated_glasses = self._rotate_object(ear_left, ear_right, scaled_glasses)

        orig_img.paste(rotated_glasses, shift, rotated_glasses)
        return orig_img, landmarks

    @staticmethod
    def _load_image(filename: str) -> Image:
        return Image.open(filename)

    def _get_facial_landmarks(self, img) -> list:
        raw_landmarks, _, _ = self.landmark_model.predict(img)
        scaled_landmarks = [back_transform(p[0], p[1], img.size[0], img.size[1]) for p in raw_landmarks.data]

        return scaled_landmarks

    @staticmethod
    def _get_eyes(landmarks: list) -> tuple:
        eye_left = landmarks[0]
        eye_right = landmarks[1]
        return eye_left, eye_right

    @staticmethod
    def _get_ears(landmarks: list) -> tuple:
        ear_left = landmarks[3]
        ear_right = landmarks[8]
        return ear_left, ear_right

    @staticmethod
    def _get_mouth(landmarks: list) -> tuple:
        return landmarks[2]

    @staticmethod
    def _scale_object(point_left: tuple, point_right: tuple, object_pic, scaling_factor) -> Image:
        dist = dist_points(point_left, point_right)
        object_size_x, object_size_y = object_pic.size

        scale = scaling_factor * dist / object_size_x

        scaled_x = int(scale * object_size_x)
        scaled_y = int(scale * object_size_y)
        scaled_size = (scaled_x, scaled_y)

        return object_pic.resize(scaled_size, resample=Image.BICUBIC)

    @staticmethod
    def _rotate_object(eye_left: tuple, eye_right: tuple, object_pic: Image) -> Image:
        object_mid = (object_pic.size[0] // 2, object_pic.size[1] // 2)
        angle_eyes = angle_between(eye_left, eye_right)

        return object_pic.rotate(-angle_eyes, expand=True, center=object_mid)

    @staticmethod
    def _get_shift(point_left, point_right, glasses_pic):
        point_mid = mean_point(point_left, point_right)
        glasses_mid = get_image_center(glasses_pic)
        return tuple(np.array(point_mid) - np.array(glasses_mid))
