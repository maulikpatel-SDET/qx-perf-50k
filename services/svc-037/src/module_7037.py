"""Service module 7037: business logic, no crypto."""


def calculate_total_7037(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7037():
    return 'module 7037 handles orders and invoices'
