from roboflow import Roboflow
# download dataset from roboflow: 
API_KEY="YOUR_API_KEY" # replace "YOUR_API_KEY" with your own api key
if API_KEY == "YOUR_API_KEY":
  raise Exception("Hey! it looks like you forgot to input your API key! Be sure to save db.py, and never share your API_KEY")
  
rf = Roboflow(api_key=API_KEY)
project = rf.workspace("theoldtofu").project("rustnodedetector")
version = project.version(6)
dataset = version.download("yolov5")
