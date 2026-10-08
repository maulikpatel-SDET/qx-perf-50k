"""Service module 10309: business logic, no crypto."""


def calculate_total_10309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10309():
    return 'module 10309 handles orders and invoices'
