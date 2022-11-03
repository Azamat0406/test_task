# Python 
Download and import libraries such as pandas,pymongo,pyexcelerate,datetime. First of all, I created a df dataset using pandas.Further, setting certain conditions, i import the result into an excel file using pyexcelerate.Using the pymongo library, upload the result to the database.

## def create_date(yyyy,mm,dd,h,m,s)<br />
Creates a date in the desired format. Converts a string to a date.

## def create_excel(data,file_name)
This function will save our dataset to an excel file.

## Pymongodb
Import the library and join our client via url by writing a username and password. To get a server, we create a cluster for MongoDB. Next, we create databases and collections.The result of our code can be viewed on MongoDB Compass
