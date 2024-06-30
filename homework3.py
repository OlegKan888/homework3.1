from datetime import datetime
date = "2023.11.01"


def get_days_from_today(date):
    new_date = datetime.strptime(date, "%Y.%m.%d").date() #перетворення рядкового формату в datetame
    date_now = datetime.today().date() # визначення поточної дати
    date_delta = date_now - new_date # визначення різниці між поточною та заданою датами
    print (date_delta.days) 
    return

get_days_from_today(date)
    
    
        
    