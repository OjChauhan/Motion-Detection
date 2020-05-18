## The Project is basically for buildiing a Efficient and Noise tolerant algorithm for identifying objects in defined space with help of a webcam and can be extended to an external camera.For Better results, Let the motion detector run for sometime before adapting to it's surroundings.

## Step-1 : Build the project

###Tools to compile the c files :
1. gcc
2. make
3. pkgconfig

**Example** : For debian-based distros : `sudo apt install gcc make pkg-config`


## Step-2 : Make the project

To build, you can use **setup.py** or directly **make** in Bash:

* `make` or `./setup.py build` -> build the C dependencies
* `make clean` or `./setup.py clean` -> remove temporary files
* `make fclean` or `./setup.py fclean` -> remove temporary and built files
* `make re` or `./setup.py rebuild` -> perform both `fclean` and `build`

## Step-3 : Run the motion_capture.py for motion detection

* `./motion.py` or `python3 motion_capture.py`

## Detector usage and parameters

* <bg_subs_scale_percent>: Scaling initial frame before movement detection occurs (default: *1/4*);
* <bg_history>: Length of background accumulator ring buffer (default: *15*);
* <bg_history_collection_period_max>: Defines how often the background ring buffer is updated with frames from movement
   (default:*1* ; every frame);
* <movement_frames_history>: how much frames to keep in movement accumulator ring buffer (default: *5*);
* <brightness_discard_level>: threshold which is used to detect movement from the noise (default: *20*);
* <pixel_compression_ratio>: how much to compress the initial video for boxes search (default: *0.1*), means that every
   *10x10 px* of initial frame will be resized to *1x1 px* of detection frame;
* <group_boxes>: group overlapping boxes into a single one or just keep them as they are (default: **True**);
* <expansion_step>: how big is expansion algorithm step when it searches for boxes, lower steps lead to smaller performance
   and close objects are detected as separate, bigger step leads to faster algorithm performance and close objects can be
   detected as a single one (default: *1*).

## Vital Information

The Efficency depends greatly from the values of following detector parameters:

* [`bg_subs_scale_percent`] (default 1/4), leads to 320x180 frame for initial 1280x720 frame.
* [`pixel_compression_ratio`] (default 1/10),  leads to 128x72 for initial bounding boxes 1280x720 frame.
* [`expansion_step`] is used to find bounding boxes.

## Tested in following environments :
1. **Python Versions** : 3.4 , 3.5 , 3.6 , 3.8.
2. **gcc Versions** :  7.5 , 8.4 ,9.3. 
3. **OS** : Ubuntu(16.04 LTS ,18.04 LTS, 19.10 , 20.04 LTS ) , Parrot OS , Kali Linux but has some issues with Arch based
        Distributions.

