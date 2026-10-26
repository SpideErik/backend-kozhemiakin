from pathlib import Path

from app.domain.order import Order
from app.services.importer import read_rows


def load_orders(path: Path) -> list[Order]:
    return [
        Order(waiter=row["waiter"], kopeks=int(row["kopeks"]))
        for row in read_rows(path)
    ]


def revenue_by_waiter(orders: list[Order], top: int = 0) -> dict[str, int]:
    """Считает выручку по каждому официанту.

    Args:
        orders (list[Order]): Заказы за смену, список не должен быть пустым.
        top (int, optional): Сколько официантов оставить в результате. Значение 0 - 
            оставить всех.

    Raises:
        ValueError: Если список заказов пуст.

    Returns:
        dict[str, int]: Выручка в копейках по именам официантов, в порядке убывания 
            суммы.
    """
    if not orders:
        raise ValueError("Список заказов пуст")
    totals: dict[str, int] = {}
    for order in orders:
        totals[order.waiter] = totals.get(order.waiter, 0) + order.kopeks
    ranked = sorted(totals.items(), key=lambda pair: -pair[1])
    if top:
        ranked = ranked[:top]
    return dict(ranked)


def sort_orders_in_place(orders: list[Order]) -> None:
    orders.sort(key=lambda order: -order.kopeks)
