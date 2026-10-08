"""Service module 33864: business logic, no crypto."""


def calculate_total_33864(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33864():
    return 'module 33864 handles orders and invoices'
