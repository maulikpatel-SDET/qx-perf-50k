"""Service module 31234: business logic, no crypto."""


def calculate_total_31234(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31234():
    return 'module 31234 handles orders and invoices'
