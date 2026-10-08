"""Service module 12203: business logic, no crypto."""


def calculate_total_12203(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12203():
    return 'module 12203 handles orders and invoices'
