import pandas as pd
from pandas import DataFrame
import time
import xlrd
import os

def getExcelfile(sourcepath):
    source_dir = os.walk(sourcepath)
    excel_list = []
    for path, dir_list, files in source_dir:
        for file in files:
            if file.endswith(".xlsx"):
                file_name = os.path.join(path,file)
                excel_list.append(file_name)
    return excel_list


if __name__ == "__main__":
  process_time = time.strftime("%Y%m%d_%H%M", time.localtime())
  filelist=getExcelfile(r'C:\Work\Develop\cudata')
  for i in filelist:

    file_name = os.path.split(i)
    file_name = file_name[-1]
    file_name = file_name.split('_')

    while '' in file_name:
        file_name.remove('')

    if len(file_name) == 5:
        if (file_name[-1].split('.'))[0].isdigit():

            file_name = process_time + '_' + file_name[0] + '_' + file_name[1] + '_' + ((file_name[2]).split(' '))[0]+' '+((file_name[2]).split(' '))[1]+'_'+((file_name[2]).split(' '))[2] + '.xlsx'
            print(file_name)
        else:
            file_name = process_time + '_' + file_name[0] + '_' + file_name[1] + '_' + file_name[2] + ' ' + file_name[3] + '_' + (file_name[-1].split('.'))[0] + '.xlsx'
            print(file_name)

    elif len(file_name) > 5:
        file_name = process_time + '_'+file_name[0] + '_' + file_name[1] + '_' + file_name[2] + ' ' + file_name[3] + '_' + file_name[4]  + '.xlsx'
        print(file_name)
    #with pd.ExcelWriter('./Add_suffix/China Mobile' + file_name) as f:
    #    insert_xlsx(df,f,'PRJ WP Site')
    #    insert_xlsx(df2,f, 'PLO dates')
    #    insert_xlsx(df3,f, 'UDF ITEM')