import argparse
from colorama import Fore, Style, init
from .config import get_api_key

# Initialize colorama
init(autoreset=True)


def main():
    api_key = get_api_key()
    if api_key is None:
        print(Fore.RED + "Error: API key not found")
        return

    parser = argparse.ArgumentParser(description="My CLI tool")
    parser.add_argument(
        "-a", "--action", type=str, required=True, help="An action to perform"
    )
    parser.add_argument("-n", "--name", type=str, required=True, help="Your name")
    args = parser.parse_args()

    if args.action == "greet":
        print(Fore.GREEN + f"Hello, {args.name}!")
    else:
        print(Fore.YELLOW + f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()
