def add_time(a,b,c=None):

    time_ampm = a.split()
    time = time_ampm[0]
    ampm = time_ampm[1]
    time_add = b

    time_list = list()
    time_list.append(time)
    time_list.append(time_add)

    ampm_list = list()
    ampm_list.append(ampm)

    pm_list = ['PM']
    pm = any(x in ampm_list for x in pm_list)
    total_minutes = 0
    total_hours = 0
    add_twelve = True

    for item in time_list:
        if pm == False:
            time_list = item.split(':')
            hour = int(time_list[0])
            total_hours += hour
            minutes = int(time_list[1])
            total_minutes += minutes

        elif pm == True:
            time_list = item.split(':')
            if add_twelve == True:
                hour = int(time_list[0]) + 12
            else:
                hour = int(time_list[0])
            total_hours += hour
            minutes = int(time_list[1])
            total_minutes += minutes
            add_twelve = False   

    if total_minutes >= 60:
        add_hours = int(total_minutes / 60)
        total_minutes = total_minutes % 60
        total_hours = add_hours + total_hours
    
    else:
        pass

    n = int(total_hours/24)
    total_hours = total_hours - 24*n
    
    if c == None:

        if n < 1:

            if total_minutes >= 10:
                if total_hours == 0:
                    total_hours = total_hours + 12
                    return('{}:{} AM'.format(total_hours,total_minutes))
                
                elif total_hours < 12:
                    return('{}:{} AM'.format(total_hours,total_minutes))
                
                elif total_hours == 12:
                    return('{}:{} PM'.format(total_hours,total_minutes))
                
                elif total_hours > 12:
                    total_hours = total_hours - 12
                    return('{}:{} PM'.format(total_hours,total_minutes))

            elif total_minutes < 10:
                if total_hours == 0:
                    total_hours = total_hours + 12
                    return('{}:0{} AM'.format(total_hours,total_minutes))

                elif total_hours < 12:
                    return('{}:0{} AM'.format(total_hours,total_minutes))
                
                elif total_hours == 12:
                    return('{}:0{} PM'.format(total_hours,total_minutes))
                
                elif total_hours > 12:
                    total_hours = total_hours - 12
                    return('{}:0{} PM'.format(total_hours,total_minutes))

                
        elif n == 1:
            
            if total_minutes >= 10:
                if total_hours == 0:
                    total_hours = total_hours + 12
                    return('{}:{} AM (next day)'.format(total_hours,total_minutes))

                elif total_hours < 12:
                    return('{}:{} AM (next day)'.format(total_hours,total_minutes))
                
                elif total_hours == 12:
                    return('{}:{} PM (next day)'.format(total_hours,total_minutes))
                
                elif total_hours > 12:
                    total_hours = total_hours - 12
                    return('{}:{} PM (next day)'.format(total_hours,total_minutes))

            elif total_minutes < 10:
                if total_hours == 0:
                    total_hours = total_hours + 12
                    return('{}:0{} AM (next day)'.format(total_hours,total_minutes))
                
                elif total_hours < 12:
                    return('{}:0{} AM (next day)'.format(total_hours,total_minutes))
                
                elif total_hours == 12:
                    return('{}:0{} PM (next day)'.format(total_hours,total_minutes))
                
                elif total_hours > 12:
                    total_hours = total_hours - 12
                    return('{}:0{} PM (next day)'.format(total_hours,total_minutes))

        elif n > 1:
            
            if total_minutes >= 10:
                if total_hours == 0:
                    total_hours = total_hours + 12
                    return('{}:{} AM ({} days later)'.format(total_hours,total_minutes,n))

                elif total_hours < 12:
                    return('{}:{} AM ({} days later)'.format(total_hours,total_minutes,n))
                
                elif total_hours == 12:
                    return('{}:{} PM ({} days later)'.format(total_hours,total_minutes,n))
                
                elif total_hours > 12:
                    total_hours = total_hours - 12
                    return('{}:{} PM ({} days later)'.format(total_hours,total_minutes,n))

            elif total_minutes < 10:
                if total_hours == 0:
                    total_hours = total_hours + 12
                    return('{}:0{} AM ({} days later)'.format(total_hours,total_minutes,n))

                elif total_hours < 12:
                    return('{}:0{} AM ({} days later)'.format(total_hours,total_minutes,n))
                
                elif total_hours == 12:
                    return('{}:0{} PM ({} days later)'.format(total_hours,total_minutes,n))
                
                elif total_hours > 12:
                    total_hours = total_hours - 12
                    return('{}:0{} PM ({} days later)'.format(total_hours,total_minutes,n))

    else:
        weeklower = {'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5,'sunday':6}
        day = c.lower()

        def number():
            for key in weeklower:

                if key == day:
                    number_of_day = weeklower[key] + n

                    if number_of_day < 7:
                        for key in weeklower:
                            if weeklower[key] == number_of_day:
                                return(weeklower[key])   

                    else:
                        for key in weeklower:
                            if weeklower[key] == number_of_day % 7:
                                return(weeklower[key])
        
        num = number()

        week = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}

        def semana():
            for key in week:

                if week[key] == num:
                    return(key)
        
        day = semana()

        if n < 1:

            if total_minutes >= 10:
                if total_hours == 0:
                    total_hours = total_hours + 12
                    return('{}:{} AM, {}'.format(total_hours,total_minutes,day))
                
                elif total_hours < 12:
                    return('{}:{} AM, {}'.format(total_hours,total_minutes,day))
                
                elif total_hours == 12:
                    return('{}:{} PM, {}'.format(total_hours,total_minutes,day))
                
                elif total_hours > 12:
                    total_hours = total_hours - 12
                    return('{}:{} PM, {}'.format(total_hours,total_minutes,day))

            elif total_minutes < 10:
                if total_hours == 0:
                    total_hours = total_hours + 12
                    return('{}:0{} AM, {}'.format(total_hours,total_minutes,day))

                elif total_hours < 12:
                    return('{}:0{} AM, {}'.format(total_hours,total_minutes,day))
                
                elif total_hours == 12:
                    return('{}:0{} PM, {}'.format(total_hours,total_minutes,day))
                
                elif total_hours > 12:
                    total_hours = total_hours - 12
                    return('{}:0{} PM, {}'.format(total_hours,total_minutes,day))

        elif n == 1:
            
            if total_minutes >= 10:
                if total_hours == 0:
                    total_hours = total_hours + 12
                    return('{}:{} AM, {} (next day)'.format(total_hours,total_minutes,day))

                elif total_hours < 12:
                    return('{}:{} AM, {} (next day)'.format(total_hours,total_minutes,day))
                
                elif total_hours == 12:
                    return('{}:{} PM, {} (next day)'.format(total_hours,total_minutes,day))
                
                elif total_hours > 12:
                    total_hours = total_hours - 12
                    return('{}:{}, {} PM (next day)'.format(total_hours,total_minutes,day))

            elif total_minutes < 10:
                if total_hours == 0:
                    total_hours = total_hours + 12
                    return('{}:0{} AM, {} (next day)'.format(total_hours,total_minutes,day))
                
                elif total_hours < 12:
                    return('{}:0{} AM, {} (next day)'.format(total_hours,total_minutes,day))
                
                elif total_hours == 12:
                    return('{}:0{} PM, {} (next day)'.format(total_hours,total_minutes,day))
                
                elif total_hours > 12:
                    total_hours = total_hours - 12
                    return('{}:0{} PM, {} (next day)'.format(total_hours,total_minutes,day))

        elif n > 1:
            
            if total_minutes >= 10:
                if total_hours == 0:
                    total_hours = total_hours + 12
                    return('{}:{} AM, {} ({} days later)'.format(total_hours,total_minutes,day,n))

                elif total_hours < 12:
                    return('{}:{} AM, {} ({} days later)'.format(total_hours,total_minutes,day,n))
                
                elif total_hours == 12:
                    return('{}:{} PM, {} ({} days later)'.format(total_hours,total_minutes,day,n))
                
                elif total_hours > 12:
                    total_hours = total_hours - 12
                    return('{}:{} PM, {} ({} days later)'.format(total_hours,total_minutes,day,n))

            elif total_minutes < 10:
                if total_hours == 0:
                    total_hours = total_hours + 12
                    return('{}:0{} AM, {} ({} days later)'.format(total_hours,total_minutes,day,n))

                elif total_hours < 12:
                    return('{}:0{} AM, {} ({} days later)'.format(total_hours,total_minutes,day,n))
                
                elif total_hours == 12:
                    return('{}:0{} PM, {} ({} days later)'.format(total_hours,total_minutes,day,n))
                
                elif total_hours > 12:
                    total_hours = total_hours - 12
                    return('{}:0{} PM, {} ({} days later)'.format(total_hours,total_minutes,day,n))

new = add_time('8:16 PM', '466:02','tuesday')
print(new)