"""Service module 12948: business logic, no crypto."""


def calculate_total_12948(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12948():
    return 'module 12948 handles orders and invoices'
