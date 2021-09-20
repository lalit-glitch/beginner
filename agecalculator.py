import datetime

def ageCalculator(y, m, d):
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days/ 365)
    print(age)

ageCalculator(1999, 10, 22)