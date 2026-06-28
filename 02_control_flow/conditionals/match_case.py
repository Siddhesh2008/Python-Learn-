#Match-case statement is a new feature introduced in Python 3.10 that allows for more
#  expressive and concise pattern matching. alternative for if-elif-else statements.
# It provides a way to match values against patterns and execute
#  code based on the matched pattern.

def day_of_week(day):
    match day:
        case "Monday":
            return "Start of the work week."
        case "Tuesday":
            return "Second day of the work week."
        case "Wednesday":
            return "Midweek day."
        case "Thursday":
            return "Almost the weekend."
        case "Friday":
            return "Last workday of the week."
        case "Saturday" | "Sunday":
            return "Weekend!"
        case _:
            return "Invalid day."

print(day_of_week("Monday"))    # Output: Start of the work week.
print(day_of_week("Friday"))    # Output: Last workday of the week.