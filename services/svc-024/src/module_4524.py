"""Service module 4524: business logic, no crypto."""


def calculate_total_4524(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4524():
    return 'module 4524 handles orders and invoices'
