"""Service module 49679: business logic, no crypto."""


def calculate_total_49679(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49679():
    return 'module 49679 handles orders and invoices'
