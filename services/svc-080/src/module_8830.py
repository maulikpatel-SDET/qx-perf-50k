"""Service module 8830: business logic, no crypto."""


def calculate_total_8830(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8830():
    return 'module 8830 handles orders and invoices'
