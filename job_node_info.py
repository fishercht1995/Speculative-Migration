f = open("info.txt")
lines = f.readlines()
f.close()
job_node = {}
for i in range(1,len(lines)):
	line = lines[i]
	splited = line.split(" ")
	node,job = splited[0],splited[-1][:-1]
	job_node[job] = node
import pandas as pd
job = list(job_node.keys())
node = []
for j in job:
	node.append(job_node[j])

d = pd.DataFrame()
d["job"] = job
d["node"] = node
d.to_csv("job_node_info.csv") 
