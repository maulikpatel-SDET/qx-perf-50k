"""Service module 39895: business logic, no crypto."""


def calculate_total_39895(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39895():
    return 'module 39895 handles orders and invoices'
