"""Service module 47610: business logic, no crypto."""


def calculate_total_47610(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47610():
    return 'module 47610 handles orders and invoices'
