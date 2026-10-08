"""Service module 48929: business logic, no crypto."""


def calculate_total_48929(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48929():
    return 'module 48929 handles orders and invoices'
