import torch
import torch.nn as nn
import torch.nn.functional as F
import my_wmseg_main
import os

if __name__ == '__main__':
    os.environ['CHECKPOINT_PATH'] = "/opt"
    os.system('CHECKPOINT_PATH=/opt')
    # tags=torch.tensor([[2]])
    # ts1=torch.tensor([[[0.4,0.6]]])
    # ts2=torch.tensor([[[0.6,0.4]]])
    # info_gain,probs_av = my_wmseg_main.uc_estimation([ts1,ts2])
    #
    # tags=my_wmseg_main.tags_select(tags,info_gain,probs_av,1,0.7)
    # print(tags)




