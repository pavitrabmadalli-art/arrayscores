import sys


def main():
    if len(sys.argv) > 1:
        raw_scores = " ".join(sys.argv[1:])
    else:
        raw_scores = input("Enter scores separated by spaces or commas: ")

    scores = [
        float(value)
        for value in raw_scores.replace(",", " ").split()
    ]

    if not scores:
        print("Enter at least one score.")
        return

    total = sum(scores)
    average = total / len(scores)

    print(f"Number of scores: {len(scores)}")
    print(f"Scores: {scores}")
    print(f"Sum: {total:g}")
    print(f"Average: {average:g}")
    print(f"Maximum: {max(scores):g}")
    print(f"Minimum: {min(scores):g}")
    
if __name__ == "__main__":
    main()