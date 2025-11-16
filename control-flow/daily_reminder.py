
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


match priority:
    case "high":
        priority_text = f"'{task}' is a high priority task"
    case "medium":
        priority_text = f"'{task}' is a medium priority task"
    case "low":
        priority_text = f"'{task}' is a low priority task"
    case _:
        priority_text = f"'{task}' is a task"

if time_bound == "yes":
    message = priority_text + " that requires immediate attention today!"
else:
    message = f"Note: {priority_text}. Consider completing it when you have free time."

print("Reminder: " + message)
