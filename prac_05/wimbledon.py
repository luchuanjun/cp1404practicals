"""
Wimbledon data analysis
Estimate: 45 minutes
Actual:   60 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    records = load_data()
    champion_counts = count_champions(records)
    countries = get_countries(records)

    print("Wimbledon Champions:")
    for name, count in champion_counts.items():
        print(f"{name} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def load_data():
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append({
                "year": int(parts[0]),
                "champion": parts[2],
                "country": parts[1]
            })
    return records


def count_champions(records):
    counts = {}
    for record in records:
        try:
            counts[record["champion"]] += 1
        except KeyError:
            counts[record["champion"]] = 1
    return counts


def get_countries(records):
    return {record["country"] for record in records}


if __name__ == "__main__":
    main()