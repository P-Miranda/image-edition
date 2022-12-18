#!/usr/bin/env python3

from PIL import Image, ImageFont, ImageDraw


def center_text_h_pos(img, font, text):
    draw = ImageDraw.Draw(img)
    return (img.width - draw.textlength(text, font)) / 2


def calc_v_font_margin(font):
    (left, top, right, bottom) = font.getbbox("a")
    return bottom - top


if __name__ == "__main__":
    print("Image Edition Program")
    original_image = Image.open("original-image.png")
    edited_image = original_image.copy()

    font = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf", 60)

    draw_image = ImageDraw.Draw(edited_image)

    text = "Top Center Text"
    h_pos = center_text_h_pos(edited_image, font, text)
    text_margin = calc_v_font_margin(font)
    draw_image.text((h_pos, text_margin), text, font=font)

    text = "Mid Center Text"
    h_pos = center_text_h_pos(edited_image, font, text)
    draw_image.text((h_pos, edited_image.height / 2), text, font=font)

    text = "Bottom Center Text"
    h_pos = center_text_h_pos(edited_image, font, text)
    draw_image.text((h_pos, edited_image.height - 60 - text_margin), text, font=font)

    edited_image.show()

    edited_image.save("edited-image.png")
