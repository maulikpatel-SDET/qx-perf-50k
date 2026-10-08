"""Service module 7548: business logic, no crypto."""


def calculate_total_7548(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7548():
    return 'module 7548 handles orders and invoices'
