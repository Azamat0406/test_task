# Python 
Download and import libraries such as pandas,pymongo,pyexcelerate,datetime. First of all, I created a df dataset using pandas.Further, setting certain conditions, i import the result into an excel file using pyexcelerate.Using the pymongo library, upload the result to the database.

#def create_date(yyyy,mm,dd,h,m,s):
    date = datetime(yyyy,mm,dd,h,m,s).strftime("%Y-%m-%dT%H:%M:%S")
    return datetime.strptime(date,'%Y-%m-%dT%H:%M:%S')
