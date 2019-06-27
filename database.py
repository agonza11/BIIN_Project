import psycopg2
import psycopg2.extras
import csv
from urllib.parse import urlparse, uses_netloc
import configparser

def connect_to_db(conn_str):
    uses_netloc.append('postgres')
    url = urlparse(conn_str)
    conn = psycopg2.connect(database=url.path[1:],
                            user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port)
    return conn

config = configparser.ConfigParser()
config.read('config.ini')
connection_string = config['database']['postgres_connection']
conn = connect_to_db(connection_string)
cursor = conn.cursor()

#cursor.execute("""DROP TABLE BtGMO""")

#cursor.execute("""DROP TABLE HerbTolGMO""")

#cursor.execute("""DROP TABLE StackedGMO""")

#cursor.execute("""DROP TABLE AllGMO""")

#cursor.execute("""DROP TABLE Production""")

#cursor.execute("""DROP TABLE Future""")

#cursor.execute("""DROP TABLE Herbicide""")


#Crop Production Table
cursor.execute("""CREATE TABLE IF NOT EXISTS Production (Crop VARCHAR(10), State VARCHAR(14), Year INTEGER, Planted INTEGER, Harvested INTEGER, PRIMARY KEY(Crop, State, Year))""")

#BT GMO Crop Adoption Table
cursor.execute("""CREATE TABLE IF NOT EXISTS BtGMO (Crop VARCHAR(10), State VARCHAR(14), Year INTEGER, GM TEXT, Percent INTEGER, PRIMARY KEY(Crop, State, Year), FOREIGN KEY(Crop, State, Year) REFERENCES Production(Crop, State, Year))""")

#Herbicide Tolerance GMO Crop Adoption Table
cursor.execute("""CREATE TABLE IF NOT EXISTS HerbTolGMO (Crop VARCHAR(10), State VARCHAR(14), Year INTEGER, GM TEXT, Percent INTEGER, PRIMARY KEY(Crop, State, Year), FOREIGN KEY(Crop, State, Year) REFERENCES Production(Crop, State, Year))""")

#Stacked GMO Crop Adoption Table
cursor.execute("""CREATE TABLE IF NOT EXISTS StackedGMO (Crop VARCHAR(10), State VARCHAR(14), Year INTEGER, GM TEXT, Percent INTEGER, PRIMARY KEY(Crop, State, Year), FOREIGN KEY(Crop, State, Year) REFERENCES Production(Crop, State, Year))""")

#GMO Crop Adoption Table
cursor.execute("""CREATE TABLE IF NOT EXISTS AllGMO (Crop VARCHAR(10), State VARCHAR(14), Year INTEGER, GM TEXT, Percent INTEGER, PRIMARY KEY(Crop, State, Year), FOREIGN KEY(Crop, State, Year) REFERENCES Production(Crop, State, Year))""")

#Predictive Data TABLE
cursor.execute("""CREATE TABLE IF NOT EXISTS Future (Crop VARCHAR(10), Year INTEGER, Planted INTEGER, Harvested INTEGER, PRIMARY KEY(Crop, Year))""")

#Herbicide Table
cursor.execute("""CREATE TABLE IF NOT EXISTS Herbicide (Crop VARCHAR(10), State VARCHAR(14), Year INTEGER, Herbicide TEXT, ApplicationInLBS VARCHAR(20), PRIMARY KEY (Crop, State, Year, Herbicide))""")

#Data Insertion

with open('CropProduction.csv','r') as CropProduction:
    reader = csv.reader(CropProduction)
    for row in reader:
        cursor.execute('INSERT INTO Production VALUES(%s,%s,%s,%s,%s)',row)

with open('BtGMO.csv','r') as BtGMO:
    reader = csv.reader(BtGMO)
    for row in reader:
        cursor.execute('INSERT INTO BtGMO VALUES(%s,%s,%s,%s,%s)',row)

with open('HerbTolGMO.csv','r') as HerbTolGMO:
    reader = csv.reader(HerbTolGMO)
    for row in reader:
        cursor.execute('INSERT INTO HerbTolGMO VALUES(%s,%s,%s,%s,%s)',row)

with open('StackedGMO.csv','r') as StackedGMO:
    reader = csv.reader(StackedGMO)
    for row in reader:
        cursor.execute('INSERT INTO StackedGMO VALUES(%s,%s,%s,%s,%s)',row)

with open('AllGMO.csv','r') as AllGMO:
    reader = csv.reader(AllGMO)
    for row in reader:
        cursor.execute('INSERT INTO AllGMO VALUES(%s,%s,%s,%s,%s)',row)

with open('PredictiveData.csv','r') as PredictiveData:
    reader = csv.reader(PredictiveData)
    for row in reader:
        cursor.execute('INSERT INTO Future VALUES(%s,%s,%s,%s)',row)

with open('Herbicides.csv','r') as Herbicides:
    reader = csv.reader(Herbicides)
    for row in reader:
        cursor.execute('INSERT INTO Herbicide VALUES(%s,%s,%s,%s,%s)',row)

conn.commit()
conn.close()
