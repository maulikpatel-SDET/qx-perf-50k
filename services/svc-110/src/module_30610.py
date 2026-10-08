"""Service module 30610: business logic, no crypto."""


def calculate_total_30610(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30610():
    return 'module 30610 handles orders and invoices'
