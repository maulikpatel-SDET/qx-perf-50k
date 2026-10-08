"""Service module 40895: business logic, no crypto."""


def calculate_total_40895(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40895():
    return 'module 40895 handles orders and invoices'
