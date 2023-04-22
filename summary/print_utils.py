from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

LEVEL_COLORS = {
    "info": Fore.CYAN,
    "success": Fore.GREEN,
    "warning": Fore.YELLOW,
    "error": Fore.RED,
}


def print_colored(text, level="info"):
    color = LEVEL_COLORS.get(level, Fore.RESET)
    print(color + text + Style.RESET_ALL)


def input_colored(prompt, level="info"):
    color = LEVEL_COLORS.get(level, Fore.RESET)
    return input(color + prompt + Style.RESET_ALL)
