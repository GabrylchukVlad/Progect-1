from PIL import Image

def run_pillow():
    img = Image.new("RGB", (100, 100), color="red")
    print("[Pillow] Створено зображення розміром:", img.size, "формат:", img.format)
