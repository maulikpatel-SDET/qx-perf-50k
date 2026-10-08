"""Service module 18633: business logic, no crypto."""


def calculate_total_18633(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18633():
    return 'module 18633 handles orders and invoices'
