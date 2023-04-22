import argparse
from .config import get_api_key


def main():
    api_key = get_api_key()
    if api_key is None:
        print("No API key found. Please run `summary config` first.")
        return

    parser = argparse.ArgumentParser(description="Summary")
    parser.add_argument(
        "-a", "--action", type=str, required=True, help="An action to perform"
    )
    parser.add_argument("-n", "--name", type=str, required=True, help="Your name")
    args = parser.parse_args()

    if args.action == "greet":
        print(f"Hello, {args.name}!")
    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()
