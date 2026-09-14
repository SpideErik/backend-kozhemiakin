from ..services import calculator


def format_report(expenses):
    total = calculator.calculate_total(expenses)
    average = calculator.calculate_average(expenses)
    lines = [
        "ОТЧЁТ ПО ПОЕЗДКЕ",
        "-" * 32,
        f"записей: {len(expenses)}",
        f"всего потрачено: {total} ₽",
        f"средняя трата: {average:.2f} ₽",
    ]
    return "\n".join(lines)
