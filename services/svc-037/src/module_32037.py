"""Service module 32037: business logic, no crypto."""


def calculate_total_32037(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32037():
    return 'module 32037 handles orders and invoices'
