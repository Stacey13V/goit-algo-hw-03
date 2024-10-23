from datetime import datetime

def get_days_from_today(date=""):
    try:
        user_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        delta_days =  current_date - user_date 
        days_difference = int(delta_days.days)
        print (f"The difference between the entered date and current date is {days_difference} days")

    except ValueError:
        print (f'Oops!  That was no valid format. Please enter the date in the YYYY-MM-DD format!') 

    finally:
        print( '-' * 90) 

get_days_from_today("2021-10-09")     