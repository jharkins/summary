import argparse
from .config import get_api_key
from .print_utils import print_colored
from .api import get_summary


def show_banner():
    with open("summary/banner.txt", "r") as banner_file:
        banner = banner_file.read()
        print_colored(banner, level="info")


def main():
    show_banner()

    api_key = get_api_key()
    if api_key is None:
        print_colored("Error: API key not found", level="error")
        return

    parser = argparse.ArgumentParser(
        description="Summary CLI tool",
        epilog="""\
This CLI tool uses the OpenAI GPT Chat API to generate summaries of input files from the command line.
Provide the path to the file you want to summarize, and the tool will return a concise summary of its content.
To get started, simply provide a file path as an argument, like this: 'summary example.txt'
""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("file", type=str, help="Path to the file you want to summarize")
    args = parser.parse_args()

    try:
        print_colored(f"Opening file: {args.file}", level="info")
        with open(args.file, "r") as file:
            file_content = file.read()
            print_colored("Generating summary...", level="info")
            summary = get_summary(file_content)
            print_colored("Summary:", level="info")
            print_colored(summary, level="success")
    except FileNotFoundError:
        print_colored(f"Error: File '{args.file}' not found", level="error")


if __name__ == "__main__":
    main()
