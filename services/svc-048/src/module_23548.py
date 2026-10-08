"""Service module 23548: business logic, no crypto."""


def calculate_total_23548(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23548():
    return 'module 23548 handles orders and invoices'
