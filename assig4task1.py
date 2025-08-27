filename = "sample.txt"

try:
    print("\033[91mReading file content:\033[0m")  # Red colored text
    with open(filename, "r") as file:
        for idx, line in enumerate(file, 1):
            print(f"\033[92mLine {idx}: {line.strip()}\033[0m")  # Green colored text
except FileNotFoundError:
    print(f"\033[91mError: The file '{filename}' was not found.\033[0m")  # Red colored text