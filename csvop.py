import pandas as pd


def insert_csv(datas, file_name):
    df = pd.DataFrame(datas)
    df.to_csv('{}.csv'.format(file_name),encoding ="utf-8", index=None)
def handle_name_column_value(x):
    #print(d)
    if x == '':
      return''
    if x in d:
      print(x)
      d[x] = str(int(d.get(x)) + 1)
    else:
      d[x] = '1'

    if int(d[x]) > 1:
        return x + '_' + d.get(x)
    else:
        return x

if __name__ == "__main__":
  d = dict()
  data = pd.read_csv("CMSC_mobile.csv")
  df = pd.read_csv('CMSC_mobile.csv', converters={'Name':handle_name_column_value})
  print(df['Name'])
  #df = df.drop(['Unnamed: 0','sf__Error'],axis=1)
  insert_csv(df, 'new3')