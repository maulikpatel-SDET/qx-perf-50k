"""Service module 17703: business logic, no crypto."""


def calculate_total_17703(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17703():
    return 'module 17703 handles orders and invoices'
