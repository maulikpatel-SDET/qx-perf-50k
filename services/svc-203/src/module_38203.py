"""Service module 38203: business logic, no crypto."""


def calculate_total_38203(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38203():
    return 'module 38203 handles orders and invoices'
