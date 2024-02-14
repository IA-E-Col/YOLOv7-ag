#%%

import os
import os.path
from os import path

#%%
dir_list = ["amborella", "castanea", "convolvulaceae", "desmodium", "eugenia", "laurus", "litsea", "magnolia", "monimiaceae", "rubus", "ulmus"]

data_folder = "your_data_folder"
dest_folder = "your_destination_folder"

for dir in dir_list:
    print(dir)
    folder = os.path.join(data_folder,dir)
    cmd = "python detect-for-annotation.py --weights last.pt --conf-thres 0.5 --img-size 640 --source " + folder + " --project "+dest_folder+" --name "+dir+" --device 2,3 --view-img --no-trace --save-txt --nosave"
    print(cmd)
    os.system(cmd)
print('Done')
    
    
