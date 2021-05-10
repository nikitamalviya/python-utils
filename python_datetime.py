import datetime

def convert_str_to_datetime(mydatetime):
    mydatetime = mydatetime[0].split("+")[0]
    mydatetime = datetime.datetime.strptime(mydatetime,'%Y-%m-%d %H:%M:%S.%f')
    return mydatetime

def convert_datetime_to_str(date_= datetime.datetime.today()):
    if isinstance(date_, datetime.datetime) or type(date_)==str:
        date_ = date_.__str__()
        date_ = date_.split("+")[0]
        date_ = datetime.datetime.strptime(date_, '%Y-%m-%d %H:%M:%S.%f')
        print("convert_datetime_to_str : ", date_)
        return date_
    else:
        return date_

def get_date_time():
    date_= datetime.datetime.today()
    date_time_string = datetime.datetime.strptime(str(date_), '%Y-%m-%d %H:%M:%S.%f')
    print("get_date_time : ", date_time_string)
    return date_time_string

def get_date(date_= datetime.datetime.today()):
    date_string = date_.strftime('%m/%d/%Y')
    print("get_date : ", date_string)
    return date_string

def get_time(date_= datetime.datetime.today()):
    time_string = date_.strftime("%H:%M:%S")
    print("get_time : ", time_string)
    return time_string


o = datetime.datetime.today()

get_date_time()
get_date(datetime.datetime.today())
get_time(datetime.datetime.today())
convert_datetime_to_str(datetime.datetime.today())



