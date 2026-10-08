"""Service module 16864: business logic, no crypto."""


def calculate_total_16864(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16864():
    return 'module 16864 handles orders and invoices'
