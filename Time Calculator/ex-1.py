time_calculator = ['11:30 AM', '2:32']
time_ampm = time_calculator[0]
time_add = time_calculator[1]
total_time = list()
ampm_list = list()
am_list = ['AM']
total_minutes = 0
total_hours = 0
time_ampm = time_ampm.split()
time = time_ampm[0]
ampm = time_ampm[1]
ampm_list.append(ampm)
total_time.append(time)
total_time.append(time_add)
am = any(x in ampm_list for x in am_list)
add_twelve = 0
for item in total_time:
    if am == True:
        total_time = item.split(':')
        hour = int(total_time[0])
        total_hours += hour
        minutes = int(total_time[1])
        total_minutes += minutes
    else:
        total_time = item.split(':')
        if add_twelve == 0:
            hour = int(total_time[0]) + 12
        else:
            hour = int(total_time[0])
        total_hours += hour
        minutes = int(total_time[1])
        total_minutes += minutes
        add_twelve += 1
if total_minutes < 60:
    days_passed = int(total_hours/24)
    if days_passed == 0 and am == True:
        if total_hours < 12:
            new = '{}:{} AM'.format(total_hours,total_minutes)
        else:
            total_hours = total_hours - 12
            new = '{}:{} PM'.format(total_hours,total_minutes)
    elif days_passed == 0:
        total_hours = total_hours - 12
        new = '{}:{} PM'.format(total_hours,total_minutes)
    elif days_passed == 1 and am == True:
        total_hours = total_hours - 24
        if total_hours < 12:
            new = '{}:{} AM (next day)'.format(total_hours,total_minutes)
        else:
            total_hours = total_hours - 12
            new = '{}:{} PM (next day)'.format(total_hours,total_minutes)    
    elif days_passed == 1:
        total_hours = total_hours - 12
        new = '{}:{} PM (next day)'.format(total_hours,total_minutes)
    elif am == True:
        div_hours = int(total_hours / 24)
        total_hours = total_hours - 24*div_hours
        if total_hours < 12:
            new = '{}:{} AM ({} days later)'.format(total_hours,total_minutes,days_passed)
        else:
            total_hours = total_hours - 12
            new = '{}:{} PM ({} days later)'.format(total_hours,total_minutes,days_passed)
    else:
        div_hours = int(total_hours / 24)
        total_hours = total_hours - 24*div_hours
        if total_hours < 12:
            new = '{}:{} AM ({} days later)'.format(total_hours,total_minutes,days_passed)
        else:
            total_hours = total_hours - 12
            new = '{}:{} PM ({} days later)'.format(total_hours,total_minutes,days_passed)
else:
    add_hours = int(total_minutes / 60)
    total_minutes = total_minutes % 60
    total_hours = add_hours + total_hours
    days_passed = int(total_hours/24)
    if days_passed == 0 and am == True:
        if total_hours < 12 and total_minutes < 10:
            new = '{}:0{} AM'.format(total_hours,total_minutes)
        elif total_hours < 12 and total_minutes >= 10:
            new = '{}:{} AM'.format(total_hours,total_minutes)
        else:
            if total_minutes < 10:
                new = '{}:0{} PM'.format(total_hours,total_minutes)
            else:
                new = '{}:{} PM'.format(total_hours,total_minutes)
    elif days_passed == 0:
        if total_hours < 12 and total_minutes < 10:
            new = '{}:0{} AM'.format(total_hours,total_minutes)
        elif total_hours < 12 and total_minutes >= 10:
            new = '{}:{} AM'.format(total_hours,total_minutes)
        else:
            total_hours = total_hours - 12
            if total_minutes < 10:
                new = '{}:0{} PM'.format(total_hours,total_minutes)
            else:
                new = '{}:{} PM'.format(total_hours,total_minutes)
    elif days_passed == 1 and am == True:
        total_hours = total_hours - 24
        if total_hours < 12 and total_minutes < 10:
            new = '{}:0{} AM (next day)'.format(total_hours,total_minutes)
        elif total_hours < 12 and total_minutes >= 10:
            new = '{}:{} AM (next day)'.format(total_hours,total_minutes)
        else:
            if total_minutes < 10:
                new = '{}:0{} PM (next day)'.format(total_hours,total_minutes)
            else:
                new = '{}:{} PM (next day)'.format(total_hours,total_minutes)
    elif days_passed == 1:
        total_hours = total_hours - 24
        if total_hours < 12 and total_minutes < 10:
            new = '{}:0{} AM (next day)'.format(total_hours,total_minutes)
        elif total_hours < 12 and total_minutes >= 10:
            new = '{}:{} AM (next day)'.format(total_hours,total_minutes)
        else:
            total_hours = total_hours - 12
            if total_minutes < 10:
                new = '{}:0{} PM (next day)'.format(total_hours,total_minutes)
            else:
                new = '{}:{} PM (next day)'.format(total_hours,total_minutes)
    elif am == True:
        div_hours = int(total_hours / 24)
        total_hours = total_hours - 24*div_hours
        if total_hours < 12 and total_minutes < 10:
            new = '{}:0{} AM ({} days later)'.format(total_hours,total_minutes,days_passed)
        elif total_hours < 12 and total_minutes >= 10:
            new = '{}:{} AM ({} days later)'.format(total_hours,total_minutes,days_passed)
        else:
            if total_minutes < 10:
                new = '{}:0{} PM ({} days later)'.format(total_hours,total_minutes,days_passed)
            else:
                new = '{}:{} PM ({} days later)'.format(total_hours,total_minutes,days_passed)
    else:
        div_hours = int(total_hours / 24)
        total_hours = total_hours - 24*div_hours
        if total_hours < 12 and total_minutes < 10:
            new = '{}:0{} AM ({} days later)'.format(total_hours,total_minutes,days_passed)
        elif total_hours < 12 and total_minutes >= 10:
            new = '{}:{} AM ({} days later)'.format(total_hours,total_minutes,days_passed)
        else:
            total_hours = total_hours - 12
            if total_minutes < 10:
                new = '{}:0{} PM ({} days later)'.format(total_hours,total_minutes,days_passed)
            else:
                new = '{}:{} PM ({} days later)'.format(total_hours,total_minutes,days_passed)
print(new)

    


