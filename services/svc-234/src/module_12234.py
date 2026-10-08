"""Service module 12234: business logic, no crypto."""


def calculate_total_12234(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12234():
    return 'module 12234 handles orders and invoices'
