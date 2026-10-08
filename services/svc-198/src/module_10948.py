"""Service module 10948: business logic, no crypto."""


def calculate_total_10948(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10948():
    return 'module 10948 handles orders and invoices'
