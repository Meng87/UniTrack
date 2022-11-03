# Introduction
A tool that performs uses UniTrack person detection on video data.

For a full description of the how UniTrack works, visit the [UniTrack project page](https://github.com/Zhongdao/UniTrack)

# Installation
Adapted from [docs/INSTALL.md](docs/INSTALL.md)

## Requirements
* Nvidia device with CUDA 
* Python 3.7+
* PyTorch 1.7.0+
* torchvision 0.8.0+
* Other python packages in requirements.txt

## Install with conda and pip

1. Create a conda virtual environment.
```
conda create -n unitrack python=3.7 -y
conda activate unitrack
```

2. Install PyTorch or relevant command from [PyTorch website](https://pytorch.org/get-started/locally/)
```
pip3 install torch torchvision torchaudio
```

3. Get UniTrack
```
git clone https://github.com/Meng87/UniTrack.git
cd UniTrack
```

4. Install other dependencies
```
pip install -r requirements.txt
pip3 install cython onnx cython_bbox==0.1.3 opencv-python numpy
```

# Running the multi-object detection model
Run the model on a directory of videos to detect 'person' (class 0). Assumes output directory ```results``` has been created beforehand.
```
python demo/mot_demo.py --path ./video_dir --classes 0 --save_result --output-root ./results
```
Flag             | Description |
---              | ---         |
--path           | Path to directory containing the videos you want to run multi-object detection on. |
--classes        | Indices of classes you want to detect and track e.g. "person" class has index 0. See [here](https://gist.github.com/AruniRC/7b3dadd004da04c80198557db5da4bda) for the index list. By default all 80 classes are detected and tracked. Separate multiple indices with spaces. |
--output-root    | Directory where you want results to be stored |

# Output
The tool will return 4 outputs:
## 1. Bounding Box Coordinates
For each person that appears in the video, the bounding box coordinates for that person will be outputted for each frame of the video in a `.json` file, formatted as follows:
```
{
  <person ID>: [<(x, y, w, h) or None>],
  ...
}
```
The person ID is a unique integer that identifies the person in the video. The x and y variable denotes the left top coordinates of the bounding box, while w and h denote the width and height of the bounding box respectively.

## 2. Cropped Video Frame
For each person that appears in the video, the cropped video frame (in numpy array form) that shows only the detected person will be outputted for each frame of the video in a `.json` file.
```
{
  <person ID>: [<numpy.ndarray or None>],
  ...
}
```
## 3. Proportion of time that each person appears in a video
The proportion of time that each person appears in a video will be outputted in a `.csv` file containing the following columns
| Column Name | Description |
| ----------- | ----------- |
| video path  | path to the video file |
| person_id   | an integer that uniquely identifies the person detected |
| proportion  | proportion of time person appears in the video |

## 4. Video Annotated with Bounding Boxes
A directory with the same name as the video will be created. It will contain a video annotated with bounding boxes around each detected person as well as a folder named `frames` that contains `.jpg` images of each frame of the annotated video.

# Visualizing the results
The third `.csv` file output can be visualized by running
```
cd demo
python viz.py
```

# Acknowledgements
This tool utilizes the [UniTrack model](https://github.com/Zhongdao/UniTrack).

