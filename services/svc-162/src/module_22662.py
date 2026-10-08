"""Service module 22662: business logic, no crypto."""


def calculate_total_22662(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22662():
    return 'module 22662 handles orders and invoices'
