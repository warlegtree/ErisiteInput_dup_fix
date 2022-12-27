import os

def getExcelfile():
    source_dir = os.walk(r'C:\Work\Develop\cmdata')
    excel_list = []
    for path, dir_list, files in source_dir:
        for file in files:
            if file.endswith(".xlsx"):
                file_name = os.path.join(path,file)
                excel_list.append(file_name)
    return excel_list
filelist = getExcelfile()
for i in filelist:
    print(i)
    name = (os.path.split(i))[1]
    print(name)
    if name.startswith('report'):
        name = str(name).replace("__", "_")
        temp_name = ((name.split("."))[0]).split('_')
        new_name = temp_name[-2]+'_'+temp_name[-1]+'_'+temp_name[1]+'_'+temp_name[2]+'_'+temp_name[3]+'_'+temp_name[4]+'.xlsx'
        print(new_name)
    else:
        pass