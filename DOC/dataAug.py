#!/usr/bin/env python
#-*- coding: utf-8 -*-

# import packages
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode='nearest',
    rescale=1/255
)

img = load_img('humpheadwrasse/humpheadwrasse005.png')  # this is a PIL image, please replace to your own file path
x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory

i = 0
for batch in datagen.flow(x, batch_size=1, save_to_dir='humpheadwrasse_crops', save_prefix='humpheadwrasse005', save_format='png'):
    i += 1
    if i > 30:
        break  # otherwise the generator would loop indefinitely