import os
dir_path = "challanges/"
listvar = []
res = os.listdir(dir_path)
print(res)
for eachfile in res:
    listvar.append(eachfile.split(".")[0])
print(listvar)
