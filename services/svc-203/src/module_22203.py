"""Service module 22203: business logic, no crypto."""


def calculate_total_22203(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22203():
    return 'module 22203 handles orders and invoices'
