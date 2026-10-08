"""Service module 42037: business logic, no crypto."""


def calculate_total_42037(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42037():
    return 'module 42037 handles orders and invoices'
