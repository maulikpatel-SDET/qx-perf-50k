"""Service module 46257: business logic, no crypto."""


def calculate_total_46257(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46257():
    return 'module 46257 handles orders and invoices'
