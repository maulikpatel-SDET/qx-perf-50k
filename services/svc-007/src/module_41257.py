"""Service module 41257: business logic, no crypto."""


def calculate_total_41257(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41257():
    return 'module 41257 handles orders and invoices'
