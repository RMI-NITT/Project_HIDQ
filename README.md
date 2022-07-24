# HIDQ : Hybrid Inspection Drive Quadcopter

A convertible hybrid drive quadcopter that is manually controlled to move across inaccessible places as a drone or a 4-wheeler bot using a self-transforming mechanism, equipped with camera to inspect various industrial systems and check for defects and anomalies with Machine Learning and Image Processing algorithms at the controller side.

This work was published under the title: "Pipeline inspection using self-transforming hybrid drive quad-copter" at the 7th International Conference on Computing in Engineering & Technology (ICCET 2022). Find the paper [here](https://digital-library.theiet.org/content/conferences/10.1049/icp.2022.0620)

### Contents 
- [Problem statement](#problem-statement)
- [Proposed solution](#proposed-solution)
- [Implementation](#implementation)
  - [Sprawl mechanism](#sprawl-mechanism)
  - [PED (Power Engage Disengage) mechanism](#ped-mechanism)
  - [Autonomous detection](#autonomous-detection)
- [Novelty and innovativeness](#novelty-and-innovativeness)
- [Gallery](#gallery)
  - [Drone sketch](#drone-sketch)
  - [Exploded view](#exploded-view)
  - [HIDQ bot](#hidq-bot)
  - [Self transforming mechanism](#self-transforming-mechanism)
 
--------------------------------------------------------------------------

## Problem statement
- Maintenance and inspection form a crucial part of an industry’s operation. 
- Proper checks and inspection are very much essential for efficient operation, avoid lethal consequences, to ensure safety and avoid physical damage. 
- Human physical inspection has constraints such as narrow spaces, dangerous environments and does not ensure precision and dependable results always.
- Physical inspection of systems like HVAC, pipes and other heavy machinery is difficult, takes a lot of time and will not be accurate.
- Sometimes, it may also be dangerous for humans to conduct physical inspection
- In cases of narrow or cramped spaces around/under heavy machinery, lot of manpower is required to inspect those spaces.

This project focuses on building a efficient and innovative solution to this inspection problem.

## Proposed solution
- A convertible hybrid drive quadcopter is manually controlled to move across inaccessible places as a drone or a 4-wheeler convertible using a self-transforming mechanism, equipped with a camera to inspect various industrial systems and check for defects and anomalies using Machine Learning and Image Processing algorithms at the controller side.
- Same BLDC motors power both the wheels and the propellers in each mode. A novel idea for power engaging disengaging mechanism is inherited which engages either the wheels or the propellers depending on the configuration of the robot (4-wheeler or drone) 
- Variable sprawl angle using self-locking gears to change dimension of bot to required arena/space.
- Automated crack and rust detection using integrated Image processing and Deep learning using Convolutional Neural Network
- Data processed and stored for future usage.
- The convertible bot can be used to inspect various systems of industries like chimney, ventilation systems, HVAC, pressurized tanks, boilers, or any confined space to detect for leakage, corrosion, cracks and other structural defects and anomalies.

### Block diagram
![hidq(2)](https://user-images.githubusercontent.com/63254914/145022849-699dca24-83a7-44fd-983c-b9c089ee6444.png)

----------------------

## Implementation

### Sprawl mechanism
The sprawl mechanism allows the bot to transform from a quadcopter to four wheeled differential drive bot. The sprawl angle is the relative angle between the plane of the wheels (and propellers) and the main body. When it is zero, the bot is in quadcopter mode and when the angle is sufficiently high, it can be driven as a four wheeled bot. Worm gears are used to ensure high torque ratio and self-locking mechanism when gears are inactive. Each of the worm gears on the two sides is rotated using the conical gear setup that ensures equal rotational speed but different rotational direction.

![sprawl2](https://user-images.githubusercontent.com/63254914/122222718-22f60500-ced0-11eb-9c0e-118e4ca0450a.gif)


### PED mechanism
In the previous designs of this project, both the propellers and the wheels are active throughout the runtime, and this consumes a lot of power. So, we came up with a novel power engage disengage mechanism to actuate either the propellers (quadcopter mode) or the wheels (four wheeled differential drive mode), this ensures that less power is wasted when the drone operates which leads to increased runtime.

![gputest_2](https://user-images.githubusercontent.com/63254914/122204002-3d25e800-cebc-11eb-870e-8d2952ef6038.gif)

### Autonomous detection
An IP camera can be accessed in OpenCV by providing the streaming URL of the camera in the constructor of cv2.VideoCapture. The HTTP protocol is used by the camera to stream video. The frames of the streamed video are processed by the deep learning model using keras and TensorFlow framework to detect anomalies on industrial structures. The datasets of cracks and rust from Kaggle and inception v3 model from local pre-trained weights have been used. The model itself is made up of symmetric and asymmetric building blocks, including convolutions, average pooling, max pooling, concats, dropouts, and fully connected layers. Batch norm is used extensively throughout the model and applied to activation inputs. Loss is computed via SoftMax.

![ip_ml](https://user-images.githubusercontent.com/63254914/122218645-44ed8880-cecc-11eb-9fea-76cf10efe5bb.gif)

## Novelty and innovativeness
- Concept of using self-transforming bot in fields of inspecting inaccessible arenas.
- Using the mobile clutch mechanism (PED) to efficiently transfer power from BLDC to wheels and propellers.
-	Integrating sprawl mechanism and PED for drone to crawl into tight and narrow spaces using reconfigurable geometry.
-	Compared to physical inspection by humans, it is safe, faster, more accurate and avoids the need for scaffolding and avoids any risk to human life.
-	A novel method for the bot to efficiently maneuver and move about any confined space and systems connected at different heights.
-	Convolutional Neural Networking to detect multiple potential defects that is precise, accurate, faster and reduces the workload of the operator.

---------------------------------------------------
## Gallery
### Drone sketch
![WhatsApp Image 2021-03-24 at 13 40 13](https://user-images.githubusercontent.com/63254914/121786457-753bdb00-cbdd-11eb-8a6d-b470b71ed607.jpeg)

### Exploded view
![gputest_2_1](https://user-images.githubusercontent.com/63254914/122204289-968e1700-cebc-11eb-933c-950bb0961dc6.gif)

### HIDQ bot
![IMG-20210324-WA0054](https://user-images.githubusercontent.com/63254914/121786458-77059e80-cbdd-11eb-857d-4f1eea02548d.jpg)

### Self transforming mechanism
![main](https://user-images.githubusercontent.com/63254914/122221131-9dbe2080-cece-11eb-8260-874edcabec2c.gif)

## Team HIDQ
- [Aswin Sreekumar](https://github.com/aswin-sreekumar)
- [Sivvani M](https://github.com/Msivvani)
- [Satish Kumar L](https://github.com/Satish-Kumar-L)
- [Lokesh Keshav S](https://github.com/dankitydanker)

