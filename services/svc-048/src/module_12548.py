"""Service module 12548: business logic, no crypto."""


def calculate_total_12548(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12548():
    return 'module 12548 handles orders and invoices'
