# Speculative-Migration


## Configuration

Based on fishercht1995/progress-based-k8s-scheduler project, there are two more thing need to modify in our kubernetes system

Firstly, modify `clusterrole system:kube-scheduler` and add `pod delete`,`pod create` to our own scheduler.
```
kubectl edit clusterrole system:kube-scheduler
```
Modify config to that
```
- apiGroups:
  - ""
  resources:
  - pods
  verbs:
  - delete
  - get
  - list
  - watch
  - create
  - delete
```

Second, add a folder `/mnt/linuxidc/templates`, and put all working yaml file inside.

## Designed pod

### system.yaml
This yaml file is to create a pod consists of a master container and serveal worker containers. You can change args in worker container to set different parameters: checking time interval and threhold.


## Implement experiment


I have maintained some easily used script to implement experiments

### job_node_info.py

It will generate job:node pairs into a csv file(Since our migrated algorithm will change containers ditribution, we can do it after implement `default` experiment.

### change_yaml.py

It provides a easy way to modify yaml files in `/mnt/linuxidc/templates`. There are two ways to use it
```
	yaml_dic["spec"]["nodeName"] = job_node[name]
	#yaml_dic["spec"].pop("nodeName")
 ```
Now I have just commented second one. The first line mean change yaml file nodeName config to some job_node pair from now. For example, we firstly run default one, then use `python change_yaml.py`. Then when we implement `migrated` algorithm later, orginal containers before migrated will be the same as default. So it makes these two experiments comparable.
 
### test.py

You can use `python test.py` to start experiment. There is a variabale called time_list which is the schedules of submitted. What I do is generate random values in local and then copy it to the script

