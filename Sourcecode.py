import pandas as pd
from graphics import *

def login():
    win = GraphWin("Login", 960, 720)
    a = Image(Point(480, 160), "Gigi1.gif")
    a.draw(win)
    inputText1 = Entry(Point(550, 320), 15)
    inputText1.setText("")
    inputText1.draw(win)
    inputText2 = Entry(Point(550, 420), 15)
    inputText2.setText("")
    inputText2.draw(win)

    b = Rectangle(Point(385, 530), Point(455, 490))
    b.setFill("blue")
    b.draw(win)
    c = Rectangle(Point(505, 530), Point(575, 490))
    c.setFill("blue")
    c.draw(win)

    d = Text(Point(410, 320), "username: ")
    d.setSize(20)
    d.draw(win)
    e = Text(Point(410, 420), "password: ")
    e.setSize(20)
    e.draw(win)
    f = Text(Point(420, 510), "login")
    f.setTextColor("white")
    f.setSize(17)
    f.draw(win)
    j = Text(Point(540, 510), "reset")
    j.setTextColor("white")
    j.setSize(17)
    j.draw(win)

    win.getMouse()
    un = str(inputText1.getText())
    pw = str(inputText2.getText())

    while un != "qiji" or pw != "0000":
        if un != "qiji":
            h = Text(Point(780, 320), "username do not exist, please click retry")
            h.setSize(13)
            h.draw(win)
            win.getMouse()
            h.undraw()
            inputText1.setText("")
            inputText2.setText("")
            win.getMouse()
            un = str(inputText1.getText())
            pw = str(inputText2.getText())
        elif pw != "0000":
            i = Text(Point(780, 420), "password is incorrect, please click retry")
            i.setSize(13)
            i.draw(win)
            win.getMouse()
            i.undraw()
            inputText2.setText("")
            win.getMouse()
            un = str(inputText1.getText())
            pw = str(inputText2.getText())

    win.close()



def ld():
    win = GraphWin("load data", 960, 720)
    a = Image(Point(480, 160), "Gigi1.gif")
    a.draw(win)

    notice = Text(Point(480, 315), "please name your data file 'data.csv' and put it in the same folder as this python code")
    notice.setSize(13)
    notice.draw(win)

    fnb = Entry(Point(550, 360), 15)
    fnb.setText(".csv")
    fnb.draw(win)

    fnt = Text(Point(410, 360), "filename: ")
    fnt.setSize(20)
    fnt.draw(win)

    lr = Rectangle(Point(385, 460), Point(455, 420))
    lr.setFill("blue")
    lr.draw(win)

    lr = Rectangle(Point(505, 460), Point(575, 420))
    lr.setFill("blue")
    lr.draw(win)

    lb = Text(Point(420, 440), "load")
    lb.setTextColor("white")
    lb.setSize(17)
    lb.draw(win)

    rb = Text(Point(540, 440), "retry")
    rb.setTextColor("white")
    rb.setSize(17)
    rb.draw(win)

    win.getMouse()
    filename = str(fnb.getText())

    while filename != "data.csv":
        er = Text(Point(740, 360), "could not locate the file, please click retry")
        er.setSize(13)
        er.draw(win)
        win.getMouse()
        er.undraw()
        fnb.setText(".csv")
        win.getMouse()
        filename = str(fnb.getText())

    win.close()

    data = pd.read_csv(filename)
    return(data)



def dp(data):
    win = GraphWin("data processing", 960, 720)

    a = Text(Point(480, 360), "here are some basic summaries of your data, click here to see", )
    a.setSize(20)
    a.draw(win)

    c = Rectangle(Point(445, 460), Point(515, 420))
    c.setFill("blue")
    c.draw(win)

    b = Text(Point(480, 440), "here", )
    b.setTextColor("white")
    b.setSize(17)
    b.draw(win)

    lisvar = list(data.columns)
    numvar = len(lisvar)
    date = data['Date'].unique()
    dw = data['Days of the Week'].unique()

    win.getMouse()
    a.undraw()
    b.undraw()
    c.undraw()

    nvt = Text(Point(240,100), "# of variables:")
    nvt.setSize(20)
    nvt.draw(win)

    nv = Text(Point(550,100), numvar)
    nv.setSize(20)
    nv.draw(win)

    vt = Text(Point(240,200), "variables and # of unique values:")
    vt.setSize(20)
    vt.draw(win)

    d = 200
    for e in lisvar:
        va = Text(Point(550, d), e)
        va.setSize(20)
        va.draw(win)
        ua = Text(Point(700, d), len(data[e].unique()))
        ua.setSize(20)
        ua.draw(win)
        d+=30

    f = Text(Point(480,360),"unique values")
    f.setSize(22)
    f.draw(win)

    g = Text(Point(220,400),"Date")
    g.setSize(20)
    g.draw(win)

    op1 = (date[0],"-",date[-1])
    j = Text(Point(220, 425), op1)
    j.setSize(17)
    j.draw(win)

    h = Text(Point(480, 400), "Days of the Week")
    h.setSize(20)
    h.draw(win)

    l = 425
    for m in dw:
        udw = Text(Point(480, l), m)
        udw.setSize(17)
        udw.draw(win)
        l += 20

    i = Text(Point(740, 400), "Time")
    i.setSize(20)
    i.draw(win)

    tmin = pd.DataFrame.min(data['Time'])
    tmax = pd.DataFrame.max(data['Time'])
    op2 = (tmin, "-", tmax)
    k = Text(Point(740, 425), op2)
    k.setSize(17)
    k.draw(win)

    c = Rectangle(Point(380, 610), Point(580, 650))
    c.setFill("blue")
    c.draw(win)

    n = Text(Point(480, 630), "Data Visualization ")
    n.setTextColor("white")
    n.setSize(22)
    n.draw(win)

    win.getMouse()
    win.close()



def dvs():
    win = GraphWin("data visualization selection", 960, 720)

    data = pd.read_csv("data.csv")
    lisvar = list(data.columns)
    lisvar.pop()

    note1 = Text(Point(300, 300), "You can visualize your data by:")
    note1.setSize(20)
    note1.draw(win)

    c = 300
    for a in lisvar:
        b = Text(Point(660, c), a)
        b.setSize(16)
        b.draw(win)
        c += 20

    note2 = Text(Point(300, 420), "Visualize by:")
    note2.setSize(20)
    note2.draw(win)

    selb = Entry(Point(660, 420), 15)
    selb.setText("")
    selb.draw(win)

    gor = Rectangle(Point(780, 435), Point(820, 405))
    gor.setFill("blue")
    gor.draw(win)

    gob = Text(Point(800, 420), "Go")
    gob.setFill("white")
    gob.setSize(16)
    gob.draw(win)

    eb = Text(Point(689, 450), "press 'e' to exit the program")
    eb.setSize(16)
    eb.draw(win)
    ebt = win.getKey()
    if ebt == "e":
        win.close()
    else:
        eb.undraw()
        win.getMouse()
        sel = str(selb.getText())

        while sel not in lisvar:
            waring = Text(Point(689, 450), "please type in a valid input")
            waring.setSize(16)
            waring.draw(win)
            selb.setText("")
            win.getMouse()
            waring.undraw()
            sel = str(selb.getText())

        win.close()
        return (sel)



def dv1(data):
    win = GraphWin("data visualization 1", 960, 720)
    date = data['Date'].unique()

    inputText1 = Entry(Point(150, 50), 15)
    inputText1.setText("mm/dd/year")
    inputText1.draw(win)

    dateb = Text(Point(50, 50), "Date:")
    dateb.setSize(20)
    dateb.draw(win)

    visr = Rectangle(Point(245, 40), Point(315, 60))
    visr.setFill("blue")
    visr.draw(win)

    visr = Rectangle(Point(335, 40), Point(385, 60))
    visr.setFill("blue")
    visr.draw(win)

    visb = Text(Point(280, 50), "visualize")
    visb.setTextColor("white")
    visb.setSize(16)
    visb.draw(win)

    visb = Text(Point(360, 50), "reset")
    visb.setTextColor("white")
    visb.setSize(16)
    visb.draw(win)

    eb = Text(Point(720, 50), "press 'e' to return to visualization selection page")
    eb.setSize(16)
    eb.draw(win)
    ebt = win.getKey()
    if ebt == "e":
        win.close()
    else:
        eb.undraw()
        win.getMouse()

        inputdate = str(inputText1.getText())

        while inputdate not in date:
            waring = Text(Point(700, 50),
                          "the date is not in your dataset or the format is incorrect, please try again")
            waring.setSize(16)
            waring.draw(win)
            inputText1.setText("mm/dd/year")
            win.getMouse()
            waring.undraw()
            inputdate = str(inputText1.getText())

        df = data.loc[data['Date'] == inputdate]
        yasix = pd.DataFrame.max(df['# of Customer'])

        if yasix < 300:
            yasixmax = (yasix + 9) // 10 * 10
            y = 580 / yasixmax
            Text(Point(30, 120), yasixmax)
            a = 700
            for i in range(int(yasixmax / 10)):
                Text(Point(30, a), i * 10).draw(win)
                a = a - 10 * y
            Text(Point(30, 120), int(yasixmax)).draw(win)
        elif yasix < 5000:
            yasixmax = (yasix + 99) // 100 * 100
            y = 580 / yasixmax
            Text(Point(30, 120), yasixmax)
            a = 700
            for i in range(int(yasixmax / 100)):
                Text(Point(30, a), i * 100).draw(win)
                a = a - 100 * y
            Text(Point(30, 120), int(yasixmax)).draw(win)
        else:
            yasixmax = (yasix + 999) // 1000 * 1000
            y = 580 / yasixmax
            Text(Point(30, 120), yasixmax)
            a = 700
            for i in range(int(yasixmax / 1000)):
                Text(Point(30, a), i * 1000).draw(win)
                a = a - 1000 * y
            Text(Point(30, 120), int(yasixmax)).draw(win)

        time = df['Time'].unique()

        nr = len(time)
        intervals = round(870 / nr, 3)
        c = 60
        for b in df['# of Customer']:
            bar = Rectangle(Point(c, 700), Point(c + intervals, 700 - b * y))
            bar.setFill("dodgerblue")
            bar.draw(win)
            c = c + intervals

        e = 60
        for d in df['Time']:
            f = Text(Point(e, 710), int(d))
            f.draw(win)
            e = e + intervals
        Text(Point(930, 710), int(pd.DataFrame.max(df['Time']) + 1)).draw(win)
        win.getMouse()
        win.close()
        dv1(data)



def dv2(data):
    win = GraphWin("data visualization 2", 960, 720)

    inputText1 = Entry(Point(150, 50), 15)
    inputText1.setText("'17'")
    inputText1.draw(win)

    timeb = Text(Point(50, 50), "Time:")
    timeb.setSize(20)
    timeb.draw(win)

    visr = Rectangle(Point(245, 40), Point(315, 60))
    visr.setFill("blue")
    visr.draw(win)

    restr = Rectangle(Point(335, 40), Point(385, 60))
    restr.setFill("blue")
    restr.draw(win)

    visb = Text(Point(280, 50), "visualize")
    visb.setTextColor("white")
    visb.setSize(16)
    visb.draw(win)

    restb = Text(Point(360, 50), "reset")
    restb.setTextColor("white")
    restb.setSize(16)
    restb.draw(win)

    eb = Text(Point(720, 50), "press 'e' to return to visualization selection page")
    eb.setSize(16)
    eb.draw(win)
    ebt = win.getKey()
    if ebt == "e":
        win.close()
    else:
        eb.undraw()
        win.getMouse()

        inputtime = int(inputText1.getText())

        alltime = data['Time'].unique()

        while inputtime not in alltime:
            waring = Text(Point(700, 50),
                          "the time is not in your dataset or the format is incorrect, please try again")
            waring.setSize(16)
            waring.draw(win)
            inputText1.setText("'17'")
            win.getMouse()
            waring.undraw()
            inputtime = int(inputText1.getText())

        df = data.loc[data['Time'] == inputtime]

        yasix = pd.DataFrame.max(df['# of Customer'])

        if yasix < 300:
            yasixmax = (yasix + 9) // 10 * 10
            y = 580 / yasixmax
            Text(Point(30, 120), yasixmax)
            a = 700
            for i in range(int(yasixmax / 10)):
                Text(Point(30, a), i * 10).draw(win)
                a = a - 10 * y
            Text(Point(30, 120), int(yasixmax)).draw(win)
        elif yasix < 3000:
            yasixmax = (yasix + 99) // 100 * 100
            y = 580 / yasixmax
            Text(Point(30, 120), yasixmax)
            a = 700
            for i in range(int(yasixmax / 100)):
                Text(Point(30, a), i * 100).draw(win)
                a = a - 100 * y
            Text(Point(30, 120), int(yasixmax)).draw(win)
        else:
            yasixmax = (yasix + 999) // 1000 * 1000
            y = 580 / yasixmax
            Text(Point(30, 120), yasixmax)
            a = 700
            for i in range(int(yasixmax / 1000)):
                Text(Point(30, a), i * 1000).draw(win)
                a = a - 1000 * y
            Text(Point(30, 120), int(yasixmax)).draw(win)

        time = df['Time']

        nr = len(time)
        intervals = round(870 / nr, 3)
        c = 60
        for b in df['# of Customer']:
            bar = Rectangle(Point(c, 700), Point(c + intervals, 700 - b * y))
            bar.setFill("dodgerblue")
            bar.draw(win)
            c = c + intervals

        e = 60 + intervals / 2
        for d in df['Date']:
            f = Text(Point(e, 710), d)
            f.draw(win)
            e = e + intervals

        win.getMouse()
        win.close()
        dv2(data)



def dv3(data):
    win = GraphWin("data visualization 3", 960, 720)

    inputText1 = Entry(Point(250, 50), 15)
    inputText1.setText("'Monday'")
    inputText1.draw(win)

    timeb = Text(Point(100, 50), "Days of the week:")
    timeb.setSize(18)
    timeb.draw(win)

    restr = Rectangle(Point(335, 40), Point(405, 60))
    restr.setFill("blue")
    restr.draw(win)

    visr = Rectangle(Point(425, 40), Point(475, 60))
    visr.setFill("blue")
    visr.draw(win)

    restb = Text(Point(370, 50), "visualize")
    restb.setTextColor("white")
    restb.setSize(16)
    restb.draw(win)

    visb = Text(Point(450, 50), "reset")
    visb.setTextColor("white")
    visb.setSize(16)
    visb.draw(win)

    eb = Text(Point(720, 50), "press 'e' to return to visualization selection page")
    eb.setSize(16)
    eb.draw(win)
    ebt = win.getKey()
    if ebt == "e":
        win.close()
    else:
        eb.undraw()
        win.getMouse()

        inputdow = str(inputText1.getText())

        alldow = data['Days of the Week'].unique()

        while inputdow not in alldow:
            waring = Text(Point(700, 50), "the days of the week is not in your dataset or the format is incorrect")
            waring.setSize(14)
            waring.draw(win)
            inputText1.setText("'Monday'")
            win.getMouse()
            waring.undraw()
            inputdow = str(inputText1.getText())

        df = data.loc[data['Days of the Week'] == inputdow]
        unidats = df['Date'].unique()
        nc = []
        for a in unidats:
            noc = df.loc[data['Date'] == a]
            b = pd.DataFrame.sum(noc['# of Customer'])
            nc.append(b)

        yasix = max(nc)

        if yasix < 300:
            yasixmax = (yasix + 9) // 10 * 10
            y = 580 / yasixmax
            Text(Point(30, 120), yasixmax)
            a = 700
            for i in range(int(yasixmax / 10)):
                Text(Point(30, a), i * 10).draw(win)
                a = a - 10 * y
            Text(Point(30, 120), int(yasixmax)).draw(win)
        elif yasix < 3000:
            yasixmax = (yasix + 99) // 100 * 100
            y = 580 / yasixmax
            Text(Point(30, 120), yasixmax)
            a = 700
            for i in range(int(yasixmax / 100)):
                Text(Point(30, a), i * 100).draw(win)
                a = a - 100 * y
            Text(Point(30, 120), int(yasixmax)).draw(win)
        elif yasix < 30000:
            yasixmax = (yasix + 999) // 1000 * 1000
            y = 580 / yasixmax
            Text(Point(30, 120), yasixmax)
            a = 700
            for i in range(int(yasixmax / 1000)):
                Text(Point(30, a), i * 1000).draw(win)
                a = a - 1000 * y
            Text(Point(30, 120), int(yasixmax)).draw(win)
        else:
            yasixmax = (yasix + 9999) // 10000 * 10000
            y = 580 / yasixmax
            Text(Point(30, 120), yasixmax)
            a = 700
            for i in range(int(yasixmax / 10000)):
                Text(Point(30, a), i * 10000).draw(win)
                a = a - 10000 * y
            Text(Point(30, 120), int(yasixmax)).draw(win)

        nr = len(nc)
        intervals = round(870 / nr, 3)
        c = 60
        for b in nc:
            bar = Rectangle(Point(c, 700), Point(c + intervals, 700 - b * y))
            bar.setFill("dodgerblue")
            bar.draw(win)
            c = c + intervals

        e = 60 + intervals / 2
        for d in unidats:
            f = Text(Point(e, 710), d)
            f.draw(win)
            e = e + intervals

        win.getMouse()
        win.close()
        dv3(data)



def dvm(data):
    dv = dvs()
    if dv == "Date":
        dv1(data)
        dvm(data)
    elif dv == "Time":
        dv2(data)
        dvm(data)
    elif dv == "Days of the Week":
        dv3(data)
        dvm(data)



def main():
    login()
    data = ld()
    dp(data)
    dvm(data)



main()




