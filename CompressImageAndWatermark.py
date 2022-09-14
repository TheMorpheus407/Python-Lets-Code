import PIL
from PIL import Image, ImageFont, ImageDraw


def save_compressed(img):
    img.save("./imgs/thumb.jpg", "JPEG", optimize=True, quality=80) #1080, JPG


def watermark(img):
    watermarked = ImageDraw.Draw(img)
    watermarked.text((5, 2), "The Morpheus")
    watermarked.bitmap((12, 9), Image.open("./imgs/MO-logo_quadratisch.png").resize((50, 50)))



if __name__ == "__main__":
    img = Image.open("./imgs/anonymous-438427_640.jpg")
    watermark(img)
    save_compressed(img)
