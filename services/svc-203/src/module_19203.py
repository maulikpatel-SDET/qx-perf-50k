"""Service module 19203: business logic, no crypto."""


def calculate_total_19203(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19203():
    return 'module 19203 handles orders and invoices'
