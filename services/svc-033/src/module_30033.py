"""Service module 30033: business logic, no crypto."""


def calculate_total_30033(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30033():
    return 'module 30033 handles orders and invoices'
