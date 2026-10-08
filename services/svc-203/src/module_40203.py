"""Service module 40203: business logic, no crypto."""


def calculate_total_40203(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40203():
    return 'module 40203 handles orders and invoices'
