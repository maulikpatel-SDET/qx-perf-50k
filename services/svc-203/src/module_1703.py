"""Service module 1703: business logic, no crypto."""


def calculate_total_1703(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1703():
    return 'module 1703 handles orders and invoices'
