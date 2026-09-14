from rich.console import Console
from rich.table import Table


def pretty_print_report(text: str):
    console = Console()
    lines = text.splitlines()
    table = Table(title=lines[0], show_header=False)

    table.add_column(justify="left", style="cyan", no_wrap=True)
    table.add_column(justify="right", style="magenta", no_wrap=True)

    for line in lines[2:]:
        columns = line.split(': ')
        table.add_row(columns[0], columns[1])
    console.print(table)


if __name__ == '__main__':
    pretty_print_report('TEST\n----\nline: 1\nline: 2')
