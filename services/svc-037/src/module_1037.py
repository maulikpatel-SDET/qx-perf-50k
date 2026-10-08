"""Service module 1037: business logic, no crypto."""


def calculate_total_1037(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1037():
    return 'module 1037 handles orders and invoices'
