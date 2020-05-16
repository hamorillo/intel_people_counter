# SSD Mobilenet v2 COCO
# python nd131-openvino-fundamentals-project-starter/main.py -i nd131-openvino-fundamentals-project-starter/resources/Pedestrian_Detect_2_1_1.mp4 -m IR/ssd_mobilenet_v2_coco_2018_03_29/frozen_inference_graph.xml -d CPU -pt 0.6 -lf logs/log.log | /Users/hector/Downloads/ffmpeg/ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm
# With an image as input
# python nd131-openvino-fundamentals-project-starter/main.py -i nd131-openvino-fundamentals-project-starter/resources/girl.png -m IR/ssd_mobilenet_v2_coco_2018_03_29/frozen_inference_graph.xml -d CPU -pt 0.6 | /Users/hector/Downloads/ffmpeg/ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm


# VGG Coco SSD 512
# python nd131-openvino-fundamentals-project-starter/main.py -i nd131-openvino-fundamentals-project-starter/resources/Pedestrian_Detect_2_1_1.mp4 -m  IR/VGG_coco_SSD_512x512_iter_360000/VGG_coco_SSD_512x512_iter_360000.xml -d CPU -pt 0.6 | /Users/hector/Downloads/ffmpeg/ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm
# With an image as input
# python nd131-openvino-fundamentals-project-starter/main.py -i nd131-openvino-fundamentals-project-starter/resources/girl.png -m IR/VGG_coco_SSD_512x512_iter_360000/VGG_coco_SSD_512x512_iter_360000.xml -d CPU -pt 0.6 | /Users/hector/Downloads/ffmpeg/ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm# VGG Coco SSD 512

# VGG Coco SSD 300
# python nd131-openvino-fundamentals-project-starter/main.py -i nd131-openvino-fundamentals-project-starter/resources/Pedestrian_Detect_2_1_1.mp4 -m  IR/VGG_coco_SSD_300x300_iter_400000/VGG_coco_SSD_300x300_iter_400000.xml -d CPU -pt 0.6 | /Users/hector/Downloads/ffmpeg/ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm
# With an image as input
# python nd131-openvino-fundamentals-project-starter/main.py -i nd131-openvino-fundamentals-project-starter/resources/girl.png -m IR/VGG_coco_SSD_300x300_iter_400000/VGG_coco_SSD_300x300_iter_400000.xml -d CPU -pt 0.6 | /Users/hector/Downloads/ffmpeg/ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm

# VGG VOC SSD 300
# python nd131-openvino-fundamentals-project-starter/main.py -i nd131-openvino-fundamentals-project-starter/resources/Pedestrian_Detect_2_1_1.mp4 -m  IR/VGG_VOC0712Plus_SSD_300x300_ft_iter_160000/VGG_VOC0712Plus_SSD_300x300_ft_iter_160000.xml -d CPU -pt 0.6 | /Users/hector/Downloads/ffmpeg/ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm
# With an image as input
python nd131-openvino-fundamentals-project-starter/main.py -i nd131-openvino-fundamentals-project-starter/resources/girl.png -m IR/VGG_VOC0712Plus_SSD_300x300_ft_iter_160000/VGG_VOC0712Plus_SSD_300x300_ft_iter_160000.xml -d CPU -pt 0.6 -is PASCAL_VOC | /Users/hector/Downloads/ffmpeg/ffmpeg -v warning -f rawvideo -pixel_format bgr24 -video_size 768x432 -framerate 24 -i - http://0.0.0.0:3004/fac.ffm