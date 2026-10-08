"""Service module 12554: business logic, no crypto."""


def calculate_total_12554(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12554():
    return 'module 12554 handles orders and invoices'
