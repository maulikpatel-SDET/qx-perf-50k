"""Service module 49895: business logic, no crypto."""


def calculate_total_49895(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49895():
    return 'module 49895 handles orders and invoices'
