def get_task_info():
    
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    return task, priority, time_bound

def create_reminder(task, priority, time_bound):
    
    match priority:
       case "high":
            print(f"{task} is a High-priority task: .")
        case "medium":
            print(f"{task}is a Medium-priority task: .")
        case "low":
            print(f"{task}is a Low-priority task: .")
        case _:
            print(f"{task}:  (unknown priority).")
 
              
    if time_bound == "yes":
        reminder += " This task requires immediate attention today!"

    return reminder

def main():
    task, priority, time_bound = get_task_info()
    reminder = create_reminder(task, priority, time_bound)
    print(reminder)

if __name__ == "__main__":
    main()
