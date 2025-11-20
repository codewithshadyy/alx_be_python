from datetime import datetime as dt, timedelta

def display_current_datetime():
    
     current_date  = dt.now()
     year = current_date.strftime("%Y")
     month= current_date.strftime("%m")
     date= current_date.strftime("%d")
     hour = current_date.strftime("%H")
     minutes= current_date.strftime("%M")
     Seconds= current_date.strftime("%S")
     print(f"Current date and time:{year}:{month}:{date} {hour}:{minutes}:{Seconds}")
 
display_current_datetime()     



def calculate_future_date():
    
     today = dt.now()
     days_to_add = int(input("Enter the number of days to add to the current date:"))
     future_date = today + timedelta(days=days_to_add)
     print("Future date:", future_date.strftime("%Y:%m:%d"))
   
calculate_future_date()    