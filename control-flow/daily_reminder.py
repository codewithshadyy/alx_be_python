




print("=== Daily Reminder ===")

while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task cannot be empty. Please enter something.\n")


priority = input("Priority (high/medium/low): ").lower().strip()


time_bound = input("Is it time-bound? (yes/no): ").lower().strip()


match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority level"


if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = "Note: " + reminder + ". Consider completing it when you have free time."

print("\nReminder:", reminder)


