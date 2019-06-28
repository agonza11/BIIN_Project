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
    cropchoice = ['Corn', 'Cotton', 'Soybeans']
    crop = " "
    state = " "
    year = " "
    statechoice = " "
    yearchoice = " "
    if year == ' ':
        crop = request.form.get('crop')

        if crop == 'Corn':
            cropchoice = ['Corn','Cotton','Soybeans']
            statechoice = ['Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
            if state == ' ':
                state = request.form.get('state')
                if state == 'Indiana':
                    statechoice = ['Indiana','Illinois','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Iowa':
                    statechoice = ['Iowa','Illinois','Indiana','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Minnesota':
                    statechoice = ['Minnesota','Illinois','Indiana','Iowa','Kansas','Michigan','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Nebraska':
                    statechoice = ['Nebraska','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Ohio':
                    statechoice = ['Ohio','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Wisconsin':
                    statechoice = ['Wisconsin','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Michigan':
                    statechoice = ['Michigan','Illinois','Indiana','Iowa','Kansas','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Missouri':
                    statechoice = ['Missouri','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'South Dakota':
                    statechoice = ['South Dakota','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Illinois':
                    statechoice = ['Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Kansas':
                    statechoice = ['Kansas','Illinois','Indiana','Iowa','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'North Dakota':
                    statechoice = ['North Dakota','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Texas':
                    statechoice = ['Texas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
        elif crop == 'Cotton':
            cropchoice = ['Cotton','Corn','Soybeans']
            statechoice = ['Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
            if state == ' ':
                state = request.form.get('state')
                if state == 'Arkansas':
                    statechoice = ['Arkansas','Alabama','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state =='Mississippi':
                    statechoice = ['Mississippi','Alabama','Arkansas','California','Georgia','Lousiana','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Texas':
                    statechoice = ['Texas','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Alabama':
                    statechoice = ['Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'California':
                    statechoice = ['California','Alabama','Arkansas','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Georgia':
                    statechoice = ['Georgia','Alabama','Arkansas','California','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Louisiana':
                    statechoice = ['Lousiana','Alabama','Arkansas','California','Georgia','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Missouri':
                    statechoice = ['Missouri','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'North Carolina':
                    statechoice = ['North Carolina','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Tennesse':
                    statechoice = ['Tennessee','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
        elif crop == 'Soybeans':
            cropchoice = ['Soybeans','Corn','Cotton']
            statechoice = ['Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
            if state == ' ':
                state = request.form.get('state')
                if state == 'Arkansas':
                    statechoice = ['Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Illinois':
                    statechoice = ['Illinois','Arkansas','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Indiana':
                    statechoice = ['Indiana','Arkansas','Illinois','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Iowa':
                    statechoice = ['Iowa','Arkansas','Illinois','Indiana','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Minnesota':
                    statechoice = ['Minnesota','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Missouri':
                    statechoice = ['Missouri','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Nebraska':
                    statechoice = ['Nebraska','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Ohio':
                    statechoice = ['Ohio','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Kansas':
                    statechoice = ['Kansas','Arkansas','Illinois','Indiana','Iowa','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif  state == 'Michigan':
                    statechoice = ['Michigan','Arkansas','Illinois','Indiana','Iowa','Kansas','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Mississippi':
                    statechoice = ['Mississippi','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'North Dakota':
                    statechoice = ['North Dakota','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'South Dakota':
                    statechoice = ['South Dakota','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Wisconsin':
                    statechoice = ['Wisconsin','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
                    if year == ' ':
                        year = request.form.get('year')
        else:
            print('God Bless the USA')
    else:
        print("God Bless the U.S.A!")
    print(crop)
    print(state)
    print(year)
    return render_template('CropDB.html', crop = crop, state = state, year = year, yearchoice = yearchoice, cropchoice = cropchoice, statechoice = statechoice, production_function=production_function)

@app.route('/Herbicide_Usage/', methods=['GET','POST'])
def herbicide():
    cropchoice = ['Corn', 'Cotton', 'Soybeans']
    crop = " "
    state = " "
    year = " "
    statechoice = " "
    yearchoice = " "
    if year == ' ':
        crop = request.form.get('crop')

        if crop == 'Corn':
            cropchoice = ['Corn','Cotton','Soybeans']
            statechoice = ['Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
            if state == ' ':
                state = request.form.get('state')
                if state == 'Indiana':
                    statechoice = ['Indiana','Illinois','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Iowa':
                    statechoice = ['Iowa','Illinois','Indiana','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Minnesota':
                    statechoice = ['Minnesota','Illinois','Indiana','Iowa','Kansas','Michigan','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Nebraska':
                    statechoice = ['Nebraska','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Ohio':
                    statechoice = ['Ohio','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Wisconsin':
                    statechoice = ['Wisconsin','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas']
                    yearchoice = ['1990','1991','1992','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Michigan':
                    statechoice = ['Michigan','Illinois','Indiana','Iowa','Kansas','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Missouri':
                    statechoice = ['Missouri','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'South Dakota':
                    statechoice = ['South Dakota','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1993','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Illinois':
                    statechoice = ['Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Kansas':
                    statechoice = ['Kansas','Illinois','Indiana','Iowa','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1995','1996','1998','1999','2000','2001','2003','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'North Dakota':
                    statechoice = ['North Dakota','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','Ohio','South Dakota','Texas','Wisconsin']
                    yearchoice = ['1990','2000','2001','2003','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Texas':
                    statechoice = ['Texas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1991','1992','1993','1995','1996','1998','1999','2000','2001','2003','2005','2010','2014','2016']
                    if year == ' ':
                        year = request.form.get('year')
        elif crop == 'Cotton':
            cropchoice = ['Cotton','Corn','Soybeans']
            statechoice = ['Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
            if state == ' ':
                state = request.form.get('state')
                if state == 'Arkansas':
                    statechoice = ['Arkansas','Alabama','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2003','2005','2007','2010','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state =='Mississippi':
                    statechoice = ['Mississippi','Alabama','Arkansas','California','Georgia','Lousiana','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2003','2005','2007','2010','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Texas':
                    statechoice = ['Texas','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2003','2005','2007','2010','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Alabama':
                    statechoice = ['Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1997','1998','1999','2000','2003','2005','2007','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'California':
                    statechoice = ['California','Alabama','Arkansas','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2003','2005','2007','2015']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Georgia':
                    statechoice = ['Georgia','Alabama','Arkansas','California','Lousiana','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1996','1997','1998','1999','2000','2001','2003','2005','2007','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Louisiana':
                    statechoice = ['Lousiana','Alabama','Arkansas','California','Georgia','Mississippi','Missouri','North Carolina','Tennessee','Texas']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2003','2005','2007']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Missouri':
                    statechoice = ['Missouri','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','North Carolina','Tennessee','Texas']
                    yearchoice = ['1997','2000','2003','2007','2010','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'North Carolina':
                    statechoice = ['North Carolina','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','Tennessee','Texas']
                    yearchoice = ['1997','1998','1999','2000','2003','2005','2007','2010','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Tennesse':
                    statechoice = ['Tennessee','Alabama','Arkansas','California','Georgia','Lousiana','Mississippi','Missouri','North Carolina','Texas']
                    yearchoice = ['1996','1997','1998','1999','2000','2003','2005','2007','2010','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
        elif crop == 'Soybeans':
            cropchoice = ['Soybeans','Corn','Cotton']
            statechoice = ['Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
            if state == ' ':
                state = request.form.get('state')
                if state == 'Arkansas':
                    statechoice = ['Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Illinois':
                    statechoice = ['Illinois','Arkansas','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Indiana':
                    statechoice = ['Indiana','Arkansas','Illinois','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Iowa':
                    statechoice = ['Iowa','Arkansas','Illinois','Indiana','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Minnesota':
                    statechoice = ['Minnesota','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Mississippi','Missouri','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Missouri':
                    statechoice = ['Missouri','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Nebraska':
                    statechoice = ['Nebraska','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Ohio':
                    statechoice = ['Ohio','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Missouri','Nebraska','North Dakota','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Kansas':
                    statechoice = ['Kansas','Arkansas','Illinois','Indiana','Iowa','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1997','1998','1999','2000','2002','2004','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif  state == 'Michigan':
                    statechoice = ['Michigan','Arkansas','Illinois','Indiana','Iowa','Kansas','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1997','1998','1999','2000','2002','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Mississippi':
                    statechoice = ['Mississippi','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Nebraska','North Dakota','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1995','1996','1997','1998','1999','2000','2002','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'North Dakota':
                    statechoice = ['North Dakota','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','Ohio','South Dakota','Wisconsin']
                    yearchoice = ['1990','2000','2002','2004','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'South Dakota':
                    statechoice = ['South Dakota','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','Wisconsin']
                    yearchoice = ['1990','1991','1992','1993','1997','1998','1999','2000','2002','2004','2005','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
                elif state == 'Wisconsin':
                    statechoice = ['Wisconsin','Arkansas','Illinois','Indiana','Iowa','Kansas','Michigan','Minnesota','Mississippi','Nebraska','North Dakota','Ohio','South Dakota']
                    yearchoice = ['1990','1996','1997','2000','2002','2006','2012','2015','2017']
                    if year == ' ':
                        year = request.form.get('year')
        else:
            print('God Bless the Good Old USA')
    else:
        print("God Bless the U.S.A!")
    return render_template('herbicide.html', crop = crop, state = state, year = year, yearchoice = yearchoice, cropchoice = cropchoice, statechoice = statechoice, herbicide_function = herbicide_function)

@app.route('/Future_Projections/', methods = ['GET', 'POST'])
def future():
    crop = "NONE"

    if crop == 'NONE':
        crop = request.form.get('crop')
        if crop == 'Corn':
            ans = cornFuture()
        elif crop == 'Cotton':
            ans = cottonFuture()
        elif crop == 'Soybeans':
            ans = soybeanFuture()
        else:
            ans = "Bullocks"
    else:
        print("God Bless the U.S.A!")
    return render_template('future.html', crop = crop, ans = ans, corn=cornFuture, cotton=cottonFuture, soybean=soybeanFuture, get_future=get_future)

@app.route('/About/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
