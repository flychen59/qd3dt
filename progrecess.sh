#!/bin/bash


outputName=cyp

python3 ./cut_video.py --outputName=$outputName 
python3 ./lab_txt2.py  --outputName=$outputName
python3 ./scripts/kitti2coco.py  --outputName=$outputName
python3 ./tools/bbb.py kitti /workspace/qd3dt-yolo/configs/KITTI/quasi_dla34_dcn_3dmatch_multibranch_conv_dep_dim_cen_clsrot_sep_aug_confidence_mod_anchor_ratio_small_strides_GTA.py /workspace/qd3dt-yolo/work_dirs/KITTI/sub/latest.pth /workspace/qd3dt-yolo/work_dirs/KITTI/output/output.pkl --data_split_prefix test_dla34_regress_GTA_VeloLSTM --add_test_set 
#python3 ./renameOriginal.py 

