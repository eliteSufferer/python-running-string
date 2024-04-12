import os
from django.conf import settings
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


def generate_video(text, duration, font_size, background_color, output_path):
    width = 100
    height = 100
    fps = 24

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    num_frames = int(fps * duration)

    font_path = os.path.join(settings.BASE_DIR, 'static', 'FreeSans.ttf')
    font = ImageFont.truetype(font_path, font_size)

    temp_image = Image.new('RGB', (1, 1))
    temp_draw = ImageDraw.Draw(temp_image)
    text_width = temp_draw.textlength(text, font=font)

    text_x = width
    text_y = int((height - font_size) / 2)

    speed = (text_width + width) / (duration * fps)

    for i in range(num_frames):
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        frame[:] = background_color
        frame_pil = Image.fromarray(frame)
        draw = ImageDraw.Draw(frame_pil)

        draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255))

        frame = np.array(frame_pil)

        text_x -= speed
        if text_x < -text_width:
            text_x = width

        video_writer.write(frame)

    video_writer.release()
