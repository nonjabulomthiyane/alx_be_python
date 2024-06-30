task = input("Enter the task description: ")
priority = input("Enter the priority level (high, medium, low): ")
time_bound = input("Is the task time-bound? (yes or no): ")
match priority:
    case 'high':
        reminder = f"High priority task: {task}"
    case 'medium':
        reminder = f"Medium priority task: {task}"
    case 'low':
        reminder = f"Low priority task: {task}"
    case _:
        print(f"Invalid priority level '{priority}'. Please choose from high, medium, low.")
if time_bound == 'yes':
    reminder += " that requires immediate attention today!"
print(reminder)
