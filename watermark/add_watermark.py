#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time:2020/4/9 20:41
# @Author:李阳
import os

from PIL import Image, ImageDraw, ImageFont


def _add_text_to_image(image, text):
    # 选择加水印的字体
    font = ImageFont.truetype(r'/System/Library/Fonts/Supplemental/Songti.ttc', 36)

    # 添加背景
    new_img = Image.new('RGBA', (image.size[0] * 3, image.size[1] * 3), (0, 0, 0, 0))
    new_img.paste(image, image.size)

    # 添加水印
    font_len = len(text)
    rgba_image = new_img.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    for i in range(0, rgba_image.size[0], font_len * 40 + 100):
        for j in range(0, rgba_image.size[1], 200):
            image_draw.text((i, j), text, font=font, fill=(0, 0, 0, 50))
    text_overlay = text_overlay.rotate(45)
    image_with_text = Image.alpha_composite(rgba_image, text_overlay)

    # 裁切图片
    image_with_text = image_with_text.crop((image.size[0], image.size[1], image.size[0] * 2, image.size[1] * 2))
    return image_with_text


def add_watermark(input_dir, mark):
    if not os.path.exists(input_dir + '/results'):
        os.mkdir(input_dir + '/results')
        print('文件夹创建成功！')
    else:
        print('文件夹已存在！')
    imgs = os.listdir(input_dir)
    length = len(imgs)

    for i in range(1, length):
        if os.path.isfile(input_dir + '/' + imgs[i]):  # 判断是否是文件
            img = Image.open(input_dir + '/' + imgs[i])
            img_name = os.path.splitext(imgs[i])[0]
            img_logo = _add_text_to_image(img, mark)
            img_logo.save(input_dir + '/results/' + img_name + '_logo.png')

    print('水印添加完成！')


if __name__ == '__main__':
    add_watermark('/Users/huangyan/Desktop/before', '我爱你中国')
