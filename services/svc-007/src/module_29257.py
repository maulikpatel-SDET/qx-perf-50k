"""Service module 29257: business logic, no crypto."""


def calculate_total_29257(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29257():
    return 'module 29257 handles orders and invoices'
