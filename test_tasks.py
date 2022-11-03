import pandas as pd
import pymongo
from pyexcelerate import Workbook
from datetime import datetime
from pyexcelerate.Format import Format
def create_date(yyyy,mm,dd,h,m,s):
    date = datetime(yyyy,mm,dd,h,m,s).strftime("%Y-%m-%dT%H:%M:%S")
    return datetime.strptime(date,'%Y-%m-%dT%H:%M:%S')
def create_excel(data,file_name):
    values = [data.columns] + list(data.values)
    wb = Workbook()
    ws = wb.new_sheet("sheet name", data=values)
    for i in range(1,len(values)+1):
        ws[i][df1.columns.get_loc("TimeToEnter")+1].style.format.format = 'yyyy/mm/dd hh:mm:ss'
        ws[i][df1.columns.get_loc("Datetime")+1].style.format.format = 'yyyy/mm/dd hh:mm:ss'
    wb.save(file_name)
data = {'Id':[i for i in range(1,8)],
        'Name':['Alex','Justin','Set','Carlos','Gareth','John','Bob'],
        'Surname':['Smur','Forman','Carey','Caret','Chapman','James','James'],
        'Age':[21,25,35,40,19,27,25],
        'Job':['Python Developer','Java Developer','Project Manager','Enterprise architect','Python Developer','IOS Developer','Python Developer'],
        'Datetime':[create_date(2022,1,1,9,45,12),create_date(2022,1,1,11,50,25),create_date(2022,1,1,10,0,45),create_date(2022,1,1,9,7,36),create_date(2022,1,1,11,54,10),create_date(2022,1,1,9,56,40),create_date(2022,1,1,9,52,45)]
       }
df = pd.DataFrame(data = data)
print(df)
dev1 = df[(df['Age']>18) & (df['Age']<=21) & (df['Job'].str.contains('Developer'))]
dev2 = df.drop(dev1.index)
dev2 = dev2[dev2['Job'].str.contains('Developer')]
dev1['TimeToEnter'] = create_date(2022,1,1,9,0,0)
dev2['TimeToEnter'] = create_date(2022,1,1,9,15,0)
df1 = pd.concat([dev1,dev2]).sort_values(by='Id')
print(df1)
create_excel(df1,"18MoreAnd21andLess.xlsx")
db_client = pymongo.MongoClient('mongodb+srv://azamat01:mX0D7GtgyAxfcLJr@cluster0.gwgamzh.mongodb.net/test')
current_db = db_client['Tasks']
collection1 = current_db['18MoreAnd21andLess']
collection1.insert_many(df1.to_dict('records'))
managers1 = df[(df['Age']>=35) & (df['Job'].str.contains('Manager'))]
managers2 = df.drop(managers1.index)
managers2 = managers2[managers2['Job'].str.contains('Manager')]
managers1['TimeToEnter'] = create_date(2022,1,1,11,0,0)
managers2['TimeToEnter'] = create_date(2022,1,1,11,30,0)
df2 = pd.concat([managers1,managers2]).sort_values(by='Id')
print(df2)
create_excel(df2,"35AndMore.xlsx")
collection2 = current_db['35AndMore']
collection2.insert_many(df1.to_dict('records'))
arch1 = df[(df['Age']>=35) & (df['Job'].str.contains('architect'))]
arch2 = df.drop(managers1.index)
arch2 = managers2[managers2['Job'].str.contains('architect')]
arch1['TimeToEnter'] = create_date(2022,1,1,10,30,0)
arch2['TimeToEnter'] = create_date(2022,1,1,10,40,0)
df3 = pd.concat([arch1,arch2]).sort_values(by='Id')
print(df3)
create_excel(df3,"ArchitectEnterTime.xlsx")
collection3 = current_db['ArchitectEnterTime']
collection3.insert_many(df1.to_dict('records'))