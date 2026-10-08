"""Service module 25836: business logic, no crypto."""


def calculate_total_25836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25836():
    return 'module 25836 handles orders and invoices'
