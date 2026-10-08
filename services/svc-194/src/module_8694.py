"""Service module 8694: business logic, no crypto."""


def calculate_total_8694(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8694():
    return 'module 8694 handles orders and invoices'
