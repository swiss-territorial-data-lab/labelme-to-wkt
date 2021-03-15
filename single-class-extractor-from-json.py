import json
import glob
import os

os.chdir("comb-test")

for file_name in glob.iglob('*.json'):

    # read the data
    with open(file_name, "r") as fr:
        data = json.load(fr)

    datashp=data["shapes"]

    newshp = []
    a = 0
    for i in datashp: 
        if i["label"] == "THM":
            a=a+1
            print(file_name, " THM ", a)
            newshp.append(i)

    #print(newshp)
    data["shapes"] = newshp
    #print(data)
    newdata = json.dumps(data, indent=2)
    #print(newdata)

    # write the data back to file
    with open(file_name, "w") as fw:
        json.dump(data, fw, indent=2)
