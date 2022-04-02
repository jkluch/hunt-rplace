from PIL import Image, ImageOps
import requests
from io import BytesIO

img = Image.open("huntlogo.png")
img = img.resize((img.size[0] * 3, img.size[1] * 3), Image.NEAREST)

mask_url = "https://media.discordapp.net/attachments/267492253168173056/959625681141104700/mask.png"
response = requests.get(mask_url)
mask_i = Image.open(BytesIO(response.content))
# mask = Image.new("1", (3000, 3000), 0)
mask = Image.new("1", (6000, 3000), 0)
mask.paste(mask_i)
mask.paste(mask_i, (3001,0))

# 1329,459
# tl = (773 * 3, 735  * 3) # top left corner
tl = (1329 * 3, 459  * 3) # top left corner

# final_img = Image.new('RGBA', (3000, 3000))
final_img = Image.new('RGBA', (6000, 3000))
# unmasked_img = Image.new('RGBA', (3000, 3000))
unmasked_img = Image.new('RGBA', (6000, 3000))
unmasked_img.paste(img, tl)
final_img = Image.composite(final_img, unmasked_img, mask)
final_img.save("huntlogo_overlay.png")