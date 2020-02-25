# -*- coding:UTF-8 -*-
import os
from PIL import Image, ImageChops


class ImageDiff(object):
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = os.path.abspath(os.path.dirname(os.getcwd()))

    def diff_images(self, one, two, different):
        """
        此模块可以进行 UI 界面对比;
        one: 第一张图片的名称
        two: 第二张图片的名称
        different: 生成对比图保存名称
        """
        img_one = self.file_path + '/new_images/' + one + 'png'
        img_two = self.file_path + '/old_image/' + two + 'png'
        img_diff = self.file_path + '/diff_image/' + different + 'png'
        image_one = Image.open(img_one)
        image_two = Image.open(img_two)
        one_data = list(image_one.getdata())
        two_data = list(image_two.getdata())

        if one_data == two_data:
            pass
        elif one_data != two_data:
            diff = ImageChops.blend(image_one, image_two, alpha=0.5)
            diff.save(img_diff)
