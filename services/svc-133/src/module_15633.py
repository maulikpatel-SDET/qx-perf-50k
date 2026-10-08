"""Service module 15633: business logic, no crypto."""


def calculate_total_15633(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15633():
    return 'module 15633 handles orders and invoices'
