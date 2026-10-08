"""Service module 9365: business logic, no crypto."""


def calculate_total_9365(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9365():
    return 'module 9365 handles orders and invoices'
