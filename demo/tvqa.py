import os

path = "/work/mengrou/UniTrack"

# on atlas
# rsync -av /results/awilf/tvqa_full/tvqa_frames_hq mengrou@vulcan:/work/mengrou/

# preprocess TVQA dataset
os.system("cd /work/mengrou")
os.system("cat tvqa_frames_hq/tvqa_video_frames_fps3_hq.tar.gz.* | tar xz -C tvqa_dataset")

# run object detection
# os.system("tmux new -s tvqa")
# os.system("conda activate unitrack")
# os.system("cd /work/mengrou/UniTrack")
# os.system("python demo/mot_demo.py --path ../tvqa_dataset --classes 0 --save_result --output-root ./results")
