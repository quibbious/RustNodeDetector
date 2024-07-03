# download dataset from roboflow: 

from roboflow import Roboflow
rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace("theoldtofu").project("rustnodedetector")
version = project.version(6)
dataset = version.download("yolov5")
