"""Service module 15309: business logic, no crypto."""


def calculate_total_15309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15309():
    return 'module 15309 handles orders and invoices'
