"""Service module 26864: business logic, no crypto."""


def calculate_total_26864(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26864():
    return 'module 26864 handles orders and invoices'
