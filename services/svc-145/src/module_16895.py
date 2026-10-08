"""Service module 16895: business logic, no crypto."""


def calculate_total_16895(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16895():
    return 'module 16895 handles orders and invoices'
