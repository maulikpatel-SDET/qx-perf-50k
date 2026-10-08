"""Service module 5203: business logic, no crypto."""


def calculate_total_5203(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5203():
    return 'module 5203 handles orders and invoices'
