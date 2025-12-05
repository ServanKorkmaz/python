from datetime import date

def find_age(b_year, b_month, b_day):
    today = date.today()
    
    age = today.year - b_year

    # hvis personnen ikke har hatt bursdag i år.
    if (today.month, today.day) < (b_month, b_day):
        age -= 1

    return age



print(find_age(2002, 1,1))



