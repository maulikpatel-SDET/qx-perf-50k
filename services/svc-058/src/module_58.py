"""Service module 58: business logic, no crypto."""


def calculate_total_58(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_58():
    return 'module 58 handles orders and invoices'
