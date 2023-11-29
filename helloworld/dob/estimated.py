import datetime
from datetime import date


def index(age):
    today = date.today()
    y = today.year - int(age)
    dob = f'{y}-{today.month}-{today.day}'
    da = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
    print(type(da))
    print(da)
    return da