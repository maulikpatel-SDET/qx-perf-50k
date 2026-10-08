"""Service module 26203: business logic, no crypto."""


def calculate_total_26203(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26203():
    return 'module 26203 handles orders and invoices'
