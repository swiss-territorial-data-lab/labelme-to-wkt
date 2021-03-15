import json
import glob
import os

os.chdir("corrected")

newshp = []

for file_name in glob.iglob('*.json'):

    print("Shapes from",file_name,"extracted.")
    # read the data
    with open(file_name, "r") as fr:
        data = json.load(fr)

    datashp=data["shapes"]

    nx = int(file_name[0:7])
    ny = int(file_name[8:15])
    #print(nx,",",ny)
    
    a = 0
    for i in datashp: 
        a=a+1
        newshplist = []
        b = 0
        for ele in i["points"]:
            #print(ele)
            b=b+1
            x = nx + (0.1 * ele[0])
            y = ny - (0.1 * ele[1])
            if b==1:
                primx = x
                primy = y
                primcoord = [x,y]
            newcoord = [x,y]
            #print ("Coords:",newcoord)
            newshplist.append(newcoord)
        newshplist.append(primcoord)
        #print(file_name, " THM ", a)
        #newshp.append(i["points"])
        #print("shape end:",newshplist)
        newshp.append(newshplist)

#print(newshp)
complete = ""
for poly in newshp:
    polystr = "POLYGON (("
    #print(poly)
    for point in poly:
        #print(point)
        polystr = polystr + str(point[0]) + " " + str(point[1]) + ", "
    polystr = polystr[:-2] + "))\n"
    complete = complete + polystr
print(complete)
#for b in newshp:
#    print (b)

os.chdir("..")

text_file = open("Output.txt", "w")
text_file.write(complete)
text_file.close()
