from datetime import date
current_date = date.today()

year, month, day = current_date.year, current_date.month, current_date.day

def find_age(birth_year, birth_month, birth_day):
    age = year - birth_year     # foreløpig alder. year = nåværende år. birth_year = fødselsår.
    
    # hvis fødselsdagen ikke har hatt bursdag i år.
    if month < birth_month or (month == birth_month and day < birth_day):
        age -= 1

    return age



