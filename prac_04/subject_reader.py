FILENAME = "subject_data.txt"

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])  # convert student number to int
            data.append(parts)
    return data

def display_subject_details(data):
    """Display formatted details about each subject."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")

def main():
    data = load_data()
    display_subject_details(data)

if __name__ == "__main__":
    main()
