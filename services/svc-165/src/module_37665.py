"""Service module 37665: business logic, no crypto."""


def calculate_total_37665(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37665():
    return 'module 37665 handles orders and invoices'
