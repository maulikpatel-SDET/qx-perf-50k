"""Service module 1309: business logic, no crypto."""


def calculate_total_1309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1309():
    return 'module 1309 handles orders and invoices'
