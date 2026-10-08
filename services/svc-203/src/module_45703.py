"""Service module 45703: business logic, no crypto."""


def calculate_total_45703(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45703():
    return 'module 45703 handles orders and invoices'
