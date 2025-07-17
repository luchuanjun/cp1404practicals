import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = start_date  # datetime.date object
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.percent_complete = int(percent_complete)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.percent_complete}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.percent_complete == 100

def load_projects(filename="projects.txt"):
    projects = []
    with open(filename, "r") as file:
        file.readline()  # skip header
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) != 5:
                continue
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = parts[2]
            cost = parts[3]
            percent = parts[4]
            projects.append(Project(name, start_date, priority, cost, percent))
    return projects

def save_projects(projects, filename="projects.txt"):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tPercent Complete\n")
        for p in projects:
            file.write(f"{p.name}\t{p.start_date.strftime('%d/%m/%Y')}\t{p.priority}\t{p.cost_estimate}\t{p.percent_complete}\n")

def display_projects(projects):
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for p in sorted(incomplete):
        print(" ", p)
    print("Completed projects:")
    for p in sorted(complete):
        print(" ", p)

def filter_projects_by_date(projects, date):
    filtered = [p for p in projects if p.start_date > date]
    for p in sorted(filtered, key=lambda x: x.start_date):
        print(p)

def add_project():
    name = input("Name: ")
    date_str = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    priority = input("Priority: ")
    cost = input("Cost estimate: $")
    percent = input("Percent complete: ")
    return Project(name, start_date, priority, cost, percent)

def update_project(projects):
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_percent = input("New Percentage: ")
    new_priority = input("New Priority: ")

    if new_percent.strip() != "":
        project.percent_complete = int(new_percent)
    if new_priority.strip() != "":
        project.priority = int(new_priority)

def menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

def main():
    projects = load_projects()
    print(f"Loaded {len(projects)} projects from projects.txt")
    while True:
        menu()
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Filename to load: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Filename to save: ")
            save_projects(projects, filename)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == 'a':
            print("Let's add a new project")
            new_proj = add_project()
            projects.append(new_proj)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save = input("Would you like to save to projects.txt? (y/n): ").lower()
            if save == 'y':
                save_projects(projects)
                print("Projects saved.")
            print("Thank you for using project management program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
