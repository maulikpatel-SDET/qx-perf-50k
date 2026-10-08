"""Service module 8234: business logic, no crypto."""


def calculate_total_8234(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8234():
    return 'module 8234 handles orders and invoices'
