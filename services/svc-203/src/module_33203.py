"""Service module 33203: business logic, no crypto."""


def calculate_total_33203(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33203():
    return 'module 33203 handles orders and invoices'
