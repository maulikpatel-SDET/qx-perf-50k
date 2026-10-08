"""Service module 35203: business logic, no crypto."""


def calculate_total_35203(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35203():
    return 'module 35203 handles orders and invoices'
