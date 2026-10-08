"""Service module 29665: business logic, no crypto."""


def calculate_total_29665(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29665():
    return 'module 29665 handles orders and invoices'
