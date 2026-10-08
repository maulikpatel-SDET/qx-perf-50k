"""Service module 4234: business logic, no crypto."""


def calculate_total_4234(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4234():
    return 'module 4234 handles orders and invoices'
