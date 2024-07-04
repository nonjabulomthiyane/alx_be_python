# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted current date and time
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    # Prompt the user to enter a number of days
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate future date
    future_date = current_date + timedelta(days=number_of_days)
    
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    # Print the formatted future date
    print(f"Future date after adding {number_of_days} days: {formatted_future_date}")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
