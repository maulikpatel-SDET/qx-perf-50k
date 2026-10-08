"""Service module 9037: business logic, no crypto."""


def calculate_total_9037(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9037():
    return 'module 9037 handles orders and invoices'
