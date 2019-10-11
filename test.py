import os
import time
time_list = [25, 43, 50, 65, 86, 142, 192]
#time_list = [i*30 for i in range(20)]

job_list = ["/mnt/linuxidc/templates/job"+str(i)+".yaml" for i in range(1,8)]

i = 0
while len(job_list)>0:
	job = job_list[0]
	if i == time_list[0]:
		time_list.pop(0)
		job_list.pop(0)
		os.popen("kubectl apply -f "+job)
	i += 1
	time.sleep(1)
