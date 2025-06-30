import random
from PIL import Image

colors = {
    "light_green": (136, 204, 136),
    "dark_green": (51, 102, 51),
    "light_yellow": (255, 255, 153),
    "dark_yellow": (204, 204, 51)
}

def get_random_color():
    return random.choice(["light_yellow", "dark_yellow"]) if random.random() < 0.25 else random.choice(["light_green", "dark_green"])

img = Image.new("RGB", (180, 180))
pixels = img.load()

for i in range(180):
    for j in range(180):
        pixels[i, j] = colors[get_random_color()]

img.save("terrain_texture_zup_90x90.png")
print("✅ Texture saved as: terrain_texture_zup_90x90.png")
