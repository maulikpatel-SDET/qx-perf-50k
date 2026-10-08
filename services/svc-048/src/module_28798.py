"""Service module 28798: business logic, no crypto."""


def calculate_total_28798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28798():
    return 'module 28798 handles orders and invoices'
