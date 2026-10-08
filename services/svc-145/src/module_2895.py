"""Service module 2895: business logic, no crypto."""


def calculate_total_2895(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2895():
    return 'module 2895 handles orders and invoices'
