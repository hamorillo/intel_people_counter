# SSD Mobilenet v2 COCO
# python nd131-openvino-fundamentals-project-starter/main.py -i nd131-openvino-fundamentals-project-starter/resources/Pedestrian_Detect_2_1_1.mp4 -m IR/ssd_mobilenet_v2_coco_2018_03_29/frozen_inference_graph.xml -d CPU -pt 0.6 | /Users/hector/Downloads/ffmpeg/ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm

# With an image as input
# python nd131-openvino-fundamentals-project-starter/main.py -i nd131-openvino-fundamentals-project-starter/resources/girl.png -m IR/ssd_mobilenet_v2_coco_2018_03_29/frozen_inference_graph.xml -d CPU -pt 0.6 | /Users/hector/Downloads/ffmpeg/ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm



python nd131-openvino-fundamentals-project-starter/main.py -i nd131-openvino-fundamentals-project-starter/resources/Pedestrian_Detect_2_1_1.mp4 -m  IR/VGG_coco_SSD_512x512_iter_360000/VGG_coco_SSD_512x512_iter_360000.xml -d CPU -pt 0.6 | /Users/hector/Downloads/ffmpeg/ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm
# With an image as input
# python nd131-openvino-fundamentals-project-starter/main.py -i nd131-openvino-fundamentals-project-starter/resources/girl.png -m IR/VGG_coco_SSD_512x512_iter_360000/VGG_coco_SSD_512x512_iter_360000.xml -d CPU -pt 0.6 | /Users/hector/Downloads/ffmpeg/ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm