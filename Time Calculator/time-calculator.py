week = {'Monday':0,'Tuesday':1,'Wednesday':2,'Thursday':3,'Friday':4,'Saturday':5,'Sunday':6}
def add_time(a,b,c = None):
    total_time = a + b
    total_day_hours = 24
    total_days = int(total_time/total_day_hours)
    day_time = total_time - total_days*total_day_hours
    if c == None:
        def manha_tarde():
        # define if day_time is am or pm
            if day_time < total_day_hours/2:
                return('{} AM'.format(day_time))
            else:
                return('{} PM'.format(day_time)) 
        if total_days == 0:
            return(manha_tarde())
        else:
            ampm_1 = manha_tarde()
            if total_days == 1:
                return('{} (next day)'.format(ampm_1))
            else:
                return('{} ({} days later)'.format(ampm_1,total_days))
    else:
        def semana():
            for key in week:
                if key == c:
                    number_of_week = week[key]
                    number_of_day = number_of_week + total_days
                    if number_of_day < 7:
                        for key in week:
                            if week[key] == number_of_day:
                                return(key)   
                    else:
                        for key in week:
                            if week[key] == number_of_day % 6:
                                return(key)   
        def manha_tarde():
        # define if day_time is am or pm
            if day_time < total_day_hours/2:
                return('{} AM'.format(day_time))
            else:
                return('{} PM'.format(day_time)) 
        if total_days == 0:
            ampm_1 = manha_tarde()
            day = semana()
            return('{},{}'.format(ampm_1,day))
        else:
            ampm_1 = manha_tarde()
            day = semana()
            if total_days == 1:
                return('{}, {}'.format(ampm_1),day)
            else:
                return('{}, {} ({} days later)'.format(ampm_1,day,total_days))

new_time = add_time(12,48,'Wednesday')
print(new_time)

