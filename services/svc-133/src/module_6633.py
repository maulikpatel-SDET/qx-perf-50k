"""Service module 6633: business logic, no crypto."""


def calculate_total_6633(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6633():
    return 'module 6633 handles orders and invoices'
