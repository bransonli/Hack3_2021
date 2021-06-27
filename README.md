# Hack3_2021

## Inspiration

There are countless people dying from covid, yet there are people still people who still continue to improperly wear mask or not wear any at all just for the sake of being comfortable. We have seen people who wear masks half-hardheartedly by exposing their nose or even their mouth. We’ve seen the growing trend of mask detection algorithms, but it always seem exploitable by the people who wear mask in the wrong way. So we decided to give it an upgrade. 

## What it does

ElonMask is an api that not only detects people whom doesn’t wear masks but those who don’t wear it properly as well. This increased complexity in the software may allow public surveillance systems to have stricter implementation of mask regulations. 

## Contribution

This project is made during Hack3 2021. Team members consisting of Aaron Li, and Paarth Bathla.

## how we built it

This software is mainly consisting of mask detection, mouth detection, and nose detection. The mouth and nose detection is made mainly using OpenCV’s cascade classifier. While mask detection is made using a TensorFlow model. After building these components, we proceed to integrate them through using python modules. During these time we also had to do some data processing, to make sure the compatibility of the data through out these different components. This software is highly dependent on Tensorflow, and OpenCV. 

## Challenges we ran into

The first challenge we ran into was the time strain modelling, training, and finding datasets will have on us. In order to lessen the risk of not being able to finish, we decided to use pre trained models and pre made cascade classifiers to lesson our time. 

The second challenge we ran into was the learning curve with openCV since both of us aren’t that comfortable with it yet. But we eventually came to have a functional understanding of it, with the help of mentors. 

The third challenge we ran into was processing the data. Because the mask detection model is constructed using a specific input dimension, all the other were suppose to follow that dimension. This was pretty hard because we had to do quite a lot of trial and error in order to find out how to pass OpenCV’s image data into tensorflow tensors. But eventually we found out how. 

The fourth challenge was polishing the software. One of which is the algorithm to detect face masks. This was a little bit challenging because I had to find out how to process the model’s confidentiality levels in order to determine which prediction we should go for. Another one is the data we use to validate the software. Since there wasn’t any pre processing with the target’s background, features in the background often mistake the algorithm and make the wrong choice. I had to take pictures where the background is plain to reduce these types of error. But of course I also gotta admit, this is one of the limitations of our algorithm. Perhaps someday we could add background removal processes in the software as well. 

The last challenge is the hardware limitations. Both of us uses laptop and some of it were close to minimum specs. Looping this various algorithms will often take time, and this has resulted into very laggy live interactions and even videos. We resorted into using image as our input for demonstration. But we also provide video and live input codes for those that has the capability to run it. 

## Accomplishment

We were able to integrate different technologies to make a software we think can be beneficial to the society.

We were able to overcome challenges mentioned previously regarding learning curves and hardware limitations.

Able to use our interest of machine learning to create a practical project.

## What we learned

Integrating OpenCV with tensorflow

Learning how to use OpenCV (data processing, using Cascadeclassifiers)

Learning how to use Tensorflow (data processing, using pre-trained models)

Learning how to process data

## What’s next

Putting our software into affordable but capable hardware.

Propose to local government for the implementation of this technology

## Dependencies

Tensorflow

Keras

Matplotlib

PIL

CV2

Numpy
