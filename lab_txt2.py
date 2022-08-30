import os
import json
import shutil
import argparse
from cut_video import image_process

def type_conversion(type_data):
    if type_data == "bicycle":
        return "Cyclist"
    elif type_data == "motorcycle":
        return "Cyclist"
    elif type_data == "car":
        return "Car"
    elif type_data == "truck":
        return "Truck"
    elif type_data == "bus":
        return "Bus"
    elif type_data == "person":
        return "Pedestrian"
    else:
        print(type_data)
        print("type error")
        exit()

def read_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as load_f:
            data = json.load(load_f)
            obj_data = data['2D']['dynamic']
        return obj_data
    else:
        print("no json file")
        return
def json_data_to_yolo(json_data):
    all_data=[]
    for line in json_data:
        temp1 = (line['bounding_box']['x1'],line['bounding_box']['y1'])
        temp2 = (line['bounding_box']['x2'],line['bounding_box']['y2'])
        temp3 = [temp1,temp2]
        type_data = type_conversion(line['type'])
        yolo_data= {"id":line['id'],"box_2d":temp3,"detected_class":type_data,"2d_tpye":line['type']}
        all_data.append(yolo_data)
    return all_data

def save_txt(frame,yolo_id,box_2d,type_2d):
    data = [int(frame),yolo_id,type_2d,"0","0","0",box_2d[0][0],box_2d[0][1],box_2d[1][0],box_2d[1][1],"0","0","0","0","0","0","0","0"]
    data = [str(x) for x in data]
    all_3D_data.append(data)
def write_txt(data,index,output_path):

    with open(output_path+index+"_2d.txt", "w") as f:
        for i in data:
            for j in i:
                f.write(j)
                f.write(' ')
            f.writelines("\n")

def renameInOrder(dir_path):
    dir_list = []
    dir_name=[]
    for i in os.listdir(dir_path):
        dir_list.append(dir_path + i + '/')
        dir_name.append(i)
    
    for j in dir_list:

        name_list_old = []
        dir_name_list=[]
        for p in os.listdir(j):
            name_list_old.append(p)
            name_list_old.sort()
            print(j)
            z=j.split("/")[5]
            dir_name_list.append(z)

        
        seq=0

        for dir_name in dir_name_list:
    
            if dir_name == 'label':
                    old_name = j + name_list_old[seq]
                    print(old_name)
                    new_file_name = j + '{:04d}'.format(seq) + '_2d'
                    try:
                        os.rename(old_name, new_file_name)
                    except:
                        pass
                    seq += 1
                   
            else:

                    old_name = j + name_list_old[seq]
                    new_file_name = j + '{:04d}'.format(seq)
                    try:
                        os.rename(old_name, new_file_name)
                    except:
                        pass
                    seq += 1
                   


all_3D_data = []

path_label = './testing/label/'
output_dir = './testing/image_02/'


json_path_dir = './inputdata/label_input/'
json_path_dir = image_process(1).make_dir(json_path_dir)



for i in os.listdir(json_path_dir):
    image_index =i

    image_dir = output_dir + image_index + '/'
    print(os.listdir(image_dir)[0].split('.png')[0])
    json_path = json_path_dir + image_index + "/"

    save_path = path_label

    # image_dir = r'C:\Users\flychen\Desktop\image_02'+"\\"+image_index +"\\"
    # json_path = r'D:\lab_data\input\output_json'+ "\\"+image_index +"\\"
    #
    # save_path = r'C:\Users\flychen\Desktop\label'+ "\\"


    if not os.path.exists(save_path):
        os.makedirs(save_path)

    try:
        ids = [x.split('.')[0] for x in sorted(os.listdir(image_dir))]
    except:
        print("\nError: no images in %s" % image_dir)
        exit()

    for img_id in ids:

        # json_file = json_path + img_id + ".JSON"
        json_file = json_path +image_index+"_"+ str("%05d"%int(img_id)) + "_2D.JSON"
        print(json_file)
        json_data = read_json(json_file)

        if json_data is None or len(json_data) == 0:
            print(img_id + " 2D have no Result")
            continue

        yolo_results = json_data_to_yolo(json_data)
        for yolo_result in yolo_results:
            yolo_id = yolo_result['id']

            # save_txt(img_id.split("_")[1],yolo_id, yolo_result['box_2d'],yolo_result['2d_tpye'])
            save_txt(img_id,yolo_id, yolo_result['box_2d'],yolo_result['2d_tpye'])

    write_txt(all_3D_data,image_index,save_path)

    # move
parser = argparse.ArgumentParser()
parser.add_argument('--outputName', required=True, type=str)
args = parser.parse_args()

move_dir_old = './testing'
move_dir_new= './data/'+args.outputName+'/tracking/'

try:
    shutil.move(move_dir_old, move_dir_new)
except:
    pass
file_new_path=move_dir_new+'testing/'
print(os.listdir(file_new_path))

dir_path='./data/'+args.outputName+'/tracking/testing/'
renameInOrder(dir_path)

#
# renameInOrder(move_dir_new)



