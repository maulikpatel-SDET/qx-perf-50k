"""Service module 7703: business logic, no crypto."""


def calculate_total_7703(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7703():
    return 'module 7703 handles orders and invoices'
