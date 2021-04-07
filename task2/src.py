from pathlib import Path
from typing import NoReturn


def main() -> NoReturn:
    print("Insert the path to the Python executable and press <Enter>")
    path = None
    try:
        path = Path(input())
    except Exception as e:
        print(f"Error {e} occured while parsing path, nothing to do")
        exit(1)

    if not path.exists():
        print("Such file doesn't exist")
        exit(1)


if __name__ == "__main__":
    main()
