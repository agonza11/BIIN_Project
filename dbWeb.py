#database functionality
import psycopg2
import psycopg2.extras
import numpy as np
import csv
import matplotlib.pyplot as plt
from urllib.parse import urlparse, uses_netloc
import configparser

#Connects to db
def connect_to_db(conn_str):
    uses_netloc.append('postgres')
    url = urlparse(conn_str)

    conn = psycopg2.connect(database=url.path[1:],
                            user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port)
    return conn
#Credentials
config = configparser.ConfigParser()
config.read('config.ini')
connection_string = config['database']['postgres_connection']
conn = connect_to_db(connection_string)
cur = conn.cursor()
 #functional parts
def production_function(crop, state, year): #this function returns the data for crop production
    title = ("GMO Breakdown of " + crop + " in " + state + ", " + year) #creates a nice title for the graph
    table = list()
    bt = list()
    ht = list()
    st = list()
    data = list()
    if (year != ' ' and int(year) >= 2000):#USDA started collecting gmo data during 2000. Data collected goes back to 1990
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:#SQL Query
            cursor.execute("""
            SELECT Production.Planted, Production.Crop, Production.Harvested, AllGMO.Percent
            FROM Production
            LEFT JOIN AllGMO ON Production.Crop = AllGMO.Crop
            WHERE (Production.Crop = %s AND Production.State = %s AND Production.Year = %s AND
            AllGMO.Crop = %s AND AllGMO.State = %s AND AllGMO.Year = %s)""", (crop, state, year, crop, state, year))
            for d in cursor:
                table.append(d)#fills list named table with data from query. lines below convert list to string and clean it and then convert it to sentence
            answer1 = str(table).replace('[{','')
            answer2 = answer1.replace(': ','')
            answer3 = answer2.replace("'","")
            answer4 = answer3.replace(",","")
            answer5 = answer4.replace('planted',' ')
            answer6 = answer5.replace('crop',' pounds of ')
            answer7 = answer6.replace('harvested',' was planted, and ')
            answer8 = answer7.replace('percent',' pounds were harvested. According to USDA data ')
            answer9 = answer8.replace('C','c')
            answer10 = answer9.replace('Soy','soy')
            answer = answer10.replace('}]','% was documented as being a GMO crop.')

            cursor.execute("""
            SELECT BtGMO.Percent
            FROM Production
            LEFT JOIN BtGMO ON Production.Crop = BtGMO.Crop
            WHERE (Production.Crop = %s AND Production.State = %s AND Production.Year = %s AND
            BtGMO.Crop = %s AND BtGMO.State = %s AND BtGMO.Year = %s)""", (crop, state, year, crop, state, year))
            for d in cursor:
                bt.append(d)#stores sql query for bt gmo data in list
            #lines below convert list to string and clean it to leave just a list of strings (values)
            temp1 = str(bt).replace('percent','')
            temp2 = temp1.replace(':','')
            temp3 = temp2.replace('{','')
            temp4 = temp3.replace('}','')
            temp5 = temp4.replace('[','')
            temp6 = temp5.replace(']','')
            temp7 = temp6.replace('(','')
            temp8 = temp7.replace(')','')
            temp9 = temp8.replace("'","")
            temp = temp9.split(', ')#splits string into list of strings
            for i in temp:
                data.append(int(i)) #converts list of strings to list of integers

            cursor.execute("""
            SELECT HerbTolGMO.Percent
            FROM Production
            LEFT JOIN HerbTolGMO ON Production.Crop = HerbTolGMO.Crop
            WHERE (Production.Crop = %s AND Production.State = %s AND Production.Year = %s AND
            HerbTolGMO.Crop = %s AND HerbTolGMO.State = %s AND HerbTolGMO.Year = %s)""", (crop, state, year, crop, state, year))
            for d in cursor:
                ht.append(d)#stores data in list
            #converts list to string and cleans
            temp1 = str(ht).replace('percent','')
            temp2 = temp1.replace(':','')
            temp3 = temp2.replace('{','')
            temp4 = temp3.replace('}','')
            temp5 = temp4.replace('[','')
            temp6 = temp5.replace(']','')
            temp7 = temp6.replace('(','')
            temp8 = temp7.replace(')','')
            temp9 = temp8.replace("'","")
            temp = temp9.split(', ') #converts string into a list of strings
            for i in temp:
                data.append(int(i))#converts list of strings to list of integers

            cursor.execute("""
            SELECT StackedGMO.Percent
            FROM Production
            LEFT JOIN StackedGMO ON Production.Crop = StackedGMO.Crop
            WHERE (Production.Crop = %s AND Production.State = %s AND Production.Year = %s AND
            StackedGMO.Crop = %s AND StackedGMO.State = %s AND StackedGMO.Year = %s)""", (crop, state, year, crop, state, year))
            for d in cursor:
                st.append(d)#adds query results to list
            #converts list to string and cleans
            temp1 = str(st).replace('percent','')
            temp2 = temp1.replace(':','')
            temp3 = temp2.replace('{','')
            temp4 = temp3.replace('}','')
            temp5 = temp4.replace('[','')
            temp6 = temp5.replace(']','')
            temp7 = temp6.replace('(','')
            temp8 = temp7.replace(')','')
            temp9 = temp8.replace("'","")
            temp = temp9.split(', ')#turns string into list of strings
            for i in temp:
                data.append(int(i))#converts list of strings to list of integers
            #This creates a pie chart based on the user selected inputs from CropDB.html
            labels = ['Bt', 'Herbicide Tolerance', 'Stacked']
            colors = ['red', 'blue', 'purple']#color selection is red for Bt, blue for Herbicide Tolerance, and purple for stacked because its a mix of the two
            patches, texts = plt.pie(data, colors=colors, shadow=True, startangle=90)
            plt.legend(patches, labels, loc="best")
            plt.axis('equal')
            plt.title(title)
            plt.tight_layout()
            plt.show()
            #so if year is 2000 or greater it shows a pie chart and returns the results in the form of a sentence
            #sentence has information on crops planted, harvested, and how many of those were GMs
            #the pie chart shows the breakdown of the specified GMOs
        return(answer)
    else:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute("""
            SELECT Production.Planted, Production.Crop, Production.Harvested
            FROM Production
            WHERE (Production.Crop = %s AND Production.State = %s AND Production.Year = %s)""",(crop,state,year))
            for d in cursor:
                table.append(d) #puts results into a list
                #converts list to string and cleans it to make results into a sentence
            answer1 = str(table).replace('[{','')
            answer2 = answer1.replace(': ','')
            answer3 = answer2.replace("'","")
            answer4 = answer3.replace(",","")
            answer5 = answer4.replace('planted',' ')
            answer6 = answer5.replace('crop',' pounds of ')
            answer7 = answer6.replace('C','c')
            answer8 = answer7.replace('Soy','soy')
            answer9 = answer8.replace('harvested',' was planted, and ')
            answer = answer9.replace('}]',' pounds were harvested.')
            return(answer) #only returns the sql results as a sentence no graph due to lack of practicality
        
def herbicide_function(crop, state, year): #This function returns a graph on herbicide data
    names = list()
    application = list()
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        if year != ' ': #Ensures Query is complete before calculation
            cursor.execute("""
            SELECT Herbicide FROM Herbicide
            WHERE Crop = %s AND State = %s AND Year = %s
            """,(crop,state,year))
            for d in cursor: #adds query results to list
                names.append(d)
            #the next 30 or so lines of code are for turning the elements in the list into a string and then cleans it
            #its particularly messy due to the nature of chemical names
            temp1 = str(names).replace('herbicide','')
            temp2 = temp1.replace(':','')
            temp3 = temp2.replace('{','')
            temp4 = temp3.replace('}','')
            temp5 = temp4.replace('[','')
            temp6 = temp5.replace(']','')
            temp7 = temp6.replace('(','')
            temp8 = temp7.replace(')','')
            temp9 = temp8.replace("'","")
            temp10 = temp9.replace('2, 4','2,4') #for the herbicide 2,4-D
            temp11 = temp10.replace('MBA, POT','MBA,POT') #for herbicide Dicamba, Pot.Salt
            temp12 = temp11.replace('MBA, DIM', 'MBA,DIMET') #for herbicide Dicamba, Dimet.Salt
            temp13 = temp12.replace('4-D, 2', '4-D,2') #for herbicide 2,4-D,2-EHE
            temp14 = temp13.replace('MBA, SOD','MBA,SOD') #for herbicide Dicamba, Sodium Salt
            temp15 = temp14.replace('MBA, DIG','MBA,DIG') #for herbicide Dicamba, Digly.Salt
            temp16 = temp15.replace('4-D, BE', '4-D,BE') #for herbicide 2,4-D,BEE
            temp17 = temp16.replace('4-D, DI', '4-D,DI') #for herbicide 2,4-D,Dimeth.salt
            temp18 = temp17.replace('CPA, SOD', 'CPA,SOD') #for herbicide MCBA,Sodium salt
            temp19 = temp18.replace('RAM, K', 'RAM,K') #for herbicide Picloram, K Salt
            temp20 = temp19.replace('4-DB, DIM', '4-DB,DIM') #for herbicide 2,4-DB,Dimeth.salt
            temp21 = temp20.replace('RFEN, SOD', 'RFEN,SOD') #for herbicide Acifluoren, Sodium
            temp22 = temp21.replace('ZAPYR, ISO', 'ZAPYR,ISO') #for herbicide Imazapyr, iso. Salt
            temp23 = temp22.replace('4-D, ISO', '4-D,ISO') #for herbicide 2,4-D, Isoprop. salt
            temp24 = temp23.replace('ZAPYR, AMM', 'ZAPYR,AMM') #for herbicide Imazethapyr, ammon.
            temp25 = temp24.replace('QUIN, MON', 'QUIN,MON') #for herbicide Imazaquin, mon. Salt
            temp26 = temp25.replace('4-D, CHL', '4-D,CHL') #for herbicide 2,4-D, Chlorine salt
            temp27 = temp26.replace('CPA, 2-E', 'CPA,2-E') #for herbicide MCBA,2-Ethylhexyl
            temp28 = temp27.replace('PP-P, DMA', 'PP-P,DMA') #for herbicide MCPP-P, DMA Salt
            chems = temp27.split(', ') #splits the string into a list of strings

            cursor.execute("""
            SELECT ApplicationInLBS FROM Herbicide
            WHERE Crop = %s AND State = %s AND Year = %s
            """,(crop,state,year))
            for d in cursor:
                application.append(d)#adds sql results to list

            #turns list to string. cleans it so it can be turned into a list for matplotlib
            temp1 = str(application).replace('applicationinlbs','')
            temp2 = temp1.replace(':','')
            temp3 = temp2.replace('{','')
            temp4 = temp3.replace('}','')
            temp5 = temp4.replace('[','')
            temp6 = temp5.replace(']','')
            temp7 = temp6.replace('(','')
            temp8 = temp7.replace(')','')
            temp9 = temp8.replace("'","")
            #the next two lines are tricky. matplotlib graphs wont register choices if their value is 0 so I set it to the next lowest possible integer 1
            temp10 = temp9.replace('NULL','1') #Within Herbicide there are chem that were documented as used but not given values
            temp11 = temp10.replace(' 0', '1') #This is due to a lack of records and this is the only way that matplotlib can render the graph
            temp = temp11.split(', ') #makes temp into a list of strings

            data = []
            for i in temp: #converts list of strings to list of integers
                data.append(int(i)) #iterates through list and changes all values to int

            #creates a bar graph using chems and data
            #matplotlib renders it in as a widget and allows users to zoom in on certain data points while scaling properly
            #widget allows them to zoom into individual chems and scales accordingly while letting users save them. also gives exact x, y coordinates
            #dislike that functonality comes at cost of a pop up window but in terms of functionality its more than worth the bang for its buck
        if len(data) == len(chems): #check to make sure the lists are the same size, cause if they're not then matplotlab can't render the image and gives a webpage crashing error
            plt.rcdefaults()
            fig, ax = plt.subplots()
            y_pos=np.arange(len(chems))
            ax.barh(y_pos, data, align = 'center')
            ax.set_yticks(y_pos)
            ax.set_yticklabels(chems)
            ax.invert_yaxis()
            ax.get_xaxis().get_major_formatter().set_scientific(False) #keeps values in data from showing up in scientific notation
            ax.set_xlabel('Application in Pounds')
            ax.set_title('Herbicide Usage')
            plt.show()
            plt.close()
            return('')
        else:
            print("Whoops something went wrong!")
            return(data,chems)#for error events/debugging
        
#the next three "crop"Future() functions are just static sql calls that return their results in list form
def cornFuture():
    table = list()
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute("""SELECT * FROM Future WHERE Crop = 'Corn'""")
        for d in cursor:
            table.append(d)
        return(table)
def cottonFuture():
    table = list()
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute("""SELECT * FROM Future WHERE Crop = 'Cotton'""")
        for d in cursor:
            table.append(d)
        return(table)
def soybeanFuture():
    table = list()
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute("""SELECT * FROM Future WHERE Crop = 'Soybeans'""")
        for d in cursor:
            table.append(d)
        return(table)

def get_future(crop): #since future is so short (5 years) this is a full proof list method. matplotlib widget grants even more functionality and automatic scaling which is nice
        x= [2019,2020,2021,2022,2023,2024]
        if crop == 'Corn':
            cornYaxisPlanted= [89.5,89.5,89.0,89.0,89.0,89.0]
            cornYaxisHarvested= [81.9,81.9,81.4,81.4,81.4,81.4]
            plt.plot(x,cornYaxisPlanted, color = 'blue')
            plt.plot(x,cornYaxisHarvested, color = 'green')
            plt.gca().legend(('Corn Planted','Corn Harvested'))
            plt.title('Future Corn Yield Projections')
        elif crop == 'Cotton':
            cottonYaxisPlanted=[9.9,10.0,10.1,10.2,10.3,10.4]
            cottonYaxisHarvested=[8.4,8.5,8.6,8.7,8.8,8.8]
            plt.plot(x,cottonYaxisPlanted, color = 'blue')
            plt.plot(x,cottonYaxisHarvested, color = 'green')
            plt.gca().legend(('Cotton Planted','Cotton Harvested'))
            plt.title('Future Cotton Yield Projections')
        elif crop == 'Soybeans':
            soyYaxisPlanted=[78.5,78.5,79.0,79.0,79.0,79.0]
            soyYaxisHarvested=[77.6,77.6,78.1,78.1,78.1,78.1]
            plt.plot(x,soyYaxisPlanted, color = 'blue')
            plt.plot(x,soyYaxisHarvested, color = 'green')
            plt.gca().legend(('Soybeans Planted','Soybeans Harvested'))
            plt.title('Future Soybeans Yield Projections')

        plt.xlabel('Year', fontsize=14)
        plt.ylabel('Amount in Acres (per million)')
        plt.grid(True)
        plt.show()
        return('')
