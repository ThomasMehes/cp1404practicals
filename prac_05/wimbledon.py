"""
Wimbledon Winners
Estimate: 45 minutes
Actual: 50 minutes
"""
import csv


def main():
    """program read file, process the data and displays each champions and how many times they have won.
       as well as the countries of the champions in alphabetical order."""
    filename = "wimbledon.csv"
    data = read_csv_file(filename)

    champions = get_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")

    countries_str = ", ".join(countries)
    print(f"\nThese {len(countries)} countries have won Wimbledon:\n{countries_str}")


def read_csv_file(filename):
    """Reads the .csv file and returns the data to main."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip the header row
        for row in reader:
            data.append(row)
    return data


def get_champions(data):
    """Counts the number of wins of each winner."""
    champions = {}
    for row in data:
        champion = row[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def get_countries(data):
    """Uses a set (no repeats) and reads every country a winner is from and sorts them alphabetical."""
    countries = set()
    for row in data:
        countries.add(row[1])
    return sorted(countries)


main()
