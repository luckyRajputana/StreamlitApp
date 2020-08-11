# Industrial Steel Defect Detection

This application takes the steel image and mark the defected patch on the image with defect type mentioned on it.
Each image may have no defects, a defect of a single class, or defects of multiple classes. For each image you must segment defects of each class (ClassId = [1, 2, 3, 4]). [Steel defect detection](https://github.com/luckyRajputana/Steel-Defect-Detection).

# Files
train_images/ - folder of training images
test_images/ - folder of test images (you are segmenting and classifying these images)
train.csv - training annotations which provide segments for defects (ClassId = [1, 2, 3, 4])
sample_submission.csv - a sample submission file in the correct format; note, each ImageId 4 rows, one for each of the 4 defect classes


### My Social Connect?

Portfolio :  [Portfolio](https://luckyportfolio.herokuapp.com/portfolio/).
Linkdin   : [![Foo](https://img.icons8.com/bubbles/100/000000/linkedin.png)](www.linkedin.com/in/luckychauhan14994)
Github    :  [![Foo](https://img.icons8.com/bubbles/100/000000/github.png)](https://github.com/luckyRajputana?tab=repositories)


### Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)