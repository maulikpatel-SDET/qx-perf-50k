"""Service module 26257: business logic, no crypto."""


def calculate_total_26257(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26257():
    return 'module 26257 handles orders and invoices'
