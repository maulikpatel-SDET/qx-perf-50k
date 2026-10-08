"""Service module 31703: business logic, no crypto."""


def calculate_total_31703(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31703():
    return 'module 31703 handles orders and invoices'
