"""Service module 31037: business logic, no crypto."""


def calculate_total_31037(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31037():
    return 'module 31037 handles orders and invoices'
