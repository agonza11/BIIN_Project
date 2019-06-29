flask import Flask, render_template, request, redirect, url_for, jsonify
from dbWeb import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/GMODef/')
def GMODef():
    return render_template('GMODef.html')

@app.route('/timeline/')
def timeline():
    return render_template('timeline.html')

@app.route('/Historical_Crop_Database/', methods = ['GET','POST'])
def historical():
    cropchoice = ['Corn', 'Cotton', 'Soybeans'] #sets the list for CropDB.html for the first dropdown list
    crop = " " #crop state year makes sure that all the sql variables are set to " "
    state = " "
    year = " "
    statechoice = " " #will get assigned based on crop chosen on cropchoice
    yearchoice = " "    #will get assigned based on crop and state selection made from cropchoice and statechoice
    if year == ' ':
        crop = request.form.get('crop')

        if crop == 'Corn':#assigns statechoice for corn
            cropchoice = ['Corn','Cotton','Soybeans']
            statechoice = ['Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
            if state == ' ':
                state = request.form.get('state')
                if state == 'Indiana':#reassigns statechoice to put Indiana at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Indiana','Illinois','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Iowa':#reassigns statechoice to put Iowa at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Iowa','Illinois','Indiana','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Minnesota':#reassigns statechoice to put Minnesota at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Minnesota','Illinois','Indiana','Iowa','Kansas','Michigan','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Nebraska':#reassigns statechoice to put Nebraska at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Nebraska','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Ohio':#reassigns statechoice to put Ohio at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Ohio','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Wisconsin':#reassigns statechoice to put Wisconsin at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Wisconsin','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Michigan': #reassigns statechoice to put Michigan at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Michigan','Illinois','Indiana','Iowa','Kansas','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Missouri':#reassigns statechoice to put Missouri at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Missouri','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'South Dakota':#reassigns statechoice to put South Dakota at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['South Dakota','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Illinois':#reassigns statechoice to put Illinois at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Kansas':#reassigns statechoice to put Kansas at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Kansas','Illinois','Indiana','Iowa','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'North Dakota':#reassigns statechoice to put North Dakota at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['North Dakota','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Texas':#reassigns statechoice to put Texas at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Texas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
        elif crop == 'Cotton':#sets cotton to the front of the list to make sql easier and assigns statechoice
            cropchoice = ['Cotton','Corn','Soybeans']
            statechoice = ['Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
            if state == ' ':
                state = request.form.get('state')
                if state == 'Arkansas':#reassigns statechoice to put Arkansas at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Arkansas','Alabama','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state =='Mississippi':#reassigns statechoice to put Mississippi at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Mississippi','Alabama','Arkansas','California','Georgia','Lousiana','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Texas':#reassigns statechoice to put Texas at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Texas','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Alabama':#reassigns statechoice to put Alabama at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'California':#reassigns statechoice to put California at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['California','Alabama','Arkansas','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Georgia':#reassigns statechoice to put Georgia at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Georgia','Alabama','Arkansas','California','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Louisiana':#reassigns statechoice to put Louisiana at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Lousiana','Alabama','Arkansas','California','Georgia','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Missouri':#reassigns statechoice to put Missouri at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Missouri','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'North Carolina':#reassigns statechoice to put North Carolina at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['North Carolina','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Tennesse':#reassigns statechoice to put Tennesse at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Tennessee','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
        elif crop == 'Soybeans':#sets soybeans to the front of the list to make sql easier and assigns statechoice
            cropchoice = ['Soybeans','Corn','Cotton']
            statechoice = ['Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
            if state == ' ':
                state = request.form.get('state')
                if state == 'Arkansas':#reassigns statechoice to put Arkansas at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Illinois':#reassigns statechoice to put Illinois at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Illinois','Arkansas','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Indiana':#reassigns statechoice to put Indiana at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Indiana','Arkansas','Illinois','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Iowa':#reassigns statechoice to put Iowa at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Iowa','Arkansas','Illinois','Indiana','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Minnesota':#reassigns statechoice to put Minnesota at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Minnesota','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Missouri':#reassigns statechoice to put Missouri at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Missouri','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Nebraska':#reassigns statechoice to put Nebraska at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Nebraska','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Ohio':#reassigns statechoice to put Ohio at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Ohio','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Kansas':#reassigns statechoice to put Kansas at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Kansas','Arkansas','Illinois','Indiana','Iowa','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif  state == 'Michigan':#reassigns statechoice to put Michigan at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Michigan','Arkansas','Illinois','Indiana','Iowa','Kansas','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Mississippi':#reassigns statechoice to put Mississippi at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Mississippi','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'North Dakota':#reassigns statechoice to put North Dakota at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['North Dakota','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'South Dakota':#reassigns statechoice to put South Dakota at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['South Dakota','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Wisconsin':#reassigns statechoice to put Wisconsin at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Wisconsin','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
        else:
            print('Ooops! There was an error.')
    else:
        print("Oops, there was an error!")
    print(crop)
    print(state)
    print(year)
    return render_template('CropDB.html', crop = crop, state = state, year = year, yearchoice = yearchoice, cropchoice = cropchoice, statechoice = statechoice, production_function=production_function)

@app.route('/Herbicide_Usage/', methods=['GET','POST'])
def herbicide():
    cropchoice = ['Corn', 'Cotton', 'Soybeans']
    crop = " "  #sets: crop state year statechoice and yearchoice to blank
    state = " "
    year = " "
    statechoice = " "
    yearchoice = " "
    if year == ' ':
        crop = request.form.get('crop')

        if crop == 'Corn':#assigns statechoice
            cropchoice = ['Corn','Cotton','Soybeans']
            statechoice = ['Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
            if state == ' ':
                state = request.form.get('state')
                if state == 'Indiana':#reassigns statechoice to put Indiana at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Indiana','Illinois','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Iowa':#reassigns statechoice to put Iowa at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Iowa','Illinois','Indiana','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Minnesota':#reassigns statechoice to put Minnesota at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Minnesota','Illinois','Indiana','Iowa','Kansas','Michigan','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Nebraska':#reassigns statechoice to put Nebraska at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Nebraska','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Ohio':#reassigns statechoice to put Ohio at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Ohio','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Wisconsin':#reassigns statechoice to put Wisconsin at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Wisconsin','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas']
                    yearchoice = ['1990','1991','1992','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Michigan':#reassigns statechoice to put Michigan at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Michigan','Illinois','Indiana','Iowa','Kansas','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Missouri':#reassigns statechoice to put Missouri at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Missouri','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'South Dakota':#reassigns statechoice to put South Dakota at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['South Dakota','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Illinois':#reassigns statechoice to put Illinois at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Kansas':#reassigns statechoice to put Kansas at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Kansas','Illinois','Indiana','Iowa','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1995','1996','1998','1999','2000','2001','2003','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'North Dakota':#reassigns statechoice to put North Dakota at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['North Dakota','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','2000','2001','2003','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Texas':#reassigns statechoice to put Texas at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Texas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1991','1992','1993','1995','1996','1998','1999','2000','2001','2003','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
        elif crop == 'Cotton': #sets cotton to the front of the cropchoice list and sets statechoices
            cropchoice = ['Cotton','Corn','Soybeans']
            statechoice = ['Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
            if state == ' ':
                state = request.form.get('state')
                if state == 'Arkansas':#reassigns statechoice to put Arkansas at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Arkansas','Alabama','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2003','2005','2007','2010','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state =='Mississippi':#reassigns statechoice to put Mississippi at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Mississippi','Alabama','Arkansas','California','Georgia','Lousiana','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2003','2005','2007','2010','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Texas':#reassigns statechoice to put Texas at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Texas','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2003','2005','2007','2010','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Alabama':#reassigns statechoice to put Alabama at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1997','1998','1999','2000','2003','2005','2007','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'California':#reassigns statechoice to put California at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['California','Alabama','Arkansas','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2003','2005','2007','2015']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Georgia':#reassigns statechoice to put Georgia at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Georgia','Alabama','Arkansas','California','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1996','1997','1998','1999','2000','2001','2003','2005','2007','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Louisiana':#reassigns statechoice to put Louisiana at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Lousiana','Alabama','Arkansas','California','Georgia','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2003','2005','2007']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Missouri':#reassigns statechoice to put Missouri at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Missouri','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','North Carolina','Tennessee','Texas']
                    yearchoice = ['1997','2000','2003','2007','2010','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'North Carolina':#reassigns statechoice to put North Carolina at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['North Carolina','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','Tennessee','Texas']
                    yearchoice = ['1997','1998','1999','2000','2003','2005','2007','2010','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Tennesse':#reassigns statechoice to put Tennesse at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Tennessee','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Texas']
                    yearchoice = ['1996','1997','1998','1999','2000','2003','2005','2007','2010','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
        elif crop == 'Soybeans': #moves soybeans to the front of cropchoice and assigns statechoice
            cropchoice = ['Soybeans','Corn','Cotton']
            statechoice = ['Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
            if state == ' ':
                state = request.form.get('state')
                if state == 'Arkansas':#reassigns statechoice to put Arkansas at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Illinois':#reassigns statechoice to put Illinois at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Illinois','Arkansas','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Indiana':#reassigns statechoice to put Indiana at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Indiana','Arkansas','Illinois','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Iowa':#reassigns statechoice to put Iowa at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Iowa','Arkansas','Illinois','Indiana','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Minnesota':#reassigns statechoice to put Minnesota at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Minnesota','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Missouri':#reassigns statechoice to put Missouri at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Missouri','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Nebraska':#reassigns statechoice to put Nebraska at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Nebraska','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Ohio':#reassigns statechoice to put Ohio at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Ohio','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Kansas':#reassigns statechoice to put Kansas at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Kansas','Arkansas','Illinois','Indiana','Iowa','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1997','1998','1999','2000','2002','2004','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif  state == 'Michigan':#reassigns statechoice to put Michigan at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Michigan','Arkansas','Illinois','Indiana','Iowa','Kansas','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1997','1998','1999','2000','2002','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Mississippi':#reassigns statechoice to put Mississippi at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Mississippi','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1995','1996','1997','1998','1999','2000','2002','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'North Dakota':#reassigns statechoice to put North Dakota at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['North Dakota','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','2000','2002','2004','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'South Dakota':#reassigns statechoice to put South Dakota at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['South Dakota','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1997','1998','1999','2000','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Wisconsin':#reassigns statechoice to put Wisconsin at the top of the list. Makes the sql query easier to process. also assigns year choices
                    statechoice = ['Wisconsin','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota']
                    yearchoice = ['1990','1996','1997','2000','2002','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
        else:
            print('Oops! An error occurred.')
    else:
        print("Something went wrong!")
    return render_template('herbicide.html', crop = crop, state = state, year = year, yearchoice = yearchoice, cropchoice = cropchoice, statechoice = statechoice, herbicide_function = herbicide_function)

@app.route('/Future_Projections/', methods = ['GET', 'POST'])
def future():
    crop = "NONE"
    #forces conditional loop to run
    if crop == 'NONE':
        crop = request.form.get('crop')
        if crop == 'Corn':
            ans = cornFuture()
        elif crop == 'Cotton':
            ans = cottonFuture()
        elif crop == 'Soybeans':
            ans = soybeanFuture()
        else:
            ans = "Error Unknown!"
    else:
        print("Error Unknown!")
    return render_template('future.html', crop = crop, ans = ans, corn=cornFuture, cotton=cottonFuture, soybean=soybeanFuture, get_future=get_future)

@app.route('/About/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
