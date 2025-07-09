from guitar import Guitar

def load_guitars(filename="guitars.csv"):
    guitars = []
    with open(filename, "r") as file:
        for line in file:
            if line.strip() == "":
                continue
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue
            name, year, cost = parts
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars

def save_guitars(guitars, filename="guitars.csv"):
    with open(filename, "w") as file:
        for g in guitars:
            file.write(f"{g.name},{g.year},{g.cost}\n")

def display_guitars(guitars):
    for g in guitars:
        print(g)

def main():
    guitars = load_guitars()
    print("Guitars loaded:")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    # Ask user to add new guitar
    print("\nAdd a new guitar:")
    name = input("Name: ")
    year = input("Year: ")
    cost = input("Cost: ")
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)

    save_guitars(guitars)
    print("\nNew guitar list saved.")

if __name__ == "__main__":
    main()
