"""Service module 46749: business logic, no crypto."""


def calculate_total_46749(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46749():
    return 'module 46749 handles orders and invoices'
