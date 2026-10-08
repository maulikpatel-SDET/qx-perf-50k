"""Service module 17234: business logic, no crypto."""


def calculate_total_17234(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17234():
    return 'module 17234 handles orders and invoices'
