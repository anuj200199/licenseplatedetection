# license plate detection
 
 yolov3-tiny_obj.cfg is the architecture of yolov3-tiny.
 
 yolo-obj.cfg is yolov3 architecture
 
 yolo-obj_weights.weights is the trained weights on yolov3 architecture for license plate detection.
 
 
 
 ![training](https://user-images.githubusercontent.com/51110977/63793463-5fccc280-c91d-11e9-8970-6fe90ffdfaa8.png)

 To predict the bounding box on the image path_to_test_image.jpg with a threshold value of 0.5, run python script as

python predict.py --image path_to_image --config yolo-obj.cfg --weights yolo-obj_last.weights --classes data/obj.names
 
  ![object-detection](https://user-images.githubusercontent.com/51110977/64024647-81fe5480-cb58-11e9-8f8a-5b211f8155d6.jpg)

The above python script will return 2 images as object_detection.jpg which will be highlight the entire image with the bouding box and ing.jpg, the cropped image fetching the license plate from the entire image.

![Cropped image](https://user-images.githubusercontent.com/51110977/64024670-8fb3da00-cb58-11e9-9302-3a00865ce308.jpg)

Apply ocr.py with trying.jpg as argument obtained and get the license plate characters and digits.

![ocr](https://user-images.githubusercontent.com/51110977/64026863-339f8480-cb5d-11e9-9a0b-a182cdd411a9.PNG)

 

ALGORITHM/LIBRARY USED:
	
Json File preprocessing:
The dataset is present in a json file specifying the content , label, image width, image height, and x and y coordinates of bottom right and top left bounding box. We have to separate all the fields and store them in csv format. For this , I have used the pandas library in python. 

For Data Augmentation:
Darknet enables us to perform data augmentation by changing the saturation, hue, brightness of images inside the yolo-tiny-obj.cfg which contains the architecture of our mode. For more information please refer [2]  

For Object detection:
The main part in the case of object detection is to decide which of the models to use. There is a wide pool of models available to us, with variations of each model . The broad category or the widely used can be divided into YOLO(You Only Look Once), RetinaNet and SSD5 models. 

Each of the models have their own unique pros and cons. However, on reading the blog [3] by Sik-Ho Tsang which shows the comparison of various models and my preference of model selection is based on the results of [3] shown below in Fig. 5.1.

From the figure below, the best models are YOLOv3 and RetinaNet.YOLOv3 has comparable Mean Average Precision(map) time with RetinaNet. Nevertheless, the inference time is smaller than RetinaNet. Hence, I have used the YOLOv3-tiny model for object detection instead of the YOLOv3 model because YOLOv3 model requires 4 GB of GPU which is not present in my laptop.

 In developing the solution for the project, I have used Darknet which is commonly used for Object Detection. Darknet comes with a pre built architecture. I have used transfer learning on the YOLOv3-tiny model with predetermined weights using opencv for license plate detection.

![Fig. 5.1 Model Comparison](https://user-images.githubusercontent.com/51110977/63793606-a8847b80-c91d-11e9-825e-2ad4c22ea1ba.png)
	

Working of YOLO: A single image is divided into cells of predefined size(N X N). Classification using computer vision and localization are applied to each cell or grid. Each cell is represented by a set of 5 values- the class label, the center of the cell(x and y), the width and height of each cell. 

Intersection between between the ground truth and the predicted box is called Intersection over union(IOU). We define confidence as p(object)*IOU for each of the grid.

If an object is found in a cell, class label is 1 , else 0. The center coordinates and the height and width are normalized in the range (0,1). The entire process is described in the next section. For testing, it performs a Non Max Suppression.

For Optical Character Recognition:
After getting the required bounding box on the license plate, we have to generate the string containing characters and digits.

The following task is done using the library pytesseract library. For documentation refer [4].

Other Libraries:
Open cv
Pandas
PIL
urllib for web scraping
numpy




PREPROCESSING STEPS:

The data in json file is converted into a .csv format with columns for content, label, given coordinates of bounding box, image height, image width, notes and extras. It is important to note that the coordinates are in normalised form. First all the details into content, notes, extras, top left coordinates, etc and stored in a csv file. For this, run the seperate.py file.

After getting all the details in csv file, we are scraping the image from the web link. The images are saved incrementally as image(i).jpg where i is the value of i from 0 to size of data-1 and also add another column, that is the name of each image to the csv file. Run image_save.py 

The top left and bottom right coordinates are stored in normalised form in the csv file. We convert them to their unnormalised form by multiplying the x coordinate with width and y coordinate with height of the image. These four columns are added to the dataset specifying the  unnormalised coordinate values. This step is done as YOLO has a particular format for taking the input coordinates of the bounding box surronding the region of interest which is discussed in the next paragraph. Run bounding_box.py. To see the bounded box randomly on images, run draw_bounding_box.py

![Bounding box across region of interest](https://user-images.githubusercontent.com/51110977/63793660-ceaa1b80-c91d-11e9-8976-b9f14fd92f88.png)


In YOLO, we have to create a  .txt file for each image and should have the same name as the image. For each image, the txt file would contain five values - the class label, which is 0 in our case, the absolute center coordinates, x_center and y_center, and the absolute width and height of the bounding box with respect to the shape of the whole image.


![annotation format](https://user-images.githubusercontent.com/51110977/63793728-ef727100-c91d-11e9-9b48-1ec06d88395d.PNG)


Run generating_annotations_test.py
For example , bounding box of coordinates (582,274) and (700,321) with image width 806 and height 466 gets converted to :


![Fig. 6.3](https://user-images.githubusercontent.com/51110977/63793787-0b761280-c91e-11e9-835b-4a1b075708b2.PNG)


SETTING DARKNET YOLOv3:

Clone the darknet YOLOv3 architecture from [2]. Execute the following commands in command prompt to setup darknet. 

![darknet setup](https://user-images.githubusercontent.com/51110977/63793837-2052a600-c91e-11e9-9df8-2b2ffd788f81.PNG)

Copy images and their corresponding txt files in folder named obj under data. Create obj.names file specifying the class name. Under data folder, also create a obj.data file specifying the following:


![Fig. 6.5: Specifying details in obj.data file](https://user-images.githubusercontent.com/51110977/63793860-306a8580-c91e-11e9-82ae-698a18c69f9c.PNG)

Since we are dealing with only one class, we have to change the conf file specifying the YOLO architecture by setting filters at output YOLOv3 layer along with classes parameter. Set classes=1 and filters =(classes+5) *3 = 18 [2] in our case. 

TESTING:

Separate the images into train and test sets in the format shown in fig.6.5  Run split_train_test.py

![Fig. 6.5: train.txt file stored in data folder](https://user-images.githubusercontent.com/51110977/63793920-4aa46380-c91e-11e9-9b7f-dd1f9b5af53d.PNG)

Run the following command to train model

![ ](https://user-images.githubusercontent.com/51110977/63793934-5bed7000-c91e-11e9-9783-7945ed163abc.PNG)



For Linux or Mac, replace darknet.exe with ./darknet

To test on images and get the coordinates of the region of interest, run predict.py with command line arguments as image_name, architecture .cfg file, trained weight file and classes file(obj.names)

python predict.py --image path_image --config path_to_cfg --weights path_to_trained_weight --classes path_to_obj.names

Note : Give entire path to the weight and other file.


![Fig. 6.6 : Prediction of license plate.](https://user-images.githubusercontent.com/51110977/63793953-67409b80-c91e-11e9-9cae-d478370a71f3.png)



GETTING THE CHARACTERS(OCR):

Once we know the value of the coordinated of the bounding box, crop the original image to only consist the license plate instead of the whole image using PIL library. Then use tesseract to generate text from image.


![Fig. 6.7:  Tesseract on image predict.png](https://user-images.githubusercontent.com/51110977/63793979-7fb0b600-c91e-11e9-8bc9-3173baad2209.PNG)



HARDWARE REQUIREMENTS:


1 GB GPU for training on YOLOv3 tiny.
4 GB GPU for training on YOLOv3.

SOFTWARE REQUIREMENTS:

Python 3- Preferred anaconda environment
All installed libraries mentioned above
GitHub Bash
CygWin64
Tesseract-OCR


REFERENCES:

[1] Object Detection Using Gradient-Based Learning by  Yann Lecun, Patrick Haffner, Leon Bottou, Yoshua Bengio.

[2] Yolo-v3 and Yolo-v2 for Windows AlexeyAB.

[3]YOLOv3 — You Only Look Once (Object Detection Improved YOLOv2, Comparable Performance with RetinaNet, 3.8× Faster! by Sik-Ho Tsang.

[4]  Python Tesseract Mathias A Lee.

