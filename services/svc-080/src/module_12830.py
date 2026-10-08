"""Service module 12830: business logic, no crypto."""


def calculate_total_12830(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12830():
    return 'module 12830 handles orders and invoices'
