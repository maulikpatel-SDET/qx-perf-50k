"""Service module 25234: business logic, no crypto."""


def calculate_total_25234(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25234():
    return 'module 25234 handles orders and invoices'
