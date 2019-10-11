import yaml
import os
f = open("info.txt")
lines = f.readlines()
f.close()
job_node = {}
for i in range(1,len(lines)):
	line = lines[i]
	splited = line.split(" ")
	node,job = splited[0],splited[-1][:-1]
	job_node[job] = node
path = "/mnt/linuxidc/templates/"
def read_templates():
    file_names = os.listdir(path)
    dict = {}
    for file_name in file_names:
        yaml_dic = yaml.load(open(path+file_name, 'r'))
	name = yaml_dic["metadata"]["name"]
	yaml_dic["spec"]["nodeName"] = job_node[name]
	#yaml_dic["spec"].pop("nodeName")
        dict[file_name] = yaml_dic
    return dict

dic = read_templates()
for file_name in dic.keys():
	with open(path+file_name, "w") as yaml_file:
		yaml.dump(dic[file_name], yaml_file)
