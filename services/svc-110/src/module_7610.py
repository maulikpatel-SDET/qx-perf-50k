"""Service module 7610: business logic, no crypto."""


def calculate_total_7610(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7610():
    return 'module 7610 handles orders and invoices'
