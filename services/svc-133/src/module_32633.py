"""Service module 32633: business logic, no crypto."""


def calculate_total_32633(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32633():
    return 'module 32633 handles orders and invoices'
