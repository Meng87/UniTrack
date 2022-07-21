# Introduction
A tool that performs uses UniTrack person detection on video data and outputs in .json format:
1) Bounding box coordinates of the location of a given person in a frame of the video
2) Video frames cropped to show only the detected person
3) .csv file containing the proportion of time that each person appears in a video

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

## Running the multi-object detection model
Run the model on a directory of videos to detect 'person' (class 0). Place videos Assumes output directory ```results``` has been created beforehand.
```
python demo/mot_demo.py --path ./video_dir --classes 0 --save_result --output-root ./results
```
Flag             | Description |
---              | ---         |
--path           | Path to directory containing the videos you want to run multi-object detection on. |
--classes        | Indices of classes you want to detect and track e.g. "person" class has index 0. See [here](https://gist.github.com/AruniRC/7b3dadd004da04c80198557db5da4bda) for the index list. By default all 80 classes are detected and tracked. Separate multiple indices with spaces. |
--output-root    | Directory where you want results to be stored |

## Visualizing the results
The .csv output, which contains the proportion of time that each person appears in a video, can be visualized by running
```
cd demo
python viz.py
```

## Acknowledgements
This tool utilizes the [UniTrack model](https://github.com/Zhongdao/UniTrack).

