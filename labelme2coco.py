# import package
import labelme2coco

# set directory that contains labelme annotations and image files
labelme_folder = "/home/beata/Studia/TP/Change_Your_Background/TrainOwnSegmentationNetwork/Dataset/train"

# set path for coco json to be saved
save_json_path = "/home/beata/Studia/TP/Change_Your_Background/TrainOwnSegmentationNetwork/Dataset/coco_train"

# convert labelme annotations to coco
labelme2coco.convert(labelme_folder, save_json_path)

