"""
Hexadecimal color codes lookup
Estimate: 15 minutes
Actual:   20 minutes
"""

COLOR_TO_HEX = {
    "absolutezero": "#0048ba",
    "acidgreen": "#b0bf1a",
    "aliceblue": "#f0f8ff",
    "alizarincrimson": "#e32636",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "amethyst": "#9966cc",
    "antiquewhite": "#faebd7",
    "apricot": "#fbceb1",
    "aqua": "#00ffff"
}

def main():
    print("Available colors:", ", ".join(COLOR_TO_HEX.keys()))
    color_name = input("Enter color name: ").lower()
    while color_name != "":
        try:
            print(f"{color_name.capitalize()} is {COLOR_TO_HEX[color_name]}")
        except KeyError:
            print("Invalid color name")
        color_name = input("Enter color name: ").lower()

if __name__ == "__main__":
    main()