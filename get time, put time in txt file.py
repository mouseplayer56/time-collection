#IMPORTANT NOTE: run the code first before tampering with this crap.
#It'll give you a much better idea of what it does.
#also, i kept no patch logs of previous iterations before 1.3 lol

#1.3.0
# un-did a function that would terminate code, after realising new years exist.
# (the above was done on the 1st of january for reference.)

#1.4.0
# fixed loop transitioning to a new month ("SHOULD" no longer spam files).
# added some more flavour text in the form of notes.

#1.4.1
# if date (day) increments during loop, it should now show curdate as well. [INCOMPLETE]
# the above requires a 'date saver', which saves the date from when the program was first ran tb-used later.
# more flavour text.

#1.5.0
# ACTUALLY implemented the v1.4.1 patch (was detecting month instead of day). [INCOMPLETE]
# also, converts both dates back into integers for logic comparisons.
# updated v1.4.1 patch logs to be correct.

#1.6.0
# creates a new, separate file to count time spent per-day in ticks.
# doesn't use 1.4.1's feature of day incrementing *yet*.

#1.6.1
# fixes the patch that 1.5.0 claimed to fix in 1.4.1 (cleaner transition)

#1.6.2
# un-scrambles code so it actually writes in 'active[x].txt' files (it was literally 2 indents)

#1.7.0
# more commercially friendly, lets you 'customise' (choose) some stuff.
# you'll have to go through the code and manually input it into "global constants" though, so you get to see this jargon of commenting [not anymore]

#1.8.0
# fixes bug in active[x] files that passing midnight would crash the program
# it was two lines: close file in read only, and open file in append mode. kill me.
# also, this patch adds a completely new file to read settings. this means you can input settings at first-time launch and then just forget about it every other time for auto-running.
# hopefully fixed a bug where disabling activewrite would crash the program.

#--script that gets current date&time + puts it into a .txt file.
#--also makes a new file every month.

#time component
import datetime
import time
import os

#math component
import decimal

setf = open("t-config.txt", "a") #verifies file stability
setf.close()
setf = open("t-config.txt", "r")
setf.seek(0)
firstcharacter = setf.read(1)
if not firstcharacter: #if .txt is blank/new file created
    newConfig = 1 #blank op
    print("New User Detected -- Thanks for downloading! :)")
else:
    newConfig = 0 #normal op
    print("User already ran code, t-config.txt file is not empty")
setf.close()

if newConfig == 1: #this part makes/edits the settings file.
    counterwrite = True # failsafe
    activewrite = True
    n = 15 # failsafe end
    setf = open("t-config.txt", "w")
    time.sleep(1)
    print("This program does have a few customization options.")
    print("For a first-time user like yourself, this prompt will only come up once")
    print("There are default options if you want to skip ahead, otherwise you're free to customize some stuff.")
    usConfig = input("Do you want to use 'default' settings or 'custom' settings?: ").lower()
    if usConfig == "default": #if default is chosen, sets these then writes them in
        counterwrite = True
        activewrite = True
        n = 15
        setf.write("counterwrite = "+str(counterwrite)+"""
"""+"activewrite = "+str(activewrite)+"""
"""+"n = "+str(n))
        print("Default settings applied successfully.")

    while usConfig == "custom": # lets you change some stuff CLI and Y/N prompt style
        print("Here's some of the stuff you can configure:")
        print(""" 'activewrite' is the main counting component of the script. it makes an initial file and a new one each month to count the amount of time spent running the program.
 'counterwrite' is a minimised version of activewrite to save storage space for long-term use. it won't make new files - it only uses one file, and will sum up the total amount of time spent overall per day.
 'n' is, essentially, the amount of time in-between ticks in minutes. Each tick adds a new entry into your file, so it's recommended not to go too low on this value!""")
        usCusConfig = input("what variable would you like to change? ('exit' to leave & save changes): ").lower()

        while usCusConfig == "activewrite":
            usCusValConfig = input("What would you like to do with this component? ('True' or 'False'): ").lower()
            if usCusValConfig == "true":
                activewrite = True
                break
            elif usCusValConfig == "false":
                activewrite = False
                break
            else:
                print("retry", usCusValConfig)
                pass
            
        while usCusConfig == "counterwrite":
            usCusValConfig = input("What would you like to do with this component? ('True' or 'False'): ").lower()
            if usCusValConfig == "true":
                counterwrite = True
                break
            elif usCusValConfig == "false":
                counterwrite = False
                break
            else:
                print("retry", usCusValConfig)
                pass
            
        if usCusConfig == "n":
            usCusValConfig = int(input("What value would you like to change this to?: "))
            n = usCusValConfig
            usCusConfig = "blank"
            
        if usCusConfig == "exit":
            setf.write("counterwrite = "+str(counterwrite)+"""
"""+"activewrite = "+str(activewrite)+"""
"""+"n = "+str(n))
            usConfig = "t'hell with you" #malum necessarium
            break
setf.close()

if newConfig == 0: #this part actually reads the txt file. much less impressive size-wise.
    setf = open("t-config.txt", "r")
    for k in setf:
        if k[0:7] == "counter":
            counterwrite = bool(k[15:])
        if k[0:6] == "active":
            activewrite = bool(k[14:])
        if k[0:1] == "n":
            n = int(k[4:])

# v old constants that would've previously customised the program (obsolete due to new settings file)

##global constants - THESE CUSTOMISE THE PROGRAM!!!
#counterwrite = True # makes a separate file to count out minutes spent
#activewrite = True # makes separate files each month + counts time spent (requires a lot more space for longer hauls)
#n = 15 # amount of time (MIN) per tick. recommended to set higher than lower.

curdatetime = datetime.datetime.now()
curtime = curdatetime.time()
curdate = curdatetime.date()
vsNo="1.8.0"

print("version",vsNo)
print("date&time=",curdatetime)
print("time=",curtime)
print("date=",curdate)

#IMPORTANT function to check if file matches current date
def checkFileDate(curdate, firstline, monthNo):
    print("checkFileDate function ran")
    k = "needs date-a" #don't ask, it's too integral to change it now.
    while k == "needs date-a":
        monthNo = str(monthNo)
        if firstline[5:-3] == str(curdate)[5:-3]: #if the .txt matches current date
            print("'data["+monthNo+"]'","perfect data")
            k = "satisfied"
            print(k)
            break
        elif firstline[5:-3] < str(curdate)[5:-3]: #if the .txt is less than current date
            print("month=",firstline[5:-3])
            print("'data["+monthNo+"]'","this data is too old")
            k = "still unpleased"
            print(k)
        else: #if the .txt is greater than current date
            #k = "could not bust"
            if firstline[0:4] < str(curdate)[0:4]: #is it a new year?
                k = "still unpleased" #it's a new year
                print("it's a New Year: file yr=", firstline[0:4], "cur yr=", str(curdate)[0:4])
            else:
                k = "could not bust" #it feels like we only go backwards, baby
                print("something crazy happened: file yr=", firstline[0:4], "cur yr=", str(curdate)[0:4])
            print(k)
    return k

#file variables (inital)
monthNo = 1 #this isn't current, this is just the amount of months since program start
monthNo = str(monthNo) #lets var be concatenated for files (active+monthNo)

if activewrite == True: # 'activewrite' CHECK
    file = open("active"+monthNo+".txt", "a") #creates/verifies 'active1.txt' [if it is a thing]
    file.close()

    file = open("active"+monthNo+".txt", "r") #copied code - checks if active1 is blank
    file.seek(0)
    firstcharacter = file.read(1)
    if not firstcharacter: #if .txt is blank
        codeRed = 1 #blank op
        print("ERR: .txt is blank, codeRED")
    else:
        codeRed = 0 #normal op
    file.close()
    print("fileopen=","active"+monthNo+".txt")

    #opening 'active1.txt' component
    file = open("active1.txt")
    firstline = file.read(10)
    print("firstline=",firstline)

#loop to check which file you're editing
x=0 #maintain overall loop
i=0 #will run checkFileDate function

hostility = "a" #determines if [appending OR writing] times/dates



while x == 0 and activewrite == True: #this is the initial part of the code, to check files/names/etc.
    
    if codeRed == 1: #called if active1 is blank
        i=1
        finalk="satisfied"
        print("CODE RED: no 'active1.txt' content detected.")
        
    if i == 0:
        finalk = checkFileDate(curdate, firstline, monthNo) #returns k= satisfied, still unpleased, could not bust
    file.close()
    
    if finalk == "satisfied": #if all checks pass, it will write into the file.
        print("finalk is satisfied")
        file = open("active"+monthNo+".txt", hostility)
        file.seek(0)
        curdatetime = datetime.datetime.now()
        if i == 1: #if codeRed has been passed through successfully (main diff: codeRed doesn't write a new line, since it already starts on a blank line)
            file.write(str(curdate)+"""
"""+str(curtime)+" -- startup")
            print("set i=1")
            file.close()
        else:
            file.write("""
"""+str(curdate)+"""
"""+str(curtime)+" -- startup")
            file.close()
        x=1
        break
    
    i=0 # i m p o r t a n t
    
    if finalk == "still unpleased": #if something isn't write[sic], a new file is created.
        print("finalk is still unpleased")
        monthNo = int(monthNo)
        monthNo = monthNo + 1 #increments monthNo
        monthNo = str(monthNo)
        
        file = open("active"+monthNo+".txt", "a") #creates file/verifies integrity
        file.close()
        file = open("active"+monthNo+".txt", "r") #checks if its blank (newly created) or not (already used)
        file.seek(0)
        firstcharacter = file.read(1) #checks if there's any text on the 1st line
        if not firstcharacter: #if the file is blank (just created, no text)
            file.close()
            print("new blank file created, temporarily sleeping to avoid accidental spam.")
            time.sleep(3)
            i=1
            finalk = "satisfied"
            hostility = "w"
        file.close()
        
        file = open("active"+monthNo+".txt", "r")
        print("reading from=","active"+monthNo+".txt")
        firstline = file.read(10)
        file.close()
    else: #this should *ideally* only be called if something goes wrong
        print("sorry, codey brokey :(")
        x=-1
if hostility == "a": #adding onto file
    tranquility = "append"
if hostility == "w": #writing from blank
    tranquility = "write"
#'hostility' is basically just a way to universally change append/write status
print("mode=",tranquility)
if activewrite:
    print("firstline=",firstline[5:-3])

#re-running the code every n minutes. (sleep does it in seconds, so n*60)

x=0 #to keep it looping indefinitely
i=0 #checks for blankness
datesaver = curdate #saves date in case the day changes (4th to 5th, etc.)
print("saved date =",datesaver)
print("program is now in sleep mode; one tick will be printed every",str(n)+"mins")

hostility="a"

cnt=1 #counts ticks per cycle (every n mins should increment it by 1)
counterRED = 0 #0=txt is blank, 1=txt is not blank

if counterwrite == True:
    f2le = open("#counter.txt", "a")
    f2le.close()

    with open("#counter.txt", "r+") as f2le: #copied code - checks if active1 is blank
        f2le.seek(0)
        firstcharacter = f2le.read(1)
        if not firstcharacter: #if blank, don't make a new line to write in
            f2le.write(str(datesaver)+" (TICK at "+str(n)+"min intervals.)"+"""
"""+str(cnt))
            f2le.close()
        else:
            counterRED = 1

    if counterRED == 1: #if filled, make a new line to write in
        f2le = open("#counter.txt", "a")
        f2le.write("""
"""+str(datesaver)+" (TICK at "+str(n)+"min intervals.)"+"""
"""+str(cnt))
        f2le.close()

    with open('#counter.txt', 'r+') as f2le: #sets pos variable correctly, thanks stackoverflow/bing ai
        f2le.seek(0, os.SEEK_END)
        pos = f2le.tell() - 1
        print("initial pos=",pos)
        while pos > 0 and f2le.read(1) != "\n":
            pos -= 1
            print("pos=",pos)
            f2le.seek(pos, os.SEEK_SET)
        if pos > 0:
            print("pos>0, pos=",pos)
            f2le.seek(pos, os.SEEK_SET)
            f2le.truncate()
        f2le.write(str(cnt)+" Tick.")

#-----------------------------------------------------------------------Loop

while x == 0: #this is the loop part of the code. THIS IS THE LOOP PART OF THE CODE.
    #i literally copied this part from the main one, and ripped out a few print cmds
    time.sleep(n*60) #sleep ticks
    curdatetime = datetime.datetime.now()
    curtime = curdatetime.time()
    curdate = curdatetime.date()
    print("--TICK:",str(n)+"minutes;",str(curtime))

    if counterwrite == True:
        cnt += 1 #increments counter
        with open('#counter.txt', 'r+') as f2le: #overwrites last line with new counter
            f2le.seek(0, os.SEEK_END)
            if pos > 0:
                f2le.seek(pos, os.SEEK_SET)
                f2le.truncate()
            f2le.write(str(cnt)+" Ticks."+" ("+str(n*cnt)+"mins/"+str(round(((n*cnt)/60), 3))+"hrs overall)")

    if i == 0 and activewrite == True: #if file has text in it
        hostility="a"
        print("monthNo=",monthNo)
        file = open("active"+str(monthNo)+".txt", "r")
        firstline = file.read(10)
        finalk = checkFileDate(curdate, firstline, monthNo) #satisfied, still unpleased, could not bust
    file.close()

    strdatesaverday = str(datesaver)[8:10]
    strcurdateday = str(curdate)[8:10]
    
    file = open("active"+str(monthNo)+".txt", "r")
    newdayvar = 0 #local variable that gets reset every time
    if int(strdatesaverday)<int(strcurdateday): #tests if it's a new day
        newdayvar = 1 #allows newdayvar process to run
        print("new day")
        file.close()

    if newdayvar == 1 and activewrite == True:
        file = open("active"+str(monthNo)+".txt", "a")
        datesaver = curdate #sets datesaver to the current date, so it doesnt proc again unless its another new day
        file.write("""
"""+str(curdate)) #new line so it doesn't co-incide with other dates

    if finalk == "satisfied" and activewrite == True: #if all checks pass, it will write into the file.
        file = open("active"+str(monthNo)+".txt", hostility)
        file.seek(0)
        if i == 1: #if the file is blank, overwrites blank spaces
            file.write(str(curdate)+"""
"""+str(curtime))
            print("i=1") #tells the user vital info (no it doesnt)
        else: #if file is filled, it just adds on
            file.write("""
"""+str(curtime))
    file.close()
    
    i=0 # i m p o r t a n t
    print("i=0") #ditto
    
    if finalk == "still unpleased" and activewrite == True: #if something isn't write[sic], a new file is created.
        monthNo = int(monthNo)
        monthNo = monthNo + 1 #incremented
        monthNo = str(monthNo)
        
        file = open("active"+monthNo+".txt", "a") #create/verify file (integrity).
        file = open("active"+monthNo+".txt", "r")
        file.seek(0)
        firstcharacter = file.read(1) #checks if there's text on first line
        if not firstcharacter: #if blank:
            file.close()
            print("new blank file created, sleeping to avoid accidental spam.")
            time.sleep(3)
            i=1 #becomes important later on, since this file is blank
            finalk = "satisfied"
            hostility = "w"
        file.close()
        
        file = open("active"+monthNo+".txt", "r")
        firstline = file.read(10)
        
    elif finalk == "could not bust" and activewrite == True: #this should only be called if the file month > current month. except it's now redundant.
        print("sorry, codey brokey :(")
        x=-1 #because that's what a rational person would do

#.
#.
#.
#run(cryptominer.exe)
