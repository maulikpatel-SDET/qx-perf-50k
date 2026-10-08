"""Service module 20531: business logic, no crypto."""


def calculate_total_20531(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20531():
    return 'module 20531 handles orders and invoices'
