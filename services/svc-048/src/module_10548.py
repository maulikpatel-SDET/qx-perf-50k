"""Service module 10548: business logic, no crypto."""


def calculate_total_10548(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10548():
    return 'module 10548 handles orders and invoices'
