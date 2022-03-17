# Introduction:

This project is served for my better understanding about the structure of Unet:

<ul>
  <li>The dataset is the images taken from the drone.</li>
  <li>I hope someday, automatic delivery will become true and I would be able to replicate one.</li>
  <li>In my project, I don't use any pre-trained model.</li>
  <li>You can look at the structure of the model inside "Unet" folder.</li>
</ul>

# Data handling:

I download the dataset from Kaggle: https://www.kaggle.com/bulentsiyah/semantic-drone-dataset

Because this is a personal project, so the scale of the dataset is not so large (only 400 images) but each image has its own incredible resolution (4000x6000). However, I resize the image to 200x300 (because the original resolution cannot be handled with my free GPU).

The structure of the Dataset:

```
dataset -- semantic_drone_dataset -- label_images_semantic
                     |
                     | ------------- original_images
```

<ul>
  <li>The folder "label_images_semantic" contains grayscale ground truth masks.</li>
  <li>The folder "original_images" contains the input images (which make me hate "high resolution" for the first time)</li>
</ul>

The image and its correspond ground truth mask have the same file name (but different folder path though), and:

- The extension of the input image is ".jpg"
- The extension of the mask is ".png"

