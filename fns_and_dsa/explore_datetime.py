from datetime import datetime , timedelta

def display_current_datetime():
    
     current_date  = datetime.now()
     print("Current date and time:", current_date.strftime("%Y-%m-%d  %H:%M:%S"))
 
display_current_datetime()     



def calculate_future_date():
    
     today = datetime.now()
     days_to_add = int(input("Enter the number of days to add to the current date:"))
     future_date = today + timedelta(days=days_to_add)
     print("Future date:", future_date.strftime("%Y-%m-%d"))
   
calculate_future_date()    