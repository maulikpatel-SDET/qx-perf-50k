"""Service module 15467: business logic, no crypto."""


def calculate_total_15467(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15467():
    return 'module 15467 handles orders and invoices'
