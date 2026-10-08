"""Service module 16037: business logic, no crypto."""


def calculate_total_16037(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16037():
    return 'module 16037 handles orders and invoices'
