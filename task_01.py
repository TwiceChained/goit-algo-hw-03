from datetime import datetime

def get_days_from_today(date_str):

    today = datetime.today().date()
    entered = datetime.strptime(date_str, "%Y-%m-%d").date()
    result = entered - today 
    return result.days



if __name__ == "__main__":
    user_input = input("Enter your date (YYYY-MM-DD): ")
    try:
        diff = get_days_from_today(user_input)
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
    else:
        print(f"Difference in days: {diff}")
