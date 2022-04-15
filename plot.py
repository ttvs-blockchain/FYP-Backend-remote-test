
import numpy as np
import matplotlib.pyplot as plt
import re

x = np.array([pow(2, 4),	pow(2, 5),	pow(2, 6),	pow(
    2, 7),	pow(2, 8),	pow(2, 9), pow(2, 10)])


################ Modify PATH to plot ################
FOLDER_PATH = "./15-04-2022-trial-1"
#####################################################


e2e_log = open(FOLDER_PATH+"/e2etime.log", "r")
upload_log = open(FOLDER_PATH+"/upload.log", "r")

e2e_time = upload_time = np.array([])

for line in e2e_log.readlines():                          
    line = line.strip()                             
    if len(line) >58:
        res = float(re.findall("\d+\.\d+", line)[0])
        e2e_time = np.append(e2e_time, res)
        
for line in upload_log.readlines():                          
    line = line.strip()                             
    if len(line) >58:
        res = float(re.findall("\d+\.\d+", line)[0])
        upload_time = np.append(upload_time, res)

e2e_log.close()
upload_log.close()


plt.title("issuing time diagram")
plt.plot(x, e2e_time, '-o')
plt.grid()

plt.savefig(FOLDER_PATH + "/issuing-time-diagram.png")
plt.close()

plt.title("upload time diagram")
plt.plot(x, upload_time, '-o')
plt.grid()
# plt.show()
plt.savefig(FOLDER_PATH + "/upload-time-diagram.png")
plt.close()
