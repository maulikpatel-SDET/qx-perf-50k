"""Service module 3895: business logic, no crypto."""


def calculate_total_3895(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3895():
    return 'module 3895 handles orders and invoices'
