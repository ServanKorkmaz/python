from datetime import date
current_date = date.today()

year, month, day = current_date.year, current_date.month, current_date.day

def find_age(byear, bmonth, bday):
    age = year - byear
    if bmonth > month or (bmonth == month and bday > day):
        age -=1
    return age

print(find_age(2000, 10, 18)
)
