"""Print in console with colors"""
import colorama


def color_print(result):
    """Print lines with different colors"""
    colorama.init()
    [print(random_color(chunk) + chunk) for chunk in result if chunk]
    colorama.deinit()


def random_color(data):
    """Return random color"""
    colors = [colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.BLUE,
              colorama.Fore.MAGENTA, colorama.Fore.CYAN, colorama.Fore.WHITE]
    return colors[hash(data) % len(colors)]
