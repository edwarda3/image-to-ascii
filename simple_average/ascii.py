from PIL import Image
import os
import sys

PIXELS_PER_COL = 2
PIXELS_PER_ROW = 4

# This dict carries the mappings of darkness_ratio to character.
# For any ratio (where 0 is darkest), use the key that is the next highest.
# ex. if my block had a ratio of .34, then use the .4 key, '੦'.
ratio_to_char_dict = {
    .1:' ',
    .2:'◌',
    .3:'·',
    .4:'◦',
    .5:'▪',
    .6:'੦',
    .7:'◎',
    .8:'▣',
    .9:'▩',
    1.:'▒'
}

def get_value_of(val, darkest=255):
    keys_list = list(ratio_to_char_dict.keys())
    keys_list.sort()
    for k in keys_list:
        if(val/darkest < k):
            return ratio_to_char_dict[k]

image_path = os.path.join(os.getcwd(), sys.argv[1])
im = Image.open(image_path)
pix = im.load()

(im_width, im_height) = im.size
a_im_rows = im_height // PIXELS_PER_ROW
a_im_cols = im_width // PIXELS_PER_COL
# This matrix contains 1 float value for every block, where every block represents (PIXELS_PER_COL*PIXELS_PER_ROW) number of pixels.
total_darkness_matrix = [[0 for _ in range(a_im_cols+1)] for _ in range(a_im_rows+1)]

# max_color_value is the maximal value that the block can have. this is just if all belonging pixels are maxed (255). Used for normalizing later.
max_color_value = 255 * (PIXELS_PER_ROW*PIXELS_PER_COL)

# For every pixel, add its value to its respective bucket/block. (PIXELS_PER_COL*PIXELS_PER_ROW) number of pixels will be added to each block.
for pixel_row in range(im_height):
    for pixel_col in range(im_width):
        avg_val = sum(pix[pixel_col,pixel_row])/3
        total_darkness_matrix[pixel_row//PIXELS_PER_ROW][pixel_col//PIXELS_PER_COL] += avg_val

# Build the string from each of the blocks. Each block is one character.
s = ''
for i,row in enumerate(total_darkness_matrix):
    for j,val in enumerate(row):
        s += get_value_of(val, darkest=max_color_value)
    s+= '\n'

print(s)
        