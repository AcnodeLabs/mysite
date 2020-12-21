from datetime import datetime

currentSecond= datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year

def todayis():
    return str(currentDay) + '/'+ str(currentMonth)+'/'+str(currentYear)

def dtg():
    return str(currentYear) + '_'+ str(currentMonth)+'_'+str(currentDay) +'T'+ str(currentHour) + '_'+ str(currentMinute)

print(dtg())
