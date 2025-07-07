import csv
from typing import List, Tuple

def load_scores(path: str) -> List[Tuple[str, int]]:
    try:
        with open(path, 'r') as f:
            reader = csv.reader(f)
            return [(row[0], int(row[1])) for row in reader]
    except FileNotFoundError:
        print("File not found, starting fresh.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def add_score(records: List[Tuple[str, int]], name: str, score: int) -> None:
    records.append((name, score))

def save_scores(path: str, records: List[Tuple[str, int]]) -> None:
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(records)

def top_n(records: List[Tuple[str, int]], n: int) -> List[Tuple[str, int]]:
    return sorted(records, key=lambda x: x[1], reverse=True)[:n]

def main():
    scores_file = "scores.csv"
    records = load_scores(scores_file)

    while True:
        print("\n1. Show Top N Scores")
        print("2. Add New Score")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            try:
                n = int(input("Enter N: "))
                for name, score in top_n(records, n):
                    print(f"{name}: {score}")
            except ValueError:
                print("Invalid number.")
        elif choice == 2:
            name = input("Enter name: ")
            try:
                score = int(input("Enter score: "))
                add_score(records, name, score)
                save_scores(scores_file, records)
                print("Score added.")
            except ValueError:
                print("Invalid score.")
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
