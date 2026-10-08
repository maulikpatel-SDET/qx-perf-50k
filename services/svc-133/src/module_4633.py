"""Service module 4633: business logic, no crypto."""


def calculate_total_4633(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4633():
    return 'module 4633 handles orders and invoices'
