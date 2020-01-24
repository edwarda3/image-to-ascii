# Image to Ascii conversion

## Simple

The simple version simply partitions the image into distinct "blocks" which contain `x*y` number of pixels. They are normalized and then, based on a predefined mapping, are converted into a character, one per block.