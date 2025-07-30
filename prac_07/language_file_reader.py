from programming_language import ProgrammingLanguage

def read_languages(filename="languages.csv"):
    languages = []
    with open(filename, "r") as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split(",")
            if len(parts) < 4:
                continue  # Skip malformed lines
            name = parts[0]
            typing = parts[1]
            reflection = parts[2].strip().lower() == 'true'
            pointer_arithmetic = parts[3].strip().lower() == 'true'
            lang = ProgrammingLanguage(name, typing, reflection, pointer_arithmetic)
            languages.append(lang)
    return languages

def main():
    langs = read_languages()
    for lang in langs:
        print(lang)

if __name__ == "__main__":
    main()
