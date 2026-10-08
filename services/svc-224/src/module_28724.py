"""Service module 28724: business logic, no crypto."""


def calculate_total_28724(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28724():
    return 'module 28724 handles orders and invoices'
