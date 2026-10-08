"""Service module 18703: business logic, no crypto."""


def calculate_total_18703(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18703():
    return 'module 18703 handles orders and invoices'
