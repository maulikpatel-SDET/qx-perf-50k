"""Service module 15383: business logic, no crypto."""


def calculate_total_15383(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15383():
    return 'module 15383 handles orders and invoices'
