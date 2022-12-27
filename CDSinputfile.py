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

def insert_xlsx(datas,file_name,sheetname):
    df = pd.DataFrame(datas)
    df.to_excel(file_name,sheet_name=sheetname,index=None)

def handle_name_column_value(x):
    if x == '':
      return''
    if x in d:
      d[x] = str(int(d.get(x)) + 1)
    else:
      d[x] = '1'
    return x + '_' + d.get(x)

if __name__ == "__main__":

  filelist=getExcelfile(r'C:\Work\Develop\cmdata')
  for i in filelist:
    process_time = time.strftime("%Y%m%d_%H%M", time.localtime())
    d = dict()
    df = pd.read_excel(i, sheet_name='PRJ WP Site', converters={'Sites--Name':handle_name_column_value})
    df2 = pd.read_excel(i, sheet_name='PLO dates')
    df3 = pd.read_excel(i, sheet_name='UDF ITEM')

    file_name = os.path.split(i)
    file_name = file_name[-1]
    file_name = file_name.split('_')

    while '' in file_name:
        file_name.remove('')

    if len(file_name) == 5:
        if (file_name[-1].split('.'))[0].isdigit():
            file_name = process_time + '_' + file_name[0] + '_' + file_name[1] + '_' + ((file_name[2]).split(' '))[0]+' '+((file_name[2]).split(' '))[1]+'_'+((file_name[2]).split(' '))[2] + '.xlsx'

        else:
            file_name = process_time + '_' + file_name[0] + '_' + file_name[1] + '_' + file_name[2] + ' ' + file_name[3] + '_' + (file_name[-1].split('.'))[0] + '.xlsx'

    elif len(file_name) > 5:
        file_name = process_time + '_'+file_name[0] + '_' + file_name[1] + '_' + file_name[2] + ' ' + file_name[3] + '_' + file_name[4]  + '.xlsx'

    elif len(file_name) < 5:
        file_name = process_time + '_'+file_name[0] + '_' + file_name[1] + '_' + ((file_name[2]).split(' '))[0]+' '+((file_name[2]).split(' '))[1]+'_'+((file_name[2]).split(' '))[2]  + '.xlsx'


    with pd.ExcelWriter('./Add_suffix/' + file_name) as f:
        insert_xlsx(df, f, 'PRJ WP Site')
        insert_xlsx(df2, f, 'PLO dates')
        insert_xlsx(df3, f, 'UDF ITEM')


