import shutil
import os


def rename_output(output_name_dir):
    # def renameInOrder(dir_path):
        old_name_path='./inputdata/video_input/'
        old_name_list=[]
        new_name_list=[]


        for i in os.listdir(old_name_path):
            old_name_list.append(i)
            old_name_list.sort()
            print(old_name_list)


        
         
        c1=os.listdir(output_name_dir[0])
        print(c1)
           # new_name_list.append(c)
        c1.sort()
        


            
        seq=0
        for x in c1:
                        old_name=output_name_dir[0]+old_name_list[seq]
                        new_file_name = output_name_dir[0] + x.split('.')[0]+'.txt'
                        os.rename(new_file_name, old_name)
                        seq+=1

        #c2=os.listdir(output_name_dir[1])
        #c2.sort()

       # seq2=0
    #for y in c2: 
                    
     #               
      #                  old_name=output_name_dir[1]+old_name_list[seq2]+'.mp4'
       #                 new_file_name = output_name_dir[1] + y
        #                os.rename(new_file_name, old_name)
         #               seq2+=1
                    



path_output_txt='/workspace/qd3dt-yolo/work_dirs/KITTI/output_test_dla34_regress_GTA_VeloLSTM_box3d_deep_depth_motion_lstm_3dcen/txts/'
path_output_video='/workspace/qd3dt-yolo/work_dirs/KITTI/output_test_dla34_regress_GTA_VeloLSTM_box3d_deep_depth_motion_lstm_3dcen/shows_compose/'
output_dir='/workspace/qd3dt-yolo/output_data/'

#if not os.path.exists(output_dir)

#shutil.move(path_output_txt,output_dir+'txts/')
#shutil.move(path_output_video,output_dir+'shows_compose/')



output_name_dir=[]
output_name_dir.append(path_output_txt)
output_name_dir.append(path_output_video)
#for i in os.listdir(output_dir):
 #   output_name_dir.append(output_dir+i+'/')
rename_output(output_name_dir)


#shutil.copy(path_output_txt,output_dir+'txts/')
#shutil.copy(path_output_video,output_dir+'shows_compose/')

