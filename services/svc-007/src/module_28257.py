"""Service module 28257: business logic, no crypto."""


def calculate_total_28257(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28257():
    return 'module 28257 handles orders and invoices'
