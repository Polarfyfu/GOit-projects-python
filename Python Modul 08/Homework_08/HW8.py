#Task 8

from datetime import datetime, timedelta
users = [{ 'name': 'Platon', 'birthday' : '2004-05-19'},
         { 'name': 'Andrew', 'birthday' : '1967-05-18'},
         { 'name': 'Bogdan', 'birthday' : '1983-05-18'},
         { 'name': 'Andrew', 'birthday' : '1994-05-22'}] # список сотрудников и их дней рождений

def congratulate(users):
    weekday = {'Monday': [],
               'Tuesday': [],
               'Wednesday': [],
               'Thursday': [],
               'Friday': [],
               'Next Monday': []}
    current_day = datetime.now().date()
    end = current_day + timedelta(days = 7) #end of week

    for i in users:
        bday = datetime.strptime(i['birthday'], '%Y-%m-%d') # day of born
        bday1 = datetime(current_day.year, bday.month, bday.day) # bday this year
        if current_day <= bday1.date() <= end:
            if bday1.weekday() == 0:
                weekday['Monday'].append(i['name'])
            elif bday1.weekday() == 1:
                weekday['Tuesday'].append(i['name'])
            elif bday1.weekday() == 2:
                weekday['Wednesday'].append(i['name'])
            elif bday1.weekday() == 3:
                weekday['Thursday'].append(i['name'])
            elif bday1.weekday() == 4:
                weekday['Friday'].append(i['name'])
            else :
                weekday['Next Monday'].append(i['name'])

    for k,v in weekday.items():
        if len(weekday[f'{k}']) > 0:
            print(k + ' : ' + ','.join(v))


    return users



congratulate(users)


