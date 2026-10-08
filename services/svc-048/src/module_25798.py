"""Service module 25798: business logic, no crypto."""


def calculate_total_25798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25798():
    return 'module 25798 handles orders and invoices'
