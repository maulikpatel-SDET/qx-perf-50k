"""Service module 9531: business logic, no crypto."""


def calculate_total_9531(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9531():
    return 'module 9531 handles orders and invoices'
