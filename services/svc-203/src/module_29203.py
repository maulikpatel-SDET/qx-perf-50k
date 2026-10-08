"""Service module 29203: business logic, no crypto."""


def calculate_total_29203(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29203():
    return 'module 29203 handles orders and invoices'
