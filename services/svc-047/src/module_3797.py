"""Service module 3797: business logic, no crypto."""


def calculate_total_3797(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3797():
    return 'module 3797 handles orders and invoices'
