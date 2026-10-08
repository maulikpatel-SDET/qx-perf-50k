"""Service module 15548: business logic, no crypto."""


def calculate_total_15548(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15548():
    return 'module 15548 handles orders and invoices'
