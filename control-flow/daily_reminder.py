def get_task_info():
    
    task = input("Enter the task description: ")
    priority = input("Enter the task priority (high, medium, low): ").lower()
    time_bound = input("Is the task time-sensitive? (yes or no): ").lower()
    return task, priority, time_bound

def create_reminder(task, priority, time_bound):
    
    match priority:
        case "high":
            reminder = f"High-priority task: {task}."
        case "medium":
            reminder = f"Medium-priority task: {task}."
        case "low":
            reminder = f"Low-priority task: {task}."
        case _:
            reminder = f"Task: {task} (unknown priority)."

              
    if time_bound == "yes":
        reminder += " This task requires immediate attention today!"

    return reminder

def main():
    task, priority, time_bound = get_task_info()
    reminder = create_reminder(task, priority, time_bound)
    print(reminder)

if __name__ == "__main__":
    main()