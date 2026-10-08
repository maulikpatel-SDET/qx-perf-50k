"""Service module 14703: business logic, no crypto."""


def calculate_total_14703(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14703():
    return 'module 14703 handles orders and invoices'
