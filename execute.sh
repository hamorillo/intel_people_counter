# SSD Mobilenet v2 COCO
python nd131-openvino-fundamentals-project-starter/main.py -i nd131-openvino-fundamentals-project-starter/resources/Pedestrian_Detect_2_1_1.mp4 -m /Users/hector/Downloads/ssd_mobilenet_v2_coco_2018_03_29/frozen_inference_graph.xml -d CPU -pt 0.6 | /Users/hector/Downloads/ffmpeg/ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm